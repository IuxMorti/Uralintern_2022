from django.urls import path, include
from .views import *

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', get_routes),
    # path('main', main_page_login),
    # path('profile', profile),
    # path('profile-change', profile_change),
    # path('team', team_intern),
    path('form', estimation_form_intern),
    path('reports', reports_intern),
    # path('api/v1/Profile', CustomerAPIView.as_view()),
    # path('api/v1/lk-auth/', include('rest_framework.urls')),
    # path('accounts/profile', reports_intern),
    # path('teamTutor/<int:team_id>/', team_tutor),
    # path('estimationFormTutor', estimation_form_tutor),
    # path('reportsTutor', reports_tutor),
    # path('stages', stages),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/<int:id>', get_user),
    path('user-change/<int:id>', change_user),
    path('get-user-teams/<int:id_user>', get_user_teams),
    path('get-team/<int:id_team>', get_team),
    path('estimate/<int:id>', estimate),
    path('estimate/', get_estimate),
    path('get-estimations/<int:id_user>/<int:id_team>', get_estimations),
]
