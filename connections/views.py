from django.shortcuts import render,get_object_or_404,HttpResponse
from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import UserDetailSerializer, UserDetail2Serializer,EQuestionsSerializer,\
EQuestions1Serializer,EQuestions2Serializer,EQuestions3Serializer,EQuestions4Serializer,EQuestions5Serializer,\
EQuestions6Serializer,EQuestions7Serializer, EQuestions8Serializer, EQuestions9Serializer,EQuestions10Serializer,\
EQuestions11Serializer,EQuestions12Serializer,EQuestions13Serializer,EQuestions14Serializer,referalResponseSerializer,\
IQuestions1Serializer,IQuestions2Serializer,VQuestion1Serializer,MatchDataSerializer,MatchDataEfficientSerializer,PurchasesSerializer,DocumentsPreparedSerializer,payLoadSerializer,preRatingSerializer,LendingRequirementsSerializer
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser  # Add this import for permissions
from rest_framework.authentication import TokenAuthentication  # Or use other authentication methods
from registration.models import UserDetail,UserDetail2
from entreprise_questions.models import EQuestions,EQuestions1,EQuestions2,EQuestions3,EQuestions4,EQuestions5,\
EQuestions6,EQuestions7,EQuestions8,EQuestions9,EQuestions10,EQuestions11,EQuestions12,EQuestions13,PreRating,\
EQuestions14,DocumentsPrepared,ReferalResponse,LendingRequirements
from iquestions.models import IQuestions1,IQuestions2
from CM_Market.models import VQuestion1
from Matching_Algorithm.models import Letter_Response,Purchases
from Matching_Algorithm.views import Match
from connections.models import Match_Data,pay_load_string
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User,Group
from rest_framework import generics,mixins,viewsets
from rest_framework.exceptions import NotFound
from .permissions import IsAdminPermission
from Matching_Algorithm.views import Match,pdf
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework.views import APIView
from django.db.models import Q

