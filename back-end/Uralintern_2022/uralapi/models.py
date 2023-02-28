# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import datetime
import os
import django.db.utils
from django.db import models, connection
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from .functions import upload_to
from django.conf import settings


class CustomerManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields) -> 'Customer':
        if email is None:
            raise TypeError('Users must have an email address.')
        customer = self.model(email=self.normalize_email(email))
        customer.set_password(password)
        customer.save()
        return customer

    def create_superuser(self, email, password, **extra_fields) -> 'Customer':
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if password is None:
            raise TypeError('Superusers must have a password.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        customer = self.create_user(email, password, **extra_fields)
        customer.is_superuser = True
        customer.is_staff = True
        customer.save()
        return customer


class Customer(AbstractUser):
    username = models.CharField(max_length=100, verbose_name='----!', null=True, blank=True)
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    firstname = models.CharField(max_length=100, verbose_name='Имя')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество', null=True, blank=True)
    role_director = models.BooleanField(verbose_name='Роль руководителя', default=False)
    role_tutor = models.BooleanField(verbose_name='Роль куратора', default=False)
    role_intern = models.BooleanField(verbose_name='Роль стажёра', default=True)
    email = models.EmailField(_('email address'), unique=True)
    unhashed_password = models.CharField(max_length=20, blank=True, null=True, verbose_name='Пароль')
    educational_institution = models.CharField(max_length=500, blank=True, null=True, verbose_name='Университет')
    specialization = models.CharField(max_length=500, blank=True, null=True, verbose_name='Специальность')
    course = models.IntegerField(blank=True, null=True, verbose_name='Курс обучения',
                                 validators=[MinValueValidator(1), MaxValueValidator(6)])
    telephone = models.CharField(max_length=16, blank=True, null=True, verbose_name='Телефон',
                                 validators=[RegexValidator(regex=r"^\+?1?\d{8,15}$")])
    telegram = models.URLField(blank=True, null=True, verbose_name='Ссылка на телеграмм')
    vk = models.URLField(blank=True, null=True, verbose_name='Ссылка на VK')
    image = models.ImageField(upload_to=upload_to, blank=True, null=True, verbose_name='Фото')

    objects = CustomerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.surname} {self.firstname} {self.patronymic}'

    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.unhashed_password = raw_password  # промежуточно сохраняет пароль и в тоже время хэширует его
        self._password = raw_password

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Director(models.Model):
    id = models.OneToOneField(settings.AUTH_USER_MODEL, models.CASCADE, primary_key=True, db_column='id',
                              verbose_name='Пользователь')
    role_director = models.CharField(max_length=100, verbose_name='Роль')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Руководитель'
        verbose_name_plural = 'Руководители'


class Estimation(models.Model):
    id_appraiser = models.ForeignKey(settings.AUTH_USER_MODEL, models.DO_NOTHING, verbose_name='Оценщик')
    customer_role = models.CharField(max_length=23, verbose_name='Роль пользователя')
    id_project = models.ForeignKey('Project', models.DO_NOTHING, db_column='id_project', verbose_name='Проект')
    id_team = models.ForeignKey('Team', models.DO_NOTHING, db_column='id_team', verbose_name='Команда')
    id_stage = models.ForeignKey('Stage', models.DO_NOTHING, db_column='id_stage', verbose_name='Этап')
    id_intern = models.ForeignKey('Intern', models.DO_NOTHING, db_column='id_intern', verbose_name='Стажёр')
    time_voting = models.DateTimeField(verbose_name='Время голосования', auto_now=True)
    competence1 = models.SmallIntegerField(blank=True, null=True, verbose_name="Вовлеченность",
                                           validators=[MinValueValidator(-1), MaxValueValidator(3)])
    competence2 = models.SmallIntegerField(blank=True, null=True, verbose_name="Организованность",
                                           validators=[MinValueValidator(-1), MaxValueValidator(3)])
    competence3 = models.SmallIntegerField(blank=True, null=True, verbose_name="Обучаемость",
                                           validators=[MinValueValidator(-1), MaxValueValidator(3)])
    competence4 = models.SmallIntegerField(blank=True, null=True, verbose_name="Командность",
                                           validators=[MinValueValidator(-1), MaxValueValidator(3)])

    class Meta:
        verbose_name = 'Собранная оценка'
        verbose_name_plural = 'Собранные оценки'
        unique_together = ('id_appraiser', 'id_team', 'id_stage', 'id_intern')


