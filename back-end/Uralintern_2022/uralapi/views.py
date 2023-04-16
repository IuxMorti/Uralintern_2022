import validators
from rest_framework import status
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
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


@api_view()
@permission_classes([IsAuthenticated])
def get_user(request, id):
    user = UserSerializer(User.objects.get(id=int(id)))
    return Response(user.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def change_user(request, id, *args, **kwargs):
    user = request.user
    if user.id != int(id):
        return Response(status=status.HTTP_403_FORBIDDEN)
    serializer = UserSerializerUpdate(data=request.data, instance=request.user)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def change_user_image(request, id):
    user = User.objects.get(id=int(id))
    if request.user.id != int(id):
        return Response(status=status.HTTP_403_FORBIDDEN)
    user.image = request.data['image']
    user.save()
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view()
@permission_classes([IsAuthenticated])
def get_user_teams(request, id_user):
    intern_teams = Team.objects.filter(interns__in=[id_user])
    tutor_teams = Team.objects.filter(id_tutor=int(id_user))
    # director_teams = Team.objects.filter(id_tutor=int(id_user))
    if request.user.id != int(id_user):
        return Response(status=status.HTTP_403_FORBIDDEN)
    b = TeamSerializer(intern_teams, many=True)
    c = TeamSerializer(tutor_teams, many=True)
    return Response({'intern': b.data, 'tutor': c.data})


@api_view()
@permission_classes([IsAuthenticated])
def get_team(request, id_team):
    a = Team.objects.get(id=int(id_team))
    b = TeamSerializer(a)
    return Response(b.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def change_chat(request, id_team):
    team = Team.objects.get(id=int(id_team))
    if team.id_tutor.id.id != request.user.id:
        return Response(status=status.HTTP_403_FORBIDDEN)
    if request.data['team_chat'] and not validators.url(request.data['team_chat']):
            return Response(status=status.HTTP_400_BAD_REQUEST)
    team.team_chat = request.data['team_chat']
    team.save()
    serializer = TeamSerializer(team)
    return Response(serializer.data)


@api_view()
@permission_classes([IsAuthenticated])
def get_estimate(request):
    a = Estimation.objects.all()
    b = EstimationSerializer(a, many=True)
    return Response(b.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def estimate(request, *args, **kwargs):
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
def get_estimation(request, id_user, id_team, id_stage):
    if int(request.user.id) != int(id_user):
        return Response(status=status.HTTP_403_FORBIDDEN)
    estimation = Estimation.objects.filter(id_appraiser=id_user, id_team=id_team, id_stage=id_stage)
    if estimation:
        return Response(EstimationSerializer(estimation, many=True).data)
    else:
        return Response([])


@api_view()
@permission_classes([IsAuthenticated])
def get_estimations(request, id_user, id_team):
    if int(request.user.id) != int(id_user) and int(request.user.id) != int(Team.objects.get(id=id_team).id_tutor.id.id):
        return Response(status=status.HTTP_403_FORBIDDEN)
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


@api_view()
@permission_classes([IsAuthenticated])
def get_stages(request, id_team):
    team = Team.objects.get(id=id_team)
    if not team:
        return Response(status=status.HTTP_404_NOT_FOUND)
    stages = Stage.objects.filter(id_project=team.id_project.id)
    return Response(StageSerializer(stages, many=True).data)


@api_view()
@permission_classes([IsAuthenticated])
def get_forms(request, id_user):
    if request.user.id != int(id_user):
        Response(status=status.HTTP_403_FORBIDDEN)
    teams = Team.objects.filter(Q(interns__in=[id_user]) | Q(id_tutor=id_user)).distinct()
    result = {'not estimated': 0, 'estimated': 0, 'total': 0}
    for team in teams:
        forms = get_forms_team(id_user, team.id).data
        result['not estimated'] += forms['not estimated']
        result['estimated'] += forms['estimated']
        result['total'] += forms['total']
    return Response(result)


@api_view()
@permission_classes([IsAuthenticated])
def get_forms_for_team(request, id_user, id_team):
    if request.user.id != int(id_user):
        Response(status=status.HTTP_403_FORBIDDEN)
    return get_forms_team(id_user=id_user, id_team=id_team)


def get_forms_team(id_user, id_team):
    team = Team.objects.get(pk=id_team)
    stages = Stage.objects.filter(Q(id_project=team.id_project.id) | Q(id_team=id_team))
    filtered_stages = []
    for stage in stages:
        if stage.start_date and stage.end_date and stage.start_date <= datetime.date.today() <= stage.end_date:
            filtered_stages.append(stage)
    total_count = team.interns.count() * len(filtered_stages)
    user_estimations = Estimation.objects.filter(id_appraiser=id_user, id_stage__in=filtered_stages, id_team=id_team)
    return Response({'not estimated': total_count - len(user_estimations),
                     'estimated': len(user_estimations),
                     'total': total_count})