class UserDetailAPIView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        GET method to get user inputs
        """
        if request.user.groups.filter(name='Admins').exists():
            # Admins get all user details
            queryset = UserDetail.objects.all()
            serializer = UserDetailSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Non-admin users get only their own data
        queryset = UserDetail.objects.filter(user=request.user)
        if not queryset.exists():
            raise NotFound("There is No response for this user yet,post first!!!")
        
        serializer = UserDetailSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def create(self, request):
        """
        POST method to add user details
        """
        serializer = UserDetailSerializer(data=request.data)

        if serializer.is_valid():
            try:
                a = UserDetail.objects.get(user=self.request.user)
                return Response({"message":"Multiple Response, Please Delete the old response of user."},status=status.HTTP_409_CONFLICT)
            except:    
                serializer.save(user=self.request.user)            
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#for account in front end
class UserDetail2APIView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        GET method to get user inputs
        """
        if request.user.groups.filter(name='Admins').exists():
            # Admins get all user details
            queryset = UserDetail2.objects.all()
            serializer = UserDetail2Serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Non-admin users get only their own data
        queryset = UserDetail2.objects.filter(user=request.user)
        if not queryset.exists():
            raise NotFound("There is No response for this user yet,post first!!!")        
        serializer = UserDetail2Serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def create(self, request):
        """
        POST method to add user details
        """
        serializer = UserDetail2Serializer(data=request.data)

        if serializer.is_valid():
            try:
                a = UserDetail2.objects.get(user=self.request.user)
                return Response({"message":"Multiple Response, Please Delete the old response of user."},status=status.HTTP_409_CONFLICT)
            except:    
                serializer.save(user=self.request.user)            
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EQuestionsAPIView(viewsets.ViewSet):
    def list(self,request):
        """
        GET method to get user inputs
        """
        if request.user.groups.filter(name='Admins').exists():
            # Admins get all user details
            queryset = EQuestions.objects.all()
            serializer = EQuestionsSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Non-admin users get only their own data
        queryset = EQuestions.objects.filter(user=request.user)
        if not queryset.exists():
            raise NotFound("There is No response for this user yet,post first!!!")        
        serializer = EQuestionsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """
        POST method to add user details
        """
        serializer = EQuestionsSerializer(data=request.data)

        if serializer.is_valid():
            try:
                a = EQuestions.objects.get(user=self.request.user)
                return Response({"message":"Multiple Response, Please Delete the old response of user."},status=status.HTTP_409_CONFLICT)
            except:    
                serializer.save(user=self.request.user)
                try:
                    data,created = EQuestions.objects.get_or_create(user=self.request.user)
                except Exception as e:
                    return Response({"message":"Multiple Response delete the old user data"},status = status.HTTP_409_CONFLICT)
                
                match serializer.validated_data.get('Selected_Option'):
                    case '0 - $499'|'0-$499':
                        data.RC_zero_to_499 = 1
                    
               
                    case '$500 - $999'|'$500-$999':
                        data.RC_500_to_999 = 1
                
                    case '$1000 - $2499'|'$1000-$2499':
                        data.RC_1000_to_2499 = 1
                    
                    case '$2500 - $4999'|'$2500-$4999':
                        data.RC_2500_to_4999 = 1
                        
                    case '$5000 - $9999'|'5000 - $9999':
                        data.RC_5000_to_9999 = 1
                        
                    case '$10000 - $24999'|'$10000-$24999':
                        data.RC_10000_to_24999 = 1
                        
                    case '$25000 - $49999'|'$25000-$49999':
                        data.RC_25000_to_49999 = 1
                        
                    case '$50000+':
                        data.RC_More_Than_50000 = 1
                
                match serializer.validated_data.get('Selected_Option2'):
                    case '1 Day to 1 Week':
                        data.RT_1D_to_1W = 1

                    case '1 Week to 2 Weeks':
                        data.RT_1W_to_2W = 1

                    case '2 Weeks to 4 Weeks':
                        data.RT_2W_to_4W = 1
                    case '1 Month to 2 Months':
                        data.RT_1M_to_2M = 1
                    case '2 Months to 3 Months':
                        data.RT_2M_to_3M = 1
                    case '3 Months to 6 Months':
                        data.RT_3M_to_6M = 1
                    case '6 Months to 12 Months':
                        data.RT_6M_to_12M = 1
                    case 'More than 1 year':
                        data.RT_More_Than_a_Year = 1                    
                data.save()            

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class EQuestions1APIView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        GET method to get user inputs
        """
        if request.user.groups.filter(name='Admins').exists():
            # Admins get all user details
            queryset = EQuestions1.objects.all()
            serializer = EQuestions1Serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Non-admin users get only their own data
        queryset = EQuestions1.objects.filter(user=request.user)
        if not queryset.exists():
            raise NotFound("There is No response for this user yet,post first!!!")
        
        serializer = EQuestions1Serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def create(self, request):
        """
        POST method to add user details
        """
        serializer = EQuestions1Serializer(data=request.data)

        if serializer.is_valid():
            try:
                a = EQuestions1.objects.get(user=self.request.user)
                return Response({"message":"Multiple Response, Please Delete the old response of user."},status=status.HTTP_409_CONFLICT)
            except:    
                serializer.save(user=self.request.user)
                try:
                    data,created = EQuestions1.objects.get_or_create(user=self.request.user)
                except Exception as e:
                    return Response({"message":"Multiple Response delete the old user data"},status = status.HTTP_409_CONFLICT)
                
                match serializer.validated_data.get('Selected_Option'):
                    case 'Idea':
                        data.Idea = 1
                        data.save()
               
                    case 'Formation':
                        data.Formation = 1
                        data.save()
                    case 'Start-Up':
                        data.Start_Up = 1
                        data.save()
                    case 'Growth':
                        data.Growth = 1
                        data.save()
                    case 'M & A':
                        data.M_And_A = 1
                        data.save()
                    case 'Preparing for Public':
                        data.Preparing_For_Public = 1
                        data.save()
                    case 'Distressted'|'Distressed':
                        data.Distressed = 1
                        data.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EQuestions2APIView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        GET method to get user inputs
        """
        if request.user.groups.filter(name='Admins').exists():
            # Admins get all user details
            queryset = EQuestions2.objects.all()
            serializer = EQuestions2Serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Non-admin users get only their own data
        queryset = EQuestions2.objects.filter(user=request.user)
        if not queryset.exists():
            raise NotFound("There is No response for this user yet,post first!!!")
        
        serializer = EQuestions2Serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def create(self, request):
        """
        POST method to add user details
        """
        serializer = EQuestions2Serializer(data=request.data)

        if serializer.is_valid():
            try:
                a = EQuestions2.objects.get(user=self.request.user)
                return Response({"message":"Multiple Response, Please Delete the old response of user."},status=status.HTTP_409_CONFLICT)
            except:    
                serializer.save(user=self.request.user)
                try:
                    data,created = EQuestions2.objects.get_or_create(user=self.request.user)
                except Exception as e:
                    return Response({"message":"Multiple Response delete the old user data"},status = status.HTTP_409_CONFLICT)
                
                match serializer.validated_data.get('Selected_Option'):
                    case 'None (TBD)':
                        data.No_Business = 1
                        data.save()
               
                    case 'Sole Proprietorship':
                        data.Sole_Proprietorship = 1
                        data.save()
                    case 'LLC':
                        data.LLC = 1
                        data.save()
                    case 'LP':
                        data.LP = 1
                        data.save()
                    case 'GP':
                        data.GP = 1
                        data.save()
                    case 'S Corp':
                        data.S_Corporation = 1
                        data.save()
                    case 'C Corp':
                        data.C_Corp = 1
                        data.save()
                    case 'Other':
                        data.Other = 1
                        data.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EQuestions3APIView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        GET method to get user inputs
        """
        if request.user.groups.filter(name='Admins').exists():
            # Admins get all user details
            queryset = EQuestions3.objects.all()
            serializer = EQuestions3Serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Non-admin users get only their own data
        queryset = EQuestions3.objects.filter(user=request.user)
        if not queryset.exists():
            raise NotFound("There is No response for this user yet,post first!!!")
        
        serializer = EQuestions3Serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def create(self, request):
        """
        POST method to add user details
        """
        serializer = EQuestions3Serializer(data=request.data)

        if serializer.is_valid():
            try:
                a = EQuestions3.objects.get(user=self.request.user)
                return Response({"message":"Multiple Response, Please Delete the old response of user."},status=status.HTTP_409_CONFLICT)
            except:    
                serializer.save(user=self.request.user)
                try:
                    data,created = EQuestions3.objects.get_or_create(user=self.request.user)
                except Exception as e:
                    return Response({"message":"Multiple Response delete the old user data"},status = status.HTTP_409_CONFLICT)
                
                match serializer.validated_data.get('Selected_Option'):
                    case 'Less Than $25,000':
                        data.Less_25k = 1
                        data.save()
               
                    case '$26,000 to $100,000':
                        data.More_25K_Less_100k = 1
                        data.save()

                    case '$101,000 to $250,000':
                        data.More_100k_Less_250K = 1
                        data.save()
                    case '$251,000 to $500,000':
                        data.More_250k_Less_500K = 1
                        data.save()
                    case '$501,000 to $1,000,000':
                        data.More_500K_Less_1M = 1
                        data.save()
                    case '$1,000,001 to $2,000,000':
                        data.More_1M_Less_2M = 1
                        data.save()
                    case '$2,000,001 to $5,000,000':
                        data.More_2M_Less_5M = 1
                        data.save()
                    case '$5,000,001 to $10,000,000':
                        data.More_5M_Less_10M = 1
                        data.save()
                    case 'More Than $10,000,000':
                        data.More_10M = 1
                        data.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EQuestions4APIView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        GET method to get user inputs
        """
        if request.user.groups.filter(name='Admins').exists():
            # Admins get all user details
            queryset = EQuestions4.objects.all()
            serializer = EQuestions4Serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Non-admin users get only their own data
        queryset = EQuestions4.objects.filter(user=request.user)
        if not queryset.exists():
            raise NotFound("There is No response for this user yet,post first!!!")
        
        serializer = EQuestions4Serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def create(self, request):
        """
        POST method to add user details
        """
        serializer = EQuestions4Serializer(data=request.data)

        if serializer.is_valid():
            try:
                a = EQuestions4.objects.get(user=self.request.user)
                return Response({"message":"Multiple Response, Please Delete the old response of user."},status=status.HTTP_409_CONFLICT)
            except:    
                serializer.save(user=self.request.user)
                try:
                    data,created = EQuestions4.objects.get_or_create(user=self.request.user)
                except Exception as e:
                    return Response({"message":"Multiple Response delete the old user data"},status = status.HTTP_409_CONFLICT)
                
                for option in serializer.validated_data.get('Selected_Options'):
                    if option == 'Accelerator':
                        data.Accelerator = 1
                    elif option == 'Bonds':
                        data.Bonds = 1
                    elif option == 'Commercial Banking':
                        data.Comercial_Banking = 1
                    elif option == 'Cryptocurrency':
                        data.Cryptocurrency = 1
                    elif option == 'EB5 Immigration':
                        data.EB5_Immigration = 1
                    elif option == 'Enterprise Zones':
                        data.Enterprise_Zones = 1
                    elif option == 'Factoring':
                        data.Factoring = 1
                    elif option == 'Grants':
                        data.Grants = 1
                    elif option == 'Hedge Funds':
                        data.Hedge_Funds = 1
                    elif option == 'Incubator':
                        data.Incubator = 1
                    elif option == 'Investment Banking':
                        data.Investment_Banking = 1
                    elif option == 'Other (Owner Equity)':
                        data.Other_Owner_Equity = 1
                    elif option == 'Private Debt (Officer Loans to Startup)':
                        data.Private_Debt = 1
                    elif option == 'Private Equity Securities':
                        data.Private_Equity = 1
                    elif option == 'Public Offering':
                        data.Public_Offereing = 1
                    elif option == 'Real Estate':
                        data.Real_Estate = 1
                    elif option == 'Royalty Financing':
                        data.Royalty_Financing = 1
                    elif option == 'Small Business Administration (SBA)':
                        data.Small_Business_Administration = 1
                    elif option == 'Venture Capital':
                        data.Venture_Capital = 1
                    elif option == "Unsure/Don't Know":
                        data.Unsure = 1         

                # Save the updated data object
                data.save()


            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)               


