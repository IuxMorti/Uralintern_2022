from django.urls import path, include
from .views import *

urlpatterns = [
    path('main', main_page_login),
    path('profile', profile),
    path('profile-change', profile_change),
    path('team', team_intern),
    path('form', estimation_form_intern),
    path('reports', reports_intern),
    path('api/v1/Profile', CustomerAPIView.as_view()),
    path('api/v1/lk-auth/', include('rest_framework.urls')),
    path('accounts/profile', reports_intern),
    # path('teamTutor/<int:team_id>/', team_tutor),
    # path('estimationFormTutor', estimation_form_tutor),
    # path('reportsTutor', reports_tutor),
    # path('stages', stages),
]
