from django.urls import path
from . import views

urlpatterns = [
    path('management-council/', views.ManagementCouncilList.as_view(), name='management_council_list'),
    path('director-board/', views.DirectorBoardList.as_view(), name='director_board_list'),
    path('chairman/', views.ChairmanList.as_view(), name='chairman_list'),
    path('manager/', views.ManagerList.as_view(), name='manager_list'),
    path('mcqa/', views.MCQAList.as_view(), name='mcqa_list'),
    path('mcqa-member/', views.MCQAmemberList.as_view(), name='mcqa_member_list'),
    path('principal/', views.PrincipalList.as_view(), name='principal_list'),
]