class EQuestions5APIView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        GET method to get user inputs
        """
        if request.user.groups.filter(name='Admins').exists():
            # Admins get all user details
            queryset = EQuestions5.objects.all()
            serializer = EQuestions5Serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Non-admin users get only their own data
        queryset = EQuestions5.objects.filter(user=request.user)
        if not queryset.exists():
            raise NotFound("There is No response for this user yet,post first!!!")
        
        serializer = EQuestions5Serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """
        POST method to add user details
        """
        serializer = EQuestions5Serializer(data=request.data)

        if serializer.is_valid():
            try:
                a = EQuestions5.objects.get(user=self.request.user)
                return Response({"message":"Multiple Response, Please Delete the old response of user."},status=status.HTTP_409_CONFLICT)
            except:    
                serializer.save(user=self.request.user)
                try:
                    data,created = EQuestions5.objects.get_or_create(user=self.request.user)
                except Exception as e:
                    return Response({"message":"Multiple Response delete the old user data"},status = status.HTTP_409_CONFLICT)
                
                match serializer.validated_data.get('Selected_Option'):
                    case 'Less Than $25,000':
                        data.Less_25k = 1
                        data.save()
               
                    case '$25,000 to $100,000':
                        data.More_25K_Less_100k = 1
                        data.save()

                    case '$100,000 to $249,999':
                        data.More_100k_Less_250K = 1
                        data.save()
                    case '$250,000 to $499,999':
                        data.More_250k_Less_500K = 1
                        data.save()
                    case '$500,000 to $999,999':
                        data.More_500K_Less_1M = 1
                        data.save()
                    case '$1,000,000 to $1,349,999':
                        data.More_1M_Less_1_35M = 1
                        data.save()
                    case '$1,350,000 to $1,999,999':
                        data.More_1_35M_Less_2M = 1
                        data.save()
                    case '$2,000,000 to $4,999,999':
                        data.More_2M_Less_5M = 1
                        data.save()
                    case '$5,000,000 to $9,999,999':
                        data.More_5M_Less_10M = 1
                        data.save()
                    case '$5,000,000 to $9,999,999':
                        data.More_5M_Less_10M = 1
                        data.save()
                    case '$10,000,000 to $19,999,999':
                        data.More_10M_Less_20M = 1
                        data.save()
                    case 'More Than $20,000,000':
                        data.More_20M = 1
                        data.save()
                    
                    #Unsure option case is not included as it is not in front end options    


            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class EQuestions6APIView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        GET method to get user inputs
        """
        if request.user.groups.filter(name='Admins').exists():
            # Admins get all user details
            queryset = EQuestions6.objects.all()
            serializer = EQuestions6Serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Non-admin users get only their own data
        queryset = EQuestions6.objects.filter(user=request.user)
        if not queryset.exists():
            raise NotFound("There is No response for this user yet,post first!!!")
        
        serializer = EQuestions6Serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def create(self, request):
        """
        POST method to add user details
        """
        serializer = EQuestions6Serializer(data=request.data)

        if serializer.is_valid():
            try:
                a = EQuestions6.objects.get(user=self.request.user)
                return Response({"message":"Multiple Response, Please Delete the old response of user."},status=status.HTTP_409_CONFLICT)
            except:    
                serializer.save(user=self.request.user)
                try:
                    data,created = EQuestions6.objects.get_or_create(user=self.request.user)
                except Exception as e:
                    return Response({"message":"Multiple Response delete the old user data"},status = status.HTTP_409_CONFLICT)
                
                for option in serializer.validated_data.get('Selected_Options'):
                    if option == "Founder's Round":
                        data.Founders_Round = 1
                    elif option == 'Pre-Seed':
                        data.Pre_Seed = 1
                    elif option == 'Seed':
                        data.Seed = 1
                    elif option == 'Series "A"':
                        data.Series_A = 1
                    elif option == 'Series "B"':
                        data.Series_B = 1
                    elif option == 'Series "C"':
                        data.Series_C = 1
                    elif option == 'Pre-IPO':
                        data.Pre_Ipo = 1
                    elif option == 'IPO':
                        data.Ipo = 1
                    elif option == "Unsure Don't Know":
                        data.Unsure = 1

                match serializer.validated_data.get('Selected_Option'):
                    case 'One':
                        data.One = 1
               
                    case 'Two':
                        data.Two = 1

                    case 'TBD':
                        data.TBD = 1
                     

                # Save the updated data object
                data.save()



            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class EQuestions7APIView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        GET method to get user inputs
        """
        if request.user.groups.filter(name='Admins').exists():
            # Admins get all user details
            queryset = EQuestions7.objects.all()
            serializer = EQuestions7Serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Non-admin users get only their own data
        queryset = EQuestions7.objects.filter(user=request.user)
        if not queryset.exists():
            raise NotFound("There is No response for this user yet,post first!!!")
        
        serializer = EQuestions7Serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def create(self, request):
        """
        POST method to add user details
        """
        serializer = EQuestions7Serializer(data=request.data)

        if serializer.is_valid():
            try:
                a = EQuestions7.objects.get(user=self.request.user)
                return Response({"message":"Multiple Response, Please Delete the old response of user."},status=status.HTTP_409_CONFLICT)
            except:    
                serializer.save(user=self.request.user)
                try:
                    data,created = EQuestions7.objects.get_or_create(user=self.request.user)
                except Exception as e:
                    return Response({"message":"Multiple Response delete the old user data"},status = status.HTTP_409_CONFLICT)
                
                for option in serializer.validated_data.get('Selected_Options'):
                    if option == ('Startup - Working' or 'Startup-Working' or 'Startup -Working' or 'Startup- Working'):
                        data.Start_Up = 1
                    elif option == 'Growth Scalability':
                        data.Growth_Scalabitlity = 1
                    elif option == 'Marketing & Sales':
                        data.Marketing_and_Sales = 1
                    elif option == 'Cash Flow Capital':
                        data.Cash_FLow_Capital = 1
                    elif option == 'Human Capital':
                        data.Human_Capital = 1
                    elif option == 'Equipment':
                        data.Equipment = 1
                    elif option == 'Mergers & Acquisitions':
                        data.Merger_and_Acquistions = 1
                    elif option == 'Inventory':
                        data.Inventory = 1
                    elif option == 'Real Estate':
                        data.Real_State = 1
                    elif option == 'Other':
                        data.Other = 1
                    elif option == "Unsure/Don't Know":
                        data.Unsure = 1
                # Save the updated data object
                data.save()


            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EQuestions8APIView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        GET method to get user inputs
        """
        if request.user.groups.filter(name='Admins').exists():
            # Admins get all user details
            queryset = EQuestions8.objects.all()
            serializer = EQuestions8Serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Non-admin users get only their own data
        queryset = EQuestions8.objects.filter(user=request.user)
        if not queryset.exists():
            raise NotFound("There is No response for this user yet,post first!!!")
        
        serializer = EQuestions8Serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def create(self, request):
        """
        POST method to add user details
        """
        serializer = EQuestions8Serializer(data=request.data)

        if serializer.is_valid():
            try:
                a = EQuestions8.objects.get(user=self.request.user)
                return Response({"message":"Multiple Response, Please Delete the old response of user."},status=status.HTTP_409_CONFLICT)
            except:    
                serializer.save(user=self.request.user)
                try:
                    data,created = EQuestions8.objects.get_or_create(user=self.request.user)
                except Exception as e:
                    return Response({"message":"Multiple Response delete the old user data"},status = status.HTTP_409_CONFLICT)
                
                match serializer.validated_data.get('Selected_Option'):
                    case 'Low Risk Tolerance (Very Low Risk tolerance, expect to at least recoup principle)':
                        data.Low_Risk_Tolerance = 1
                                       
                    case 'Medium Risk Tolerance (Can lose some or most of the funding)':
                        data.Medium_Risk_Tolerance = 1

                    case 'High Risk Tolerance (Can lose most or all of the funding)':
                        data.High_Risk_Tolerance = 1

                
                match serializer.validated_data.get('Selected_Option2'):
                    case 'Low Cost of Capital (1-4%)':
                        data.Low_Cost_Capital = 1
                    case 'Medium Cost of Capital (5-10%)':
                        data.Medium_Cost_Capital = 1
                    case 'High Cost of Capital (11-18%)':
                        data.High_Cost_Capital = 1
                    case 'Very High Cost of Capital (19%+)':
                        data.Very_High_Cost_Capital = 1
                    case 'As long as the enterprise receives the net amount it needs, the cost is immaterial':
                        data.Immaterial_Cost_Capital = 1     

                data.save()                                

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class DocumentsPreparedAPIView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        GET method to get user inputs
        """
        if request.user.groups.filter(name='Admins').exists():
            # Admins get all user details
            queryset = DocumentsPrepared.objects.all()
            serializer = DocumentsPreparedSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Non-admin users get only their own data
        queryset = DocumentsPrepared.objects.filter(user=request.user)
        if not queryset.exists():
            raise NotFound("There is No response for this user yet,post first!!!")
        
        serializer = DocumentsPreparedSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def create(self, request):
        """
        POST method to add user details
        """
        serializer = DocumentsPreparedSerializer(data=request.data)

        if serializer.is_valid():
            try:
                a = DocumentsPrepared.objects.get(user=self.request.user)
                return Response({"message":"Multiple Response, Please Delete the old response of user."},status=status.HTTP_409_CONFLICT)
            except:    
                serializer.save(user=self.request.user)
                try:
                    data,created = DocumentsPrepared.objects.get_or_create(user=self.request.user)
                except Exception as e:
                    return Response({"message":"Multiple Response delete the old user data"},status = status.HTTP_409_CONFLICT)
                
                match serializer.validated_data.get('summary_of_offering'):
                    case 'Yes':
                        data.summary_of_offering = True

                    case 'No':
                        data.summary_of_offering = False

                match serializer.validated_data.get('financial_forecast'):        
                    case 'Yes':
                        data.financial_forecast = True

                    case 'No':
                        data.financial_forecast = False

                match serializer.validated_data.get('lean_business_model'):
                    case 'Yes':
                        data.lean_business_model = True
                    case 'No':
                        data.lean_business_model =False        

                match serializer.validated_data.get('presentation_deck'):
                    case 'Yes':
                        data.presentation_deck = True
                    case 'No':
                        data.presentation_deck = False

                match serializer.validated_data.get('leadership_overview'):
                    case 'Yes':
                        data.leadership_overview = True
                    case 'No':
                        data.leadership_overview = False

                match serializer.validated_data.get('exit_strategy'):
                    case 'Yes':
                        data.exit_strategy = True
                    case 'No':
                        data.exit_strategy = False

                match serializer.validated_data.get('offering_documents'):
                    case 'Yes':
                        data.offering_documents = True
                    case 'No':
                        data.offering_documents = False 

                match serializer.validated_data.get('ai_generated_deep_dive'):
                    case 'Yes':
                        data.ai_generated_deep_dive = True
                    case 'No':
                        data.ai_generated_deep_dive = False 

                match serializer.validated_data.get('virtual_data_room'):
                    case 'Yes':
                        data.virtual_data_room = True
                    case 'No':
                        data.virtual_data_room = False

                data.save()                                

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class EQuestions9APIView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        GET method to get user inputs
        """
        if request.user.groups.filter(name='Admins').exists():
            # Admins get all user details
            queryset = EQuestions9.objects.all()
            serializer = EQuestions9Serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Non-admin users get only their own data
        queryset = EQuestions9.objects.filter(user=request.user)
        if not queryset.exists():
            raise NotFound("There is No response for this user yet,post first!!!")
        
        serializer = EQuestions9Serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def create(self, request):
        """
        POST method to add user details
        """
        serializer = EQuestions9Serializer(data=request.data)

        if serializer.is_valid():
            try:
                a = EQuestions9.objects.get(user=self.request.user)
                return Response({"message":"Multiple Response, Please Delete the old response of user."},status=status.HTTP_409_CONFLICT)
            except:    
                serializer.save(user=self.request.user)            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EQuestions10APIView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        GET method to get user inputs
        """
        if request.user.groups.filter(name='Admins').exists():
            # Admins get all user details
            queryset = EQuestions10.objects.all()
            serializer = EQuestions10Serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Non-admin users get only their own data
        queryset = EQuestions10.objects.filter(user=request.user)
        if not queryset.exists():
            raise NotFound("There is No response for this user yet,post first!!!")
        
        serializer = EQuestions10Serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def create(self, request):
        """
        POST method to add user details
        """
        serializer = EQuestions10Serializer(data=request.data)

        if serializer.is_valid():
            try:
                a = EQuestions10.objects.get(user=self.request.user)
                return Response({"message":"Multiple Response, Please Delete the old response of user."},status=status.HTTP_409_CONFLICT)
            except:    
                serializer.save(user=self.request.user)              
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EQuestions11APIView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        GET method to get user inputs
        """
        if request.user.groups.filter(name='Admins').exists():
            # Admins get all user details
            queryset = EQuestions11.objects.all()
            serializer = EQuestions11Serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Non-admin users get only their own data
        queryset = EQuestions11.objects.filter(user=request.user)
        if not queryset.exists():
            raise NotFound("There is No response for this user yet,post first!!!")
        
        serializer = EQuestions11Serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def create(self, request):
        """
        POST method to add user details
        """
        serializer = EQuestions11Serializer(data=request.data)

        if serializer.is_valid():
            try:
                a = EQuestions11.objects.get(user=self.request.user)
                return Response({"message":"Multiple Response, Please Delete the old response of user."},status=status.HTTP_409_CONFLICT)
            except:    
                serializer.save(user=self.request.user)              
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EQuestions12APIView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        GET method to get user inputs
        """
        if request.user.groups.filter(name='Admins').exists():
            # Admins get all user details
            queryset = EQuestions12.objects.all()
            serializer = EQuestions12Serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Non-admin users get only their own data
        queryset = EQuestions12.objects.filter(user=request.user)
        if not queryset.exists():
            raise NotFound("There is No response for this user yet,post first!!!")
        
        serializer = EQuestions12Serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def create(self, request):
        """
        POST method to add user details
        """
        serializer = EQuestions12Serializer(data=request.data)

        if serializer.is_valid():
            try:
                a = EQuestions12.objects.get(user=self.request.user)
                return Response({"message":"Multiple Response, Please Delete the old response of user."},status=status.HTTP_409_CONFLICT)
            except:    
                serializer.save(user=self.request.user)              
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class EQuestions13APIView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        GET method to get user inputs
        """
        if request.user.groups.filter(name='Admins').exists():
            # Admins get all user details
            queryset = EQuestions13.objects.all()
            serializer = EQuestions13Serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Non-admin users get only their own data
        queryset = EQuestions13.objects.filter(user=request.user)
        if not queryset.exists():
            raise NotFound("There is No response for this user yet,post first!!!")
        
        serializer = EQuestions13Serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def create(self, request):
        """
        POST method to add user details
        """
        serializer = EQuestions13Serializer(data=request.data)

        if serializer.is_valid():
            try:
                a = EQuestions13.objects.get(user=self.request.user)
                return Response({"message":"Multiple Response, Please Delete the old response of user."},status=status.HTTP_409_CONFLICT)
            except:    
                serializer.save(user=self.request.user)              
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EQuestions14APIView(viewsets.ViewSet):
    def list(self, request):
        """
        GET method to get user inputs
        """
        if request.user.groups.filter(name='Admins').exists():
            # Admins get all user details
            queryset = EQuestions14.objects.all()
            serializer = EQuestions14Serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Non-admin users get only their own data
        queryset = EQuestions14.objects.filter(user=request.user)
        if not queryset.exists():
            raise NotFound("There is No response for this user yet,post first!!!")        
        serializer = EQuestions14Serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def create(self, request):
        """
        POST method to add user details
        """
        serializer = EQuestions14Serializer(data=request.data)

        if serializer.is_valid():
            try:
                a = EQuestions14.objects.get(user=self.request.user)
                return Response({"message":"Multiple Response, Please Delete the old response of user."},status=status.HTTP_409_CONFLICT)
            except:    
                serializer.save(user=self.request.user)            
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IQuestions1APIView(generics.CreateAPIView):   
    #permission_classes = [IsAuthenticated]
    queryset = IQuestions1.objects.all()
    serializer_class = IQuestions1Serializer    

    #def post(self, request):
    #    try:
    #        # Check if an IQuestions1 record already exists for the logged-in user
    #        iquestions1 = IQuestions1.objects.get(user=request.user)
    #        # If the record exists, update it
    #        serializer = IQuestions1Serializer(iquestions1, data=request.data)
    #    except IQuestions1.DoesNotExist:
    #        # If no record exists, create a new one
    #        serializer = IQuestions1Serializer(data=request.data)

    #    if serializer.is_valid():
    #        serializer.save(user=request.user)
    #        return Response(serializer.data, status=status.HTTP_200_OK)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IQuestions2APIView(generics.CreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = IQuestions2.objects.all()
    serializer_class = IQuestions2Serializer
    
    #def post(self, request):
    #    try:
    #        # Check if an IQuestions2 record already exists for the logged-in user
    #        iquestions2 = IQuestions2.objects.get(user=request.user)
    #        # If the record exists, update it
    #        serializer = IQuestions2Serializer(iquestions2, data=request.data)
    #    except IQuestions2.DoesNotExist:
            # If no record exists, create a new one
    #        serializer = IQuestions2Serializer(data=request.data)

    #    if serializer.is_valid():
    #        serializer.save(user=request.user)
    #        return Response(serializer.data, status=status.HTTP_200_OK)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VQuestion1APIView(generics.CreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = VQuestion1.objects.all()
    serializer_class = VQuestion1Serializer    

    #def post(self, request):
    #    try:
    #        # Check if a VQuestion1 record already exists for the logged-in user
    #        vquestion1 = VQuestion1.objects.get(user=request.user)
    #        # If the record exists, update it
    #        serializer = VQuestion1Serializer(vquestion1, data=request.data)
    #    except VQuestion1.DoesNotExist:
    #        # If no record exists, create a new one
    #        serializer = VQuestion1Serializer(data=request.data)

    #    if serializer.is_valid():
    #        serializer.save(user=request.user)
    #        return Response(serializer.data, status=status.HTTP_200_OK)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #def get(self, request):
    #    try:
    #        # Retrieve the VQuestion1 record for the logged-in user
    #        vquestion1 = VQuestion1.objects.get(user=request.user)
    #        serializer = VQuestion1Serializer(vquestion1)
    #        return Response(serializer.data, status=status.HTTP_200_OK)
    #    except VQuestion1.DoesNotExist:
    #        return Response({"detail": "Record not found."}, status=status.HTTP_404_NOT_FOUND)   

