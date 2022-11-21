from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework import generics
from rest_framework.response import Response

from .models import *
from .serializers import CustomerSerializer


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
