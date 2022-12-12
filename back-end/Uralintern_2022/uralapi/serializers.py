from rest_framework import serializers
from .models import *
import datetime

# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ('surname', 'firstname', 'patronymic',
#                   'role_director', 'role_tutor', 'role_intern',
#                   'email', 'unhashed_password', 'educational_institution',
#                   'specialization', 'course', 'telephone',
#                   'telegram', 'vk', 'image')
class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
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


class TutorSerializer(serializers.Serializer):
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
    id_tutor = TutorSerializer()
    interns = InternsSerializer(many=True)
    team_chat = serializers.URLField()


class ReportSerializer(serializers.Serializer):
    id_appraiser = serializers.CharField()
    customer_role = serializers.CharField()
    id_project = serializers.CharField()
    id_team = serializers.CharField()
    id_stage = serializers.CharField()
    id_intern = serializers.CharField()
    time_voting = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    competence1 = serializers.FloatField(allow_null=True, validators=[MinValueValidator(-1), MaxValueValidator(3)])
    competence2 = serializers.FloatField(allow_null=True, validators=[MinValueValidator(-1), MaxValueValidator(3)])
    competence3 = serializers.FloatField(allow_null=True, validators=[MinValueValidator(-1), MaxValueValidator(3)])
    competence4 = serializers.FloatField(allow_null=True, validators=[MinValueValidator(-1), MaxValueValidator(3)])


class EstimationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Estimation.objects.create(**validated_data)

    def update(self, instance: Estimation, validated_data):
        # Далее, если в словаре есть такой ключ, перепишет данные в базе, либо оствит то, что было
        instance.competence1 = validated_data.get('competence1', instance.competence1)
        instance.competence2 = validated_data.get('competence2', instance.competence2)
        instance.competence3 = validated_data.get('competence3', instance.competence3)
        instance.competence4 = validated_data.get('competence4', instance.competence4)
        instance.time_voting = datetime.datetime.now()
        instance.save()
        return instance

    class Meta:
        model = Estimation
        fields = ('id_appraiser',
                  'customer_role',
                  'id_project',
                  'id_team',
                  'id_stage',
                  'id_intern',
                  'time_voting',
                  'competence1',
                  'competence2',
                  'competence3',
                  'competence4',)