class EvaluationCriteria(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название критерия оценки')
    description = models.CharField(max_length=1000, verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Критерий оценки'
        verbose_name_plural = 'Критерии оценки'


class EventUts(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название мероприятия')
    start_date = models.DateField(blank=True, null=True, verbose_name='Дата начала')
    end_date = models.DateField(blank=True, null=True, verbose_name='Дата окончания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Intern(models.Model):
    id = models.OneToOneField(settings.AUTH_USER_MODEL, models.CASCADE, primary_key=True, db_column='id',
                              verbose_name='Пользователь')
    role_intern = models.CharField(max_length=100, verbose_name='Роль')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Стажёр'
        verbose_name_plural = 'Стажёры'


class Project(models.Model):
    id_event = models.ForeignKey(EventUts, models.DO_NOTHING, db_column='id_event', verbose_name='Название мероприятия')
    title = models.CharField(max_length=200, verbose_name='Название проекта')
    id_director = models.ForeignKey(Director, models.DO_NOTHING, db_column='id_director', verbose_name='Руководитель')
    start_date = models.DateField(blank=True, null=True, verbose_name='Дата начала')
    end_date = models.DateField(blank=True, null=True, verbose_name='Дата окончания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Stage(models.Model):
    id_project = models.ForeignKey(Project, models.DO_NOTHING, db_column='id_project', verbose_name='Название проекта', null=True)
    id_team = models.ForeignKey('Team', models.DO_NOTHING, verbose_name='Название команды', null=True)
    title = models.CharField(max_length=100, verbose_name='Название этапа')
    start_date = models.DateField(blank=True, null=True, verbose_name='Дата начала')
    end_date = models.DateField(blank=True, null=True, verbose_name='Дата окончания')
    description = models.CharField(max_length=1000, verbose_name='Описание', blank=True, null=True)
    # active = models.BooleanField(verbose_name='Активно')
    default = None
    if 'uralapi_evaluationcriteria' in connection.introspection.table_names():
        default = EvaluationCriteria.objects.filter(pk__lte=4)
    evaluation_criteria = models.ManyToManyField(EvaluationCriteria, verbose_name='Критерии оценки', default=default)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Этап оценивания'
        verbose_name_plural = 'Этапы оценивания'


class Team(models.Model):
    id_project = models.ForeignKey(Project, models.DO_NOTHING, db_column='id_project', verbose_name='Название проекта')
    title = models.CharField(max_length=200, verbose_name='Название команды')
    id_tutor = models.ForeignKey('Tutor', models.DO_NOTHING, db_column='id_tutor', verbose_name='Куратор')
    interns = models.ManyToManyField(Intern, verbose_name='Стажёры', blank=True)
    team_chat = models.URLField(blank=True, null=True, verbose_name='Ссылка на чат')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'


class Tutor(models.Model):
    id = models.OneToOneField(settings.AUTH_USER_MODEL, models.CASCADE, primary_key=True, db_column='id',
                              verbose_name='Пользователь')
    role_tutor = models.CharField(max_length=100, verbose_name='Роль', blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Куратор'
        verbose_name_plural = 'Кураторы'


@receiver(post_save, sender=Customer)
def create_profiles(sender, instance: Customer, **kwargs):
    """Обработчик сигнала. При создании/изменении пользователя создает/удаляет запись о
    нем в таблицах Intern, Tutor или Director(в зависимости от выбранной роли пользователя)"""
    if instance.role_intern:
        if not Intern.objects.filter(id=instance).exists():
            Intern.objects.create(id=instance, role_intern='Стажёр')
    else:
        if Intern.objects.filter(id=instance).exists():
            Intern.objects.get(id=instance).delete()

    if instance.role_tutor:
        if not Tutor.objects.filter(id=instance).exists():
            Tutor.objects.create(id=instance, role_tutor='Куратор')
    else:
        if Tutor.objects.filter(id=instance).exists():
            Tutor.objects.get(id=instance).delete()

    if instance.role_director:
        if not Director.objects.filter(id=instance).exists():
            Director.objects.create(id=instance, role_director='Руководитель')
    else:
        if Director.objects.filter(id=instance).exists():
            Director.objects.get(id=instance).delete()


def change_parent(sender, instance, **kwargs):
    """Обработчик сигнала. Изменяет родителя при удалении дочерней записи."""
    if instance.id:
        if sender is Intern:
            instance.id.role_intern = False
        if sender is Tutor:
            instance.id.role_tutor = False
        if sender is Director:
            instance.id.role_director = False
        instance.id.save()


post_delete.connect(change_parent, sender=Intern)
post_delete.connect(change_parent, sender=Tutor)
post_delete.connect(change_parent, sender=Director)


@receiver(post_save, sender=Project)
def create_stages(sender, instance: Project, **kwargs):
    start_date = instance.start_date
    end_date = instance.end_date
    dates_stage = []
    while start_date < end_date:
        date_stage = [start_date]
        start_date += datetime.timedelta(days=7)
        if start_date > end_date:
            start_date = end_date
        date_stage.append(start_date)
        dates_stage.append(date_stage)
    if int(str(dates_stage[-1][1] - dates_stage[-1][0])[:1]) < 5:
        del dates_stage[-1]
        dates_stage[-1][1] = end_date
    for i in range(len(dates_stage)):
        Stage.objects.create(id_project=instance, start_date=dates_stage[i][0],
                             end_date=dates_stage[i][1], title=f'Неделя {i + 1} ({instance.title})')


@receiver(pre_save, sender=Customer)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    ext = str(instance.image).split('.')[-1]
    old_img = os.path.join(settings.BASE_DIR, f'media/photos/user{instance.id}.{ext}')
    if os.path.exists(old_img):
        os.remove(old_img)
