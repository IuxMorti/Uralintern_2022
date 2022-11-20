from rest_framework import serializers
from .models import Customer



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('surname', 'firstname', 'patronymic',
                  'role_director', 'role_tutor', 'role_intern',
                  'mail', 'password', 'educational_institution',
                  'specialization', 'course', 'telephone',
                  'telegram', 'vk', 'image')
# class CustomerSerializer(serializers.Serializer):
#     surname = serializers.CharField(max_length=100)
#     firstname = serializers.CharField(max_length=100)
#     patronymic = serializers.CharField(max_length=100)
#     role_director = serializers.BooleanField()
#     role_tutor = serializers.BooleanField()
#     role_intern = serializers.BooleanField(default=True)
#     mail = serializers.EmailField(max_length=250)
#     password = serializers.CharField(max_length=10, read_only=True)
#     educational_institution = serializers.CharField(max_length=500, read_only=True)
#     specialization = serializers.CharField(max_length=500, read_only=True)
#     course = serializers.CharField(max_length=2, read_only=True)
#     telephone = serializers.CharField(max_length=100, read_only=True)
#     telegram = serializers.URLField(read_only=True)
#     vk = serializers.URLField(read_only=True)
#     image = serializers.ImageField(read_only=True)