#class MatchDataDetailView(generics.RetrieveAPIView):
#    queryset = Match_Data.objects.all()
#    serializer_class = MatchDataSerializer
#    lookup_field = 'user_id'              
        
class MatchDataRetrieveEfficientListView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
   
    def list(self, request):
        """
        GET method to get user inputs
        """
        Match(request)
        if request.user.groups.filter(name='Admins').exists():
            # Admins get all user details
            queryset = Letter_Response.objects.all()
            serializer = MatchDataEfficientSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # Non-admin users get only their own data
        queryset = Letter_Response.objects.filter(user=request.user)
        if not queryset.exists():
            raise NotFound("There is No response for this user yet,trigger match based on all other inputs first!!!")
        serializer = MatchDataEfficientSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MatchDataRetrieveEfficientListViewPdf(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
   
    def get(self, request):
        """
        GET method to get user inputs
        """
        return pdf(request)

class referalResponseAPIView(viewsets.ViewSet):
    def list(self, request):
        """
        GET method to get user inputs
        """
        if request.user.groups.filter(name='Admins').exists():
            # Admins get all user details
            queryset = ReferalResponse.objects.all()
            serializer = referalResponseSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Non-admin users get only their own data
        queryset = ReferalResponse.objects.filter(user=request.user)
        if not queryset.exists():
            raise NotFound("There is No response for this user yet,post first!!!")
        
        serializer = referalResponseSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def create(self, request):
        """
        POST method to add user details
        """
        serializer = referalResponseSerializer(data=request.data)

        if serializer.is_valid():
            try:
                a = ReferalResponse.objects.get(user=self.request.user)
                return Response({"message":"Multiple Response, Please Delete the old response of user."},status=status.HTTP_409_CONFLICT)
            except:    
                serializer.save(user=self.request.user)            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class preRatingAPIView(viewsets.ViewSet):
    def list(self, request):
        """
        GET method to get user inputs
        """
        if request.user.groups.filter(name='Admins').exists():
            # Admins get all user details
            queryset = PreRating.objects.all()
            serializer = preRatingSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Non-admin users get only their own data
        queryset = PreRating.objects.filter(user=request.user)
        if not queryset.exists():
            raise NotFound("There is No response for this user yet,post first!!!")

        serializer = preRatingSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        """
        POST method to add or merge user pre-rating data.
        If a PreRating record already exists for this user, the incoming
        preratings JSON is merged into the existing data (update).
        """
        serializer = preRatingSerializer(data=request.data)

        if serializer.is_valid():
            try:
                existing = PreRating.objects.get(user=self.request.user)
                # Merge new preratings into existing JSON data
                new_data = serializer.validated_data.get('preratings', {})
                if isinstance(existing.preratings, dict):
                    existing.preratings.update(new_data)
                else:
                    existing.preratings = new_data
                existing.save()
                return Response(preRatingSerializer(existing).data, status=status.HTTP_200_OK)
            except PreRating.DoesNotExist:
                serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class payLoadView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        GET method to get user inputs
        """
        if request.user.groups.filter(Q(name='Admins') | Q(name='Third_Party_Applications')).exists():
            # Admins get all user details
            queryset = pay_load_string.objects.all()
            serializer = payLoadSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # Non-admin users get only their own data
        queryset = pay_load_string.objects.filter(user=request.user)
        if not queryset.exists():
            raise NotFound("There is No response for this user yet,post first!!!")
        
        serializer = payLoadSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def create(self, request):
        """
        POST method to add user details
        """
        serializer = payLoadSerializer(data=request.data)

        if serializer.is_valid():
            try:
                a = pay_load_string.objects.get(user=self.request.user)
                return Response({"message":"Multiple Response, Please Delete the old response of user."},status=status.HTTP_409_CONFLICT)
            except:    
                serializer.save(user=self.request.user)
                try:
                    data,created = pay_load_string.objects.get_or_create(user=self.request.user)
                    data.save()
                except Exception as e:
                    return Response({"message":"Multiple Response delete the old user data"},status = status.HTTP_409_CONFLICT)
                try:
                    payLoadString = serializer.data.get("payLoadString", {})
                    email = payLoadString.get("email")
                    fundsUse = payLoadString.get("fundsUse")
                    entityName = payLoadString.get("entityName")
                    entityType = payLoadString.get("entityType")
                    mobilePhone = payLoadString.get("mobilePhone")
                    display_name = payLoadString.get("display_name")
                    plannedRaise = payLoadString.get("plannedRaise")
                    businessPhone = payLoadString.get("businessPhone")
                    currentRounds = payLoadString.get("currentRounds")
                    howManyRounds = payLoadString.get("howManyRounds")
                    primaryAppUse = payLoadString.get("primaryAppUse")
                    companyWebsite = payLoadString.get("companyWebsite")
                    stageofCompany = payLoadString.get("stageofCompany")
                    preCapitalRaise = payLoadString.get("preCapitalRaise")
                    specialPrograms = payLoadString.get("specialPrograms")
                    capitalPreMarkets = payLoadString.get("capitalPreMarkets")
                    companyAffiliation = payLoadString.get("companyAffiliation")
                    riskToleranceFounder = payLoadString.get("riskToleranceFounder")
                    riskToleranceInvestor = payLoadString.get("riskToleranceInvestor")
                    primaryBusinessAddress = payLoadString.get("primaryBusinessAddress")
                    entityStateofRegistration = payLoadString.get("entityStateofRegistration")
                    rangeofCost = payLoadString.get("rangeofCost")
                    timming = payLoadString.get("timing")
                    summaryofOffering = payLoadString.get("summaryofOffering")
                    financialForecast = payLoadString.get("financialForecast")
                    leanBusinessModelCanvas = payLoadString.get("leanBusinessModelCanvas")
                    presentationDeck = payLoadString.get("presentationDeck")
                    leadershipOverview = payLoadString.get("leadershipOverview")
                    exitStrategy = payLoadString.get("exitStrategy")
                    offeringDocuments = payLoadString.get("offeringDocuments")
                    aiGeneratedDeepDive = payLoadString.get("aiGeneratedDeepDive")
                    virtualDataroom = payLoadString.get("virtualDataroom")


                    
                    apiUser = UserDetail(user=request.user)
                    apiPrimaryPurpose = UserDetail2(user=request.user)
                    apiStage = EQuestions1(user=request.user)
                    apiEntity = EQuestions2(user=request.user)
                    apiPreCapitalRaise = EQuestions3(user=request.user)
                    apiCapitalPreMarket = EQuestions4(user=request.user)
                    apiPlannedraise = EQuestions5(user=request.user)
                    apiRoundsofCapital = EQuestions6(user=request.user)
                    apiUseofFunds = EQuestions7(user=request.user)
                    apiRiskCost = EQuestions8(user=request.user)
                    apiUpfrontCostandTime = EQuestions(user=request.user)
                    apiDocumentsPrepared = DocumentsPrepared(user=request.user) 


                    apiUser.user = request.user
                    apiUser.First_Name=display_name
                    apiUser.Middle_Name=""
                    apiUser.Last_Name=""
                    apiUser.Affiliation=companyAffiliation
                    apiUser.User_Email= email
                    apiUser.Company_Website= companyWebsite
                    apiUser.Business_Adress=primaryBusinessAddress
                    apiUser.Business_Phone=businessPhone
                    apiUser.Mobile_Phone=mobilePhone
                    apiUser.Special_Programs=specialPrograms 
                    apiUser.save()
                    apiPrimaryPurpose.user = request.user
                    apiPrimaryPurpose.Primary_Purpose = primaryAppUse
                    apiPrimaryPurpose.save()
                    #apiStagestart
                    apiStageOption = stageofCompany
                    # Create a dictionary to hold the values
                    stageoption_values = {
                        'Idea': 0,
                        'Formation': 0,
                        'Start Up': 0,
                        'Growth': 0,
                        'M & A': 0,
                        'Preparing for Public': 0,
                        'Distressed': 0,
                    }
                    # Set the selected option to 1
                    stageoption_values[apiStageOption] = 1
                    # Create the UserDetail instance with the correct values
                    apiStage.user = request.user
                    apiStage.Idea=stageoption_values['Idea']
                    apiStage.Formation=stageoption_values['Formation']
                    apiStage.Start_Up=stageoption_values['Start Up']
                    apiStage.Growth=stageoption_values['Growth']
                    apiStage.M_And_A=stageoption_values['M & A']
                    apiStage.Preparing_For_Public = stageoption_values['Preparing for Public']
                    apiStage.Distressed = stageoption_values['Distressed']
                    apiStage.Selected_Option = apiStageOption
                    apiStage.save()
                    
                    #Api entity start
                    apiEntityOption = entityType
                    # Create a dictionary to hold the values
                    entityoption_values = {
                        'None (To be Determined)': 0,
                        'Sole Proprietorship': 0,
                        'LLC': 0,
                        'LP': 0,
                        'GP': 0,
                        'S Corporation': 0,
                        'C Corp': 0,
                        'Other':0,
                    }
                    # Set the selected option to 1
                    entityoption_values[apiEntityOption] = 1
                    # Create the entity instance with the correct values
                    apiEntity.user = request.user
                    apiEntity.Selected_Option = apiEntityOption # this is to retrieve data
                    apiEntity.Business_Name = entityName
                    apiEntity.Registration_Region = entityStateofRegistration
                    apiEntity.No_Business=entityoption_values['None (To be Determined)']
                    apiEntity.Sole_Proprietorship=entityoption_values['Sole Proprietorship']
                    apiEntity.LLC=entityoption_values['LLC']
                    apiEntity.LP=entityoption_values['LP']
                    apiEntity.GP=entityoption_values['GP']
                    apiEntity.S_Corporation = entityoption_values['S Corporation']
                    apiEntity.C_Corp = entityoption_values['C Corp']
                    apiEntity.Other = entityoption_values['Other']
                    apiEntity.save()
                    
                    #API pre capital raise start
                    precapitalselected_option = preCapitalRaise
                    # Create a dictionary to hold the values
                    precapitalraiseoption_values = {
                        'Less than $25,000': 0,
                        '$26,000 to $100,000': 0,
                        '$101,000 to $250,000': 0,
                        '$251,000 to $500,000': 0,
                        '$501,000 to $1,000,000': 0,
                        '$1,000,001 to $2,000,000': 0,
                        '$2,000,001 to $5,000,000': 0,
                        '$5,000,001 to $10,000,000': 0,
                        'More than $10,000,000': 0,
                    }
                    # Set the selected option to 1
                    precapitalraiseoption_values[precapitalselected_option] = 1
                    # Create the UserDetail instance with the correct values
                    apiPreCapitalRaise.user = request.user
                    apiPreCapitalRaise.Selected_Option = precapitalselected_option
                    apiPreCapitalRaise.Less_25k = precapitalraiseoption_values['Less than $25,000']
                    apiPreCapitalRaise.More_25K_Less_100k = precapitalraiseoption_values['$26,000 to $100,000']
                    apiPreCapitalRaise.More_100k_Less_250K = precapitalraiseoption_values['$101,000 to $250,000']
                    apiPreCapitalRaise.More_250k_Less_500K = precapitalraiseoption_values['$251,000 to $500,000']
                    apiPreCapitalRaise.More_500K_Less_1M = precapitalraiseoption_values['$501,000 to $1,000,000']
                    apiPreCapitalRaise.More_1M_Less_2M = precapitalraiseoption_values['$1,000,001 to $2,000,000']
                    apiPreCapitalRaise.More_2M_Less_5M = precapitalraiseoption_values['$2,000,001 to $5,000,000']
                    apiPreCapitalRaise.More_5M_Less_10M = precapitalraiseoption_values['$5,000,001 to $10,000,000']
                    apiPreCapitalRaise.More_10M = precapitalraiseoption_values['More than $10,000,000']
                    apiPreCapitalRaise.save()

                    #pre market capital type start
                    capitalpremarketselected_options_list = capitalPreMarkets
                    # Create a dictionary to hold the values
                    capitalpremarketoption_values = {
                        'Accelerator': 0,
                        'Bonds': 0,
                        'Commercial Banks': 0,
                        'Cryptocurrency': 0,
                        'EB5 Immigration': 0,
                        'Enterprise Zones': 0,
                        'Factoring': 0,
                        'Grants': 0,
                        'Hedge Funds': 0,
                        'Incubator': 0,
                        'Investment Banking': 0,
                        'Other (Owner Equity)': 0,
                        'Private Debt (Officer Loans to Startup)': 0,
                        'Private Equity Securities': 0,
                        'Public Offering': 0,
                        'Real State': 0,
                        'Royalty Financing': 0,
                        'Small Business Administration (SBA)': 0,
                        'Venture Capital': 0,
                        'Unsure/Do not Know': 0
                    }
                    for cm in capitalpremarketselected_options_list:
                        capitalpremarketoption_values[cm] =1
                    # Create the UserDetail instance with the correct values
                    apiCapitalPreMarket.user = request.user
                    apiCapitalPreMarket.Selected_Options = capitalpremarketselected_options_list
                    apiCapitalPreMarket.Accelerator = capitalpremarketoption_values['Accelerator']
                    apiCapitalPreMarket.Bonds = capitalpremarketoption_values['Bonds']
                    apiCapitalPreMarket.Comercial_Banking = capitalpremarketoption_values['Commercial Banks']
                    apiCapitalPreMarket.Cryptocurrency = capitalpremarketoption_values['Cryptocurrency']
                    apiCapitalPreMarket.EB5_Immigration = capitalpremarketoption_values['EB5 Immigration']
                    apiCapitalPreMarket.Enterprise_Zones = capitalpremarketoption_values['Enterprise Zones']
                    apiCapitalPreMarket.Factoring = capitalpremarketoption_values['Factoring']
                    apiCapitalPreMarket.Grants = capitalpremarketoption_values['Grants']
                    apiCapitalPreMarket.Hedge_Funds = capitalpremarketoption_values['Hedge Funds']
                    apiCapitalPreMarket.Incubator = capitalpremarketoption_values['Incubator']
                    apiCapitalPreMarket.Investment_Banking = capitalpremarketoption_values['Investment Banking']
                    apiCapitalPreMarket.Other_Owner_Equity =capitalpremarketoption_values['Other (Owner Equity)']
                    apiCapitalPreMarket.Private_Debt = capitalpremarketoption_values['Private Debt (Officer Loans to Startup)']
                    apiCapitalPreMarket.Private_Equity = capitalpremarketoption_values['Private Equity Securities']
                    apiCapitalPreMarket.Public_Offereing =capitalpremarketoption_values['Public Offering']
                    apiCapitalPreMarket.Real_Estate = capitalpremarketoption_values['Real State']
                    apiCapitalPreMarket.Royalty_Financing = capitalpremarketoption_values['Royalty Financing']
                    apiCapitalPreMarket.Small_Business_Administration = capitalpremarketoption_values['Small Business Administration (SBA)']
                    apiCapitalPreMarket.Venture_Capital = capitalpremarketoption_values['Venture Capital']
                    apiCapitalPreMarket.Unsure = capitalpremarketoption_values['Unsure/Do not Know']
                    apiCapitalPreMarket.save()
                    #Ammount of planned raise
                    plannedraiseselected_option = plannedRaise
                    # Create a dictionary to hold the values
                    plannedraiseoption_values = {
                        'Less than $25,000': 0,
                        '$25,000 to $100,000': 0,
                        '$100,000 to $249,999': 0,
                        '$250,000 to $499,999': 0,
                        '$500,000 to $999,999': 0,
                        '$1,000,000 to $1,349,999': 0,
                        '$1,350,000 to $1,999,999': 0,
                        '$2,000,000 to $4,999,999': 0,
                        '$5,000,000 to $9,999,999': 0,
                        '$10,000,000 to $19,999,999': 0,
                        'More Than $20 Million': 0,
                        'Unsure/Do not Know/TBD': 0,
                    }
                    # Set the selected option to 1
                    plannedraiseoption_values[plannedRaise] = 1
                    # Create the UserDetail instance with the correct values
                    apiPlannedraise.user = request.user
                    apiPlannedraise.Selected_Option = plannedraiseselected_option
                    apiPlannedraise.Less_25k = plannedraiseoption_values['Less than $25,000']
                    apiPlannedraise.More_25K_Less_100k = plannedraiseoption_values['$25,000 to $100,000']
                    apiPlannedraise.More_100k_Less_250K = plannedraiseoption_values['$100,000 to $249,999']
                    apiPlannedraise.More_250k_Less_500K = plannedraiseoption_values['$250,000 to $499,999']
                    apiPlannedraise.More_500K_Less_1M = plannedraiseoption_values['$500,000 to $999,999']
                    apiPlannedraise.More_1M_Less_1_35M = plannedraiseoption_values['$1,000,000 to $1,349,999']
                    apiPlannedraise.More_1_35M_Less_2M = plannedraiseoption_values['$1,350,000 to $1,999,999']
                    apiPlannedraise.More_2M_Less_5M = plannedraiseoption_values['$2,000,000 to $4,999,999']
                    apiPlannedraise.More_5M_Less_10M = plannedraiseoption_values['$5,000,000 to $9,999,999']
                    apiPlannedraise.More_10M_Less_20M = plannedraiseoption_values['$10,000,000 to $19,999,999']
                    apiPlannedraise.More_20M = plannedraiseoption_values['More Than $20 Million']
                    apiPlannedraise.Unsure = plannedraiseoption_values['Unsure/Do not Know/TBD']
                    apiPlannedraise.save()
                    
                    #rounds of capital start
                    roundsselected_options_list = currentRounds
                    roundsselected_option_2 = howManyRounds

                    # Create a dictionary to hold the values for first question in form
                    roundsoption_values = {
                        'Founders Round': 0,
                        'Pre Seed': 0,
                        'Seed': 0,
                        'Series A': 0,
                        'Series B': 0,
                        'Series C': 0,
                        'Pre Ipo': 0,
                        'Ipo': 0,
                        'Unsure': 0,
                    }
                    #Set the seleceted options to 1
                    for round in roundsselected_options_list:
                        roundsoption_values[round] =1
                    
                    # Create a dictionary to hold the values for first question in form
                    roundoption_values2 = {
                        'One': 0,
                        'Two': 0,
                        'TBD': 0,
                    }
                    # Set the selected option to 1 for the second question of form
                    roundoption_values2[roundsselected_option_2] = 1

                    # Create the UserDetail instance with the correct values
                    apiRoundsofCapital.user = request.user
                    apiRoundsofCapital.Selected_Options = roundsselected_options_list
                    apiRoundsofCapital.Selected_Option =roundsselected_option_2
                    apiRoundsofCapital.Founders_Round = roundsoption_values['Founders Round']
                    apiRoundsofCapital.Pre_Seed = roundsoption_values['Pre Seed']
                    apiRoundsofCapital.Seed = roundsoption_values['Seed']
                    apiRoundsofCapital.Series_A = roundsoption_values['Series A']
                    apiRoundsofCapital.Series_B = roundsoption_values['Series B']
                    apiRoundsofCapital.Series_C = roundsoption_values['Series C']
                    apiRoundsofCapital.Pre_Ipo = roundsoption_values['Pre Ipo']
                    apiRoundsofCapital.Ipo = roundsoption_values['Ipo']
                    apiRoundsofCapital.Unsure = roundsoption_values['Unsure']

                    # for second question option_values2
                    apiRoundsofCapital.One = roundoption_values2['One']
                    apiRoundsofCapital.Two = roundoption_values2['Two']
                    apiRoundsofCapital.TBD = roundoption_values2['TBD']
                    apiRoundsofCapital.save()

                    #start of use of funds api
                    useoffundselected_options_list = fundsUse

                    # Create a dictionary to hold the values
                    useoffundsoption_values = {
                        'Startup/Working': 0,
                        'Growth Scalability': 0,
                        'Marketing & Sales': 0,
                        'Cash Flow Capital': 0,
                        'Human Capital': 0,
                        'Equipment': 0,
                        'Merger & Acquitions': 0,
                        'Inventory': 0,
                        'Real Estate': 0,
                        'Other': 0,
                        'Do not Know/Unsure/TBD': 0,
                    }
                    #Set the seleceted options to 1
                    for use in useoffundselected_options_list:
                        useoffundsoption_values[use] = 1

                    # Create the UserDetail instance with the correct values
                    apiUseofFunds.user = request.user
                    apiUseofFunds.Selected_Options =useoffundselected_options_list
                    apiUseofFunds.Start_Up = useoffundsoption_values['Startup/Working']
                    apiUseofFunds.Growth_Scalabitlity = useoffundsoption_values['Growth Scalability']
                    apiUseofFunds.Marketing_and_Sales = useoffundsoption_values['Marketing & Sales']
                    apiUseofFunds.Cash_FLow_Capital = useoffundsoption_values['Cash Flow Capital']
                    apiUseofFunds.Human_Capital = useoffundsoption_values['Human Capital']
                    apiUseofFunds.Equipment = useoffundsoption_values['Equipment']
                    apiUseofFunds.Merger_and_Acquistions = useoffundsoption_values['Merger & Acquitions']
                    apiUseofFunds.Inventory = useoffundsoption_values['Inventory']
                    apiUseofFunds.Real_State = useoffundsoption_values['Real Estate']
                    apiUseofFunds.Other = useoffundsoption_values['Other']
                    apiUseofFunds.Unsure = useoffundsoption_values['Do not Know/Unsure/TBD']
                    apiUseofFunds.save()

                    #risk assesment and capital cost api start
                    riskselected_option1 = riskToleranceInvestor
                    capitalcostselected_option2 = riskToleranceFounder

                    # Create a dictionary to hold the values for first Risk question
                    riskoption_values1 = {
                        'Very Low/Low Risk Tolerance (Expect to at least recoup principle)': 0,
                        'Medium Risk Tolerance (Can lose some or most of the funding)': 0,
                        'High Risk Tolerance (Can lose most or all of the funding)': 0,
                    }
                
                    riskoption_values1[riskselected_option1] =1
                    
                    # Create a dictionary to hold the values for second Risk question (Cost of capital)
                    capitalcostoption_values2 = {
                        'Low Cost of Capital (1-4%)': 0,
                        'Medium Cost of Capital (5-10%)': 0,
                        'High Cost of Capital (11-18%)': 0,
                        'Very High Cost of Capital (19%+)': 0,
                        'As long as the enterprise receives the net amount it needs, the cost is immaterial': 0,
                    }

                    capitalcostoption_values2[capitalcostselected_option2] =1

                    # Create the UserDetail instance with the correct values
                    apiRiskCost.user = request.user
                    apiRiskCost.Selected_Option = riskselected_option1
                    apiRiskCost.Selected_Option2 = capitalcostselected_option2
                    #Updating First Question's Column in Model 
                    apiRiskCost.Low_Risk_Tolerance = riskoption_values1['Very Low/Low Risk Tolerance (Expect to at least recoup principle)']
                    apiRiskCost.Medium_Risk_Tolerance = riskoption_values1['Medium Risk Tolerance (Can lose some or most of the funding)']
                    apiRiskCost.High_Risk_Tolerance = riskoption_values1['High Risk Tolerance (Can lose most or all of the funding)']
                    #Updating Second Question's Column in Model
                    apiRiskCost.Low_Cost_Capital = capitalcostoption_values2['Low Cost of Capital (1-4%)']
                    apiRiskCost.Medium_Cost_Capital = capitalcostoption_values2['Medium Cost of Capital (5-10%)']
                    apiRiskCost.High_Cost_Capital = capitalcostoption_values2['High Cost of Capital (11-18%)']
                    apiRiskCost.Very_High_Cost_Capital = capitalcostoption_values2['Very High Cost of Capital (19%+)']
                    apiRiskCost.Immaterial_Cost_Capital = capitalcostoption_values2['As long as the enterprise receives the net amount it needs, the cost is immaterial']
                    apiRiskCost.save()

                    #Start upfront cost api
                    upfcostselected_option = rangeofCost

                    # Create a dictionary to hold the values
                    upfcostoption_values = {
                        'Minimum $0 - Maximum $499': 0,
                        'Minimum $500 - Maximum $999': 0,
                        'Minimum $1000 - Maximum $2499': 0,
                        'Minimum $2500 - Maximum $4999': 0,
                        'Minimum $5000 - Maximum $9999': 0,
                        'Minimum $10000 - Maximum $24999': 0,
                        'Minimum $25000 - Maximum $49999': 0,
                        'More than $50000+':0,
                    }

                    # Set the selected option to 1
                    upfcostoption_values[upfcostselected_option] = 1

                    # Create the UserDetail instance with the correct values
                    apiUpfrontCostandTime.user = request.user
                    apiUpfrontCostandTime.Selected_Option = upfcostselected_option # this is to retrieve data
                    apiUpfrontCostandTime.RC_zero_to_499 = upfcostoption_values['Minimum $0 - Maximum $499']
                    apiUpfrontCostandTime.RC_500_to_999 = upfcostoption_values['Minimum $500 - Maximum $999']
                    apiUpfrontCostandTime.RC_1000_to_2499=upfcostoption_values['Minimum $1000 - Maximum $2499']
                    apiUpfrontCostandTime.RC_2500_to_4999=upfcostoption_values['Minimum $2500 - Maximum $4999']
                    apiUpfrontCostandTime.RC_5000_to_9999=upfcostoption_values['Minimum $5000 - Maximum $9999']
                    apiUpfrontCostandTime.RC_10000_to_24999=upfcostoption_values['Minimum $10000 - Maximum $24999']
                    apiUpfrontCostandTime.RC_25000_to_49999=upfcostoption_values['Minimum $25000 - Maximum $49999']
                    apiUpfrontCostandTime.RC_More_Than_50000 = upfcostoption_values['More than $50000+']

                    upftimeselected_option = timming
                    # Create a dictionary to hold the values
                    upftimeoption_values = {
                        '1 Day to 1 Week': 0,
                        '1 Week to 2 Weeks': 0,
                        '2 Weeks to 4 Weeks': 0,
                        '1 Month to 2 Months': 0,
                        '2 Months to 3 Months': 0,
                        '3 Months to 6 Months': 0,
                        '6 Months to 12 Months': 0,
                        'More than 1 year':0,
                    }

                    # Set the selected option to 1
                    upftimeoption_values[upftimeselected_option] = 1

                    # Create the UserDetail instance with the correct values
                    apiUpfrontCostandTime.Selected_Option2 = upftimeselected_option # this is to retrieve data
                    apiUpfrontCostandTime.RT_1D_to_1W = upftimeoption_values['1 Day to 1 Week']
                    apiUpfrontCostandTime.RT_1W_to_2W = upftimeoption_values['1 Week to 2 Weeks']
                    apiUpfrontCostandTime.RT_2W_to_4W=upftimeoption_values['2 Weeks to 4 Weeks']
                    apiUpfrontCostandTime.RT_1M_to_2M=upftimeoption_values['1 Month to 2 Months']
                    apiUpfrontCostandTime.RT_2M_to_3M=upftimeoption_values['2 Months to 3 Months']
                    apiUpfrontCostandTime.RT_3M_to_6M=upftimeoption_values['3 Months to 6 Months']
                    apiUpfrontCostandTime.RT_6M_to_12M=upftimeoption_values['6 Months to 12 Months']
                    apiUpfrontCostandTime.RT_More_Than_a_Year = upftimeoption_values['More than 1 year']
                    apiUpfrontCostandTime.save()

                    #Documents prepared API:
                    summary_of_offering = summaryofOffering
                    financial_forecast = financialForecast
                    lean_business_model_canvas = leanBusinessModelCanvas
                    presentation_deck = presentationDeck
                    leadership_overview = leadershipOverview
                    exit_strategy = exitStrategy
                    offering_documents = offeringDocuments
                    ai_generated_deep_dive = aiGeneratedDeepDive
                    virtual_data_room = virtualDataroom

                    apiDocumentsPrepared.user = request.user
                    match summary_of_offering:
                        case 'Yes':
                            apiDocumentsPrepared.summary_of_offering = True

                        case 'No':
                            apiDocumentsPrepared.summary_of_offering = False

                    match financial_forecast:        
                        case 'Yes':
                            apiDocumentsPrepared.financial_forecast = True

                        case 'No':
                            apiDocumentsPrepared.financial_forecast = False

                    match lean_business_model_canvas:
                        case 'Yes':
                            apiDocumentsPrepared.lean_business_model = True
                        case 'No':
                            apiDocumentsPrepared.lean_business_model =False        

                    match presentation_deck:
                        case 'Yes':
                            apiDocumentsPrepared.presentation_deck = True
                        case 'No':
                            apiDocumentsPrepared.presentation_deck = False

                    match leadership_overview:
                        case 'Yes':
                            apiDocumentsPrepared.leadership_overview = True
                        case 'No':
                            apiDocumentsPrepared.leadership_overview = False

                    match exit_strategy:
                        case 'Yes':
                            apiDocumentsPrepared.exit_strategy = True
                        case 'No':
                            apiDocumentsPrepared.exit_strategy = False

                    match offering_documents:
                        case 'Yes':
                            apiDocumentsPrepared.offering_documents = True
                        case 'No':
                            apiDocumentsPrepared.offering_documents = False 

                    match ai_generated_deep_dive:
                        case 'Yes':
                            apiDocumentsPrepared.ai_generated_deep_dive = True
                        case 'No':
                            apiDocumentsPrepared.ai_generated_deep_dive = False 

                    match virtual_data_room:
                        case 'Yes':
                            apiDocumentsPrepared.virtual_data_room = True
                        case 'No':
                            apiDocumentsPrepared.virtual_data_room = False
                    apiDocumentsPrepared.save()         
                except:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)                             

                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LendingRequirementsAPIView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        """
        GET method to get lending requirements
        """
        if request.user.groups.filter(name='Admins').exists():
            queryset = LendingRequirements.objects.all()
            serializer = LendingRequirementsSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        queryset = LendingRequirements.objects.filter(user=request.user)
        if not queryset.exists():
            raise NotFound("There is No response for this user yet, post first!!!")
        serializer = LendingRequirementsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """
        POST method to add lending requirements
        """
        serializer = LendingRequirementsSerializer(data=request.data)

        if serializer.is_valid():
            try:
                LendingRequirements.objects.get(user=self.request.user)
                return Response(
                    {"message": "Multiple Response, Please Delete the old response of user."},
                    status=status.HTTP_409_CONFLICT,
                )
            except LendingRequirements.DoesNotExist:
                serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

