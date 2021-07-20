from django.urls import path, include
from . import views

urlpatterns = [
    path('users/all/', views.UserView.as_view({'get':'list'}), name='all-users'),
    path('users/<int:pk>', views.UserView.as_view({'get':'retrieve'}), name='retrive-user'),
    path('users/register/', views.UserView.as_view({'post':'create'}), name='register-new-user'),
    # # path('team/delete/<int:pk>/',views.TeamView.as_view(get= 'destroy'), name='delete-team'),
    # path('team/update/<int:pk>/',views.UpdateTeamView.as_view(), name='update-team'),
    # path('team/add-member/<int:pk>/',views.AddMemberToTeamView.as_view(), name='update-team')
]