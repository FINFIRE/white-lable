from django.urls import path,include
from django.contrib import admin
from rest_framework import routers
from .views import UserDetailAPIView,UserDetail2APIView,EQuestionsAPIView,EQuestions1APIView,EQuestions2APIView,\
EQuestions3APIView,EQuestions4APIView,EQuestions5APIView,EQuestions6APIView,EQuestions7APIView,\
EQuestions8APIView,DocumentsPreparedAPIView,EQuestions9APIView,EQuestions10APIView,EQuestions11APIView,EQuestions12APIView,\
EQuestions13APIView,EQuestions14APIView,IQuestions1APIView,IQuestions2APIView,VQuestion1APIView,MatchDataRetrieveEfficientListView,MatchDataRetrieveEfficientListViewPdf\
,payLoadView,referalResponseAPIView,preRatingAPIView#PurchasesListCreateView,PurchasesRetrieveUpdateDestroyView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from Matching_Algorithm.views import pdf


router = routers.DefaultRouter()
urlpatterns = router.urls


urlpatterns +=[
    path('contact',UserDetailAPIView.as_view({'get':'list','post':'create'}),name='user_detail_create'),
    path('account',UserDetail2APIView.as_view({'get':'list','post':'create'}),name='user_detail2_create'),
    path('cost-time',EQuestionsAPIView.as_view({'get':'list','post':'create'}),name='equestionapi'),
    path('stage',EQuestions1APIView.as_view({'get':'list','post':'create'}),name='equestion_one'),
    path('entity',EQuestions2APIView.as_view({'get':'list','post':'create'}),name='equestion_two'),
    path('pre-capital',EQuestions3APIView.as_view({'get':'list','post':'create'}),name='equestion_three'),
    path('pre-market',EQuestions4APIView.as_view({'get':'list','post':'create'}),name='equestion_four'),
    path('planned-raise',EQuestions5APIView.as_view({'get':'list','post':'create'}),name='equestion_five'),
    path('rounds',EQuestions6APIView.as_view({'get':'list','post':'create'}),name='equestion_six'),
    path('use-of-funds',EQuestions7APIView.as_view({'get':'list','post':'create'}),name='equestion_seven'),
    path('risk-assesments',EQuestions8APIView.as_view({'get':'list','post':'create'}),name='equestion_Eight'),
    path('all-documents',DocumentsPreparedAPIView.as_view({'get':'list','post':'create'}),name='doucmentspreparedall'),
    path('documents-prepared',EQuestions9APIView.as_view({'get':'list','post':'create'}),name='equestion_Nine'),
    path('referal-response',referalResponseAPIView.as_view({'get':'list','post':'create'}),name='referal_response'),
    path('pre-rating',preRatingAPIView.as_view({'get':'list','post':'create'}),name='pre-rating'),
    path('financials-prepared',EQuestions10APIView.as_view({'get':'list','post':'create'}),name='equestion_ten'),
    path('marketing-and-presentation',EQuestions11APIView.as_view({'get':'list','post':'create'}),name='equestion_eleven'),
    path('people-and-culture',EQuestions12APIView.as_view({'get':'list','post':'create'}),name='equestion_twelve'),
    path('legal-offering-risk',EQuestions13APIView.as_view({'get':'list','post':'create'}),name='equestion_thirteen'),
    path('naics',EQuestions14APIView.as_view({'get':'list','post':'create'}),name='equestion_fourteen'),
    path('iquestion-one',IQuestions1APIView.as_view(),name='iquestion_one'),
    path('iquestion-two',IQuestions2APIView.as_view(),name='iquestion_two'),
    path('vquestion-one',VQuestion1APIView.as_view(),name='vquestion_one'),
    #path('match-data/', MatchDataRetrieveListView.as_view(), name='match_data_list'),
    #path('match-data/<int:user_id>', MatchDataRetrieveListView.as_view(), name='match_data_detail'),
    path('match-data-json', MatchDataRetrieveEfficientListView.as_view({'get':'list'}), name='match_datae_list'),
    path('match-letter-pdf',MatchDataRetrieveEfficientListViewPdf.as_view({'get':'get'}),name='match_datae_list_pdf'),
    path('pay-load-string',payLoadView.as_view({'get':'list','post':'create'}),name='pay_load_string'),
    #path('match-datae/<int:user_id>', MatchDataRetrieveEfficientListView.as_view(), name='match_datae_detail'), 
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.authtoken'))
    #path('purchases/', PurchasesListCreateView.as_view(), name='purchases-list-create'),
    #path('purchases/<int:user_id>/', PurchasesRetrieveUpdateDestroyView.as_view(), name='purchases-detail'),           
    #path('match-data/<int:user_id>/', MatchDataDetailView.as_view(), name='match_data_detail'),
    #path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),    
]