"""
Admin-only API views for managing users and their questionnaire data.
All views require the requesting user to be in the 'Admins' group.
"""
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .permissions import IsAdminPermission
from .serializers import (
    UserDetailSerializer, UserDetail2Serializer,
    EQuestionsSerializer, EQuestions1Serializer, EQuestions2Serializer,
    EQuestions3Serializer, EQuestions4Serializer, EQuestions5Serializer,
    EQuestions6Serializer, EQuestions7Serializer, EQuestions8Serializer,
    DocumentsPreparedSerializer,
    referalResponseSerializer, preRatingSerializer,
    LendingRequirementsSerializer,
)
from registration.models import UserDetail, UserDetail2
from entreprise_questions.models import (
    EQuestions, EQuestions1, EQuestions2, EQuestions3, EQuestions4,
    EQuestions5, EQuestions6, EQuestions7, EQuestions8,
    DocumentsPrepared, ReferalResponse, PreRating, LendingRequirements,
)


# ── Mapping of step keys to (Model, Serializer) ─────────────────────────────

STEP_MAP = {
    'contact':           (UserDetail,          UserDetailSerializer),
    'account':           (UserDetail2,         UserDetail2Serializer),
    'stage':             (EQuestions1,          EQuestions1Serializer),
    'entity':            (EQuestions2,          EQuestions2Serializer),
    'preCapital':        (EQuestions3,          EQuestions3Serializer),
    'preMarket':         (EQuestions4,          EQuestions4Serializer),
    'plannedRaise':      (EQuestions5,          EQuestions5Serializer),
    'rounds':            (EQuestions6,          EQuestions6Serializer),
    'useOfFunds':        (EQuestions7,          EQuestions7Serializer),
    'risk':              (EQuestions8,          EQuestions8Serializer),
    'costTime':          (EQuestions,           EQuestionsSerializer),
    'docsPrepared':      (DocumentsPrepared,    DocumentsPreparedSerializer),
    'preRating':         (PreRating,            preRatingSerializer),
    'referral':          (ReferalResponse,      referalResponseSerializer),
    'lending':           (LendingRequirements,  LendingRequirementsSerializer),
}


class AdminUserListCreateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminPermission]

    def get(self, request):
        users = User.objects.all().order_by('-date_joined')
        data = []
        for u in users:
            contact = None
            try:
                detail = UserDetail.objects.get(user=u)
                contact = {
                    'display_name': detail.Last_Name or '',
                    'email': detail.User_Email or '',
                    'companyWebsite': detail.Company_Website or '',
                    'primaryBusinessAddress': detail.Business_Adress or '',
                }
            except UserDetail.DoesNotExist:
                pass

            data.append({
                'id': u.id,
                'username': u.username,
                'email': u.email,
                'is_active': u.is_active,
                'is_staff': u.is_staff,
                'date_joined': u.date_joined.isoformat(),
                'contact': contact,
            })
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email', '')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {'error': 'username and password are required'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {'error': 'A user with this username already exists'},
                status=status.HTTP_409_CONFLICT,
            )

        user = User.objects.create_user(
            username=username, email=email, password=password,
        )
        user.is_active = True
        user.save()

        return Response(
            {'id': user.id, 'username': user.username, 'email': user.email, 'is_active': user.is_active},
            status=status.HTTP_201_CREATED,
        )


class AdminActivateUserView(APIView):
    permission_classes = [IsAuthenticated, IsAdminPermission]

    def post(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        user.is_active = True
        user.save()
        return Response({'message': f'User {user.username} activated.'}, status=status.HTTP_200_OK)


class AdminUserAllDataView(APIView):
    permission_classes = [IsAuthenticated, IsAdminPermission]

    def get(self, request, user_id):
        target_user = get_object_or_404(User, pk=user_id)
        result = {}

        for step_key, (Model, Serializer) in STEP_MAP.items():
            try:
                obj = Model.objects.get(user=target_user)
                result[step_key] = Serializer(obj).data
            except Model.DoesNotExist:
                result[step_key] = None

        return Response({
            'user': {
                'id': target_user.id,
                'username': target_user.username,
                'email': target_user.email,
                'is_active': target_user.is_active,
            },
            'steps': result,
        }, status=status.HTTP_200_OK)


class AdminUserStepDataView(APIView):
    permission_classes = [IsAuthenticated, IsAdminPermission]

    def post(self, request, user_id, step_key):
        target_user = get_object_or_404(User, pk=user_id)

        if step_key not in STEP_MAP:
            return Response(
                {'error': f'Unknown step: {step_key}'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        Model, Serializer = STEP_MAP[step_key]

        # Special handling for DocumentsPrepared
        if step_key == 'docsPrepared':
            return self._handle_docs_prepared(request, target_user, Model, Serializer)

        serializer = Serializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Special handling for PreRating (merge JSON data)
        if step_key == 'preRating':
            try:
                existing = Model.objects.get(user=target_user)
                new_data = serializer.validated_data.get('preratings', {})
                if isinstance(existing.preratings, dict):
                    existing.preratings.update(new_data)
                else:
                    existing.preratings = new_data
                existing.save()
                return Response(Serializer(existing).data, status=status.HTTP_200_OK)
            except Model.DoesNotExist:
                serializer.save(user=target_user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        # For all other steps: update if exists, create if not
        try:
            existing = Model.objects.get(user=target_user)
            for attr, value in serializer.validated_data.items():
                setattr(existing, attr, value)
            existing.save()
            return Response(Serializer(existing).data, status=status.HTTP_200_OK)
        except Model.DoesNotExist:
            serializer.save(user=target_user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def _handle_docs_prepared(self, request, target_user, Model, Serializer):
        BOOL_FIELDS = {
            'summaryofOffering': 'summary_of_offering',
            'financialForecast': 'financial_forecast',
            'leanBusinessModelCanvas': 'lean_business_model',
            'presentationDeck': 'presentation_deck',
            'leadershipOverview': 'leadership_overview',
            'exitStrategy': 'exit_strategy',
            'offeringDocuments': 'offering_documents',
            'aiGeneratedDeepDive': 'ai_generated_deep_dive',
            'virtualDataroom': 'virtual_data_room',
        }

        try:
            obj = Model.objects.get(user=target_user)
        except Model.DoesNotExist:
            obj = Model(user=target_user)

        for camel_name, model_field in BOOL_FIELDS.items():
            val = request.data.get(camel_name, False)
            if val is True or val == 'true' or val == 1 or val == '1':
                setattr(obj, model_field, 1)
            else:
                setattr(obj, model_field, 0)

        obj.save()
        return Response(Serializer(obj).data, status=status.HTTP_200_OK)


class AdminMatchPDFView(APIView):
    """
    GET /api/admin/users/<user_id>/match-pdf → Run matching for target user
    and return the PDF. Temporarily swaps request.user so the existing
    pdf() view runs against the target user's data.
    """
    permission_classes = [IsAuthenticated, IsAdminPermission]

    def get(self, request, user_id):
        from Matching_Algorithm.views import pdf as pdf_view

        target_user = get_object_or_404(User, pk=user_id)

        # Temporarily swap request.user to the target user
        original_user = request.user
        request.user = target_user

        try:
            response = pdf_view(request)
            return response
        except Exception as e:
            return Response(
                {'error': f'Matching failed: {str(e)}. Ensure all questionnaire steps are completed.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        finally:
            # Always restore the original admin user
            request.user = original_user
