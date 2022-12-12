from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import *
from .serializers import *


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['role_director'] = user.role_director
        token['role_tutor'] = user.role_tutor
        token['role_intern'] = user.role_intern
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def get_routes(request):
    routes = [
        '/token',
        '/token/refresh',
    ]

    return Response(routes)


# class CustomerAPIView(generics.ListAPIView):
#     def get(self, request):
#         c = Customer.objects.all()
#         return Response({'posts': CustomerSerializer(c, many=True).data})
#
#     def post(self, request):
#         serializer = CustomerSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         post_new = Customer.objects.create(
#             surname=request.data['surname'],
#             firstname=request.data['firstname'],
#             patronymic=request.data['patronymic'],
#             role_director=request.data['role_director'],
#             role_tutor=request.data['role_tutor'],
#             role_intern=request.data['role_intern'],
#             mail=request.data['mail'],
#             password=request.data['password'],
#             educational_institution=request.data['educational_institution'],
#             specialization=request.data['specialization'],
#             course=request.data['course'],
#             telephone=request.data['telephone'],
#             telegram=request.data['telegram'],
#             vk=request.data['vk'],
#             image=request.data['image'],
#         )
#
#         return Response({'post': CustomerSerializer(post_new).data})

#
# class CustomerAPIView(generics.ListCreateAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer


def main_page_login(request):
    return render(request, 'authentication.html')


def main_page(request):
    return render(request, 'trainee/welcome-page.html')


def profile(request):
    return render(request, 'trainee/profile-change-info.html')


def profile_change(request):
    return render(request, 'trainee/profile-save-info.html')


# def profile_edit(request):
#     return HttpResponse('<h1>Редактирование профиля</h1>')

def team_intern(request):
    return render(request, 'trainee/team.html')


def estimation_form_intern(request):
    return render(request, 'trainee/forms.html')


def reports_intern(request):
    return render(request, 'trainee/reports.html')


@api_view()
@permission_classes([IsAuthenticated])
def get_user(request, id):
    user = request.user
    a = Customer.objects.get(id=int(id))
    b = CustomerSerializer(a)
    return Response(b.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def change_user(request, id, *args, **kwargs):
    user = request.user
    if user.id != int(id):
        return Response(status=401)
    serializer = CustomerSerializer(data=request.data, instance=request.user)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view()
@permission_classes([IsAuthenticated])
def get_user_teams(request, id_user):
    intern_teams = Team.objects.filter(interns__in=[id_user])
    tutor_teams = Team.objects.filter(id_tutor=int(id_user))
    # director_teams = Team.objects.filter(id_tutor=int(id_user))
    b = TeamSerializer(intern_teams, many=True)
    c = TeamSerializer(tutor_teams, many=True)
    return Response({'intern': b.data, 'tutor': c.data})


@api_view()
@permission_classes([IsAuthenticated])
def get_team(request, id_team):
    a = Team.objects.get(id=int(id_team))
    b = TeamSerializer(a)
    return Response(b.data)


@api_view()
@permission_classes([IsAuthenticated])
def get_estimate(request):
    a = Estimation.objects.all()
    b = EstimationSerializer(a, many=True)
    return Response(b.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def estimate(request, id, *args, **kwargs):
    estimation = request.data
    estimation['id_appraiser'] = request.user.id
    # пробуем получить оценку, если есть, то обновить существующую, если None, то создать новую
    instance_estimation = Estimation.objects.select_related('id_appraiser', 'id_intern', 'id_stage', 'id_team') \
        .filter(id_appraiser=estimation['id_appraiser'], id_intern=estimation['id_intern'],
                id_stage=estimation['id_stage'], id_team=estimation['id_team']).first()
    # операция обновления стоит дороже
    serializer = EstimationSerializer(instance_estimation, data=estimation) if instance_estimation else \
        EstimationSerializer(data=estimation)

    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view()
@permission_classes([IsAuthenticated])
def get_estimations(request, id_user, id_team):
    if int(request.user.id) != int(id_user) and int(request.user.id) != int(Team.objects.get(id=id_team).id_tutor.id.id):
        return Response({'Вы не можете смотреть данные отчеты'})
    self_estimations = Estimation.objects.filter(id_appraiser=id_user, id_team=id_team, id_intern=id_user)
    self_estimation = get_report(self_estimations)
    team_estimations = Estimation.objects.filter(~Q(id_appraiser=id_user), id_team=id_team, id_intern=id_user)
    team_estimation = get_report(team_estimations)
    total_estimation = team_estimations.first()
    total_estimation.competence1 = (self_estimation.competence1 + team_estimation.competence1) / 2
    total_estimation.competence2 = (self_estimation.competence2 + team_estimation.competence2) / 2
    total_estimation.competence3 = (self_estimation.competence3 + team_estimation.competence3) / 2
    total_estimation.competence4 = (self_estimation.competence4 + team_estimation.competence4) / 2
    return Response({'total_estimation': ReportSerializer(total_estimation).data,
                     'self_estimation': ReportSerializer(self_estimation).data,
                     'team_estimation': ReportSerializer(team_estimation).data})

def get_report(estimations):
    estimation = estimations.first()
    if len(estimations) != 0:
        estimation.competence1 = sum([i.competence1 for i in estimations]) / len(estimations)
        estimation.competence2 = sum([i.competence2 for i in estimations]) / len(estimations)
        estimation.competence3 = sum([i.competence3 for i in estimations]) / len(estimations)
        estimation.competence4 = sum([i.competence4 for i in estimations]) / len(estimations)
    return estimation

# def estimation_form_tutor(request):
#     return HttpResponse('<h1>Форма оценки у куратора</h1>')
#
#
# def team_tutor(request, team_id):
#     return HttpResponse(f'<h1>Команда куратора</h1> <p>{team_id}</p>')
#
#
# def reports_tutor(request):
#     return HttpResponse('<h1>Отчёты у куратора</h1>')
#
#
# def stages(request):
#     return HttpResponse('<h1>Этапы у куратора</h1>')