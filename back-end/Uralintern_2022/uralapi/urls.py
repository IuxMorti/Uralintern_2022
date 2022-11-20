from django.urls import path, include
from .views import *

urlpatterns = [
    path('login', main_page_login),
    path('profile', profile),
    path('teamIntern/<int:team_id>/', team_intern),
    path('estimationFormIntern', estimation_form_intern),
    path('reportsIntern', reports_intern),
    path('teamTutor/<int:team_id>/', team_tutor),
    path('estimationFormTutor', estimation_form_tutor),
    path('reportsTutor', reports_tutor),
    path('stages', stages),
    path('api/v1/Profile', CustomerAPIView.as_view()),
    path('api/v1/lk-auth/', include('rest_framework.urls'))
]
