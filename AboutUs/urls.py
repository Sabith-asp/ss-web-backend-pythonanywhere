from django.urls import path
from .views import (
    MissionVisionList, HistoryofCollegeList, AboutCollegeList,
    SisterInstituitionList, FormerPrincipalList, AccreditationList,
    RecognitionandAwardList, StrategicPlanList, RTIList
)

urlpatterns = [
    path('mission_vision/', MissionVisionList.as_view(), name='mission_vision-list'),
    path('history_of_college/', HistoryofCollegeList.as_view(), name='history_of_college-list'),
    path('about_college/', AboutCollegeList.as_view(), name='about_college-list'),
    path('sister_institution/', SisterInstituitionList.as_view(), name='sister_institution-list'),
    path('former_principal/', FormerPrincipalList.as_view(), name='former_principal-list'),
    path('accreditation/', AccreditationList.as_view(), name='accreditation-list'),
    path('recognition_and_award/', RecognitionandAwardList.as_view(), name='recognition_and_award-list'),
    path('strategic_plan/', StrategicPlanList.as_view(), name='strategic_plan-list'),
    path('rti/', RTIList.as_view(), name='rti-list'),
]


