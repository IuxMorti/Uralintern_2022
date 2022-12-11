from rest_framework import serializers
from .models import *


# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ('surname', 'firstname', 'patronymic',
#                   'role_director', 'role_tutor', 'role_intern',
#                   'email', 'unhashed_password', 'educational_institution',
#                   'specialization', 'course', 'telephone',
#                   'telegram', 'vk', 'image')
class CustomerSerializer(serializers.Serializer):
    surname = serializers.CharField()
    firstname = serializers.CharField()
    patronymic = serializers.CharField()
    role_director = serializers.BooleanField()
    role_tutor = serializers.BooleanField()
    role_intern = serializers.BooleanField()
    email = serializers.EmailField()
    unhashed_password = serializers.CharField()
    educational_institution = serializers.CharField(allow_null=True)
    specialization = serializers.CharField(allow_null=True)
    course = serializers.CharField(allow_null=True)
    telephone = serializers.CharField(allow_null=True)
    telegram = serializers.URLField(allow_null=True)
    vk = serializers.URLField(allow_null=True)
    image = serializers.ImageField(allow_null=True)

    def update(self, instance, validated_data):
        instance.surname = validated_data.get('surname', instance.surname)
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.patronymic = validated_data.get('patronymic', instance.patronymic)
        instance.role_director = validated_data.get('role_director', instance.role_director)
        instance.role_tutor = validated_data.get('role_tutor', instance.role_tutor)
        instance.role_intern = validated_data.get('role_intern', instance.role_intern)
        instance.email = validated_data.get('email', instance.email)
        instance.unhashed_password = validated_data.get('unhashed_password', instance.unhashed_password)
        instance.educational_institution = validated_data.get('educational_institution', instance.educational_institution)
        instance.specialization = validated_data.get('specialization', instance.specialization)
        instance.course = validated_data.get('course', instance.course)
        instance.telephone = validated_data.get('telephone', instance.telephone)
        instance.telegram = validated_data.get('telegram', instance.telegram)
        instance.vk = validated_data.get('vk', instance.vk)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance


class InternsSerializer(serializers.Serializer):
    id = CustomerSerializer()


class EvaluationCriteriaSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()


class StageSerializer(serializers.Serializer):
    id_project = serializers.CharField()
    title = serializers.CharField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    description = serializers.CharField()
    evaluation_criteria = EvaluationCriteriaSerializer(many=True)


class TeamSerializer(serializers.Serializer):
    id_project = serializers.CharField()
    title = serializers.CharField()
    id_tutor = serializers.CharField()
    interns = InternsSerializer(many=True)
    # stages = StageSerializer(many=True)
    team_chat = serializers.URLField()


# class TeamSerializer(serializers.ModelSerializer):
#     # interns = CustomerSerializer(many=True)
#     class Meta:
#         model = Team
#         fields = ('id_project', 'title', 'id_tutor', 'interns', 'stages', 'team_chat')

# class EstimationSerializer(serializers.Serializer):
#     id_appraiser