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


class CustomerAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


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