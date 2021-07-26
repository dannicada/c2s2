from django.urls import path, include
from . import views


urlpatterns = [
    path('users/all/', views.UserView.as_view({'get':'list'}), name='all-users'),
    path('users/<int:pk>/', views.UserView.as_view({'get':'retrieve'}), name='retrive-user'),
    path('me/', views.UserView.as_view({'get': 'retrieve'}), name= 'get-my-info'),
    path('register/', views.UserRegistrationView.as_view(), name='register-new-user'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('users/search/<str:email>/', views.RetrieveUserView().as_view(), name='get-user-by-email'),
    # # path('team/delete/<int:pk>/',views.TeamView.as_view(get= 'destroy'), name='delete-team'),
    # path('team/update/<int:pk>/',views.UpdateTeamView.as_view(), name='update-team'),
    # path('team/add-member/<int:pk>/',views.AddMemberToTeamView.as_view(), name='update-team')
]