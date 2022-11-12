# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customer(models.Model):
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    firstname = models.CharField(max_length=100, verbose_name='Имя')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество')
    role_director = models.BooleanField(verbose_name='Роль директора')
    role_tutor = models.BooleanField(verbose_name='Роль куратора')
    role_intern = models.BooleanField(verbose_name='Роль стажёра')
    mail = models.CharField(unique=True, max_length=400, verbose_name='Почта')
    password = models.CharField(max_length=10, blank=True, null=True, verbose_name='Пароль')

    def __str__(self):
        return f'{self.surname} {self.firstname} {self.patronymic}'

    class Meta:
        managed = False
        db_table = 'customer'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Director(models.Model):
    id = models.OneToOneField(Customer, models.DO_NOTHING, db_column='id', primary_key=True, verbose_name='Пользователь')
    role = models.CharField(max_length=100, verbose_name='Роль')

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = False
        db_table = 'director'
        verbose_name = 'Руководитель'
        verbose_name_plural = 'Руководители'


class Estimation(models.Model):
    id_appraiser = models.IntegerField(verbose_name='Оценщик')
    customer_role = models.CharField(max_length=23, verbose_name='Роль пользователя')
    id_project = models.ForeignKey('Project', models.DO_NOTHING, db_column='id_project', verbose_name='Проект')
    id_team = models.ForeignKey('Team', models.DO_NOTHING, db_column='id_team', verbose_name='Команда')
    id_stage = models.ForeignKey('Stage', models.DO_NOTHING, db_column='id_stage', verbose_name='Этап')
    id_intern = models.ForeignKey('Intern', models.DO_NOTHING, db_column='id_intern', verbose_name='Стажёр')
    time_voting = models.DateTimeField(verbose_name='Время голосования')

    class Meta:
        managed = False
        db_table = 'estimation'
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'


class EvaluationCriteria(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название критерия оценки')
    description = models.CharField(max_length=1000, verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'evaluationсriteria'
        verbose_name = 'Критерий оценки'
        verbose_name_plural = 'Критерии оценки'


class EvaluationCriteriaStage(models.Model):
    id_stage = models.OneToOneField('Stage', models.DO_NOTHING, db_column='id_stage', primary_key=True, verbose_name='Этап')
    id_evaluationCriteria = models.ForeignKey(EvaluationCriteria, models.DO_NOTHING, db_column='id_evaluationСriteria', verbose_name='Критерий оценки')

    class Meta:
        managed = False
        db_table = 'evaluationсriteria_stage'
        unique_together = (('id_stage', 'id_evaluationCriteria'),)
        verbose_name = 'Критерий оценки / Этап'
        verbose_name_plural = 'Критерии оценки / Этапы'


class EventUts(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название мероприятия')
    start_date = models.DateField(blank=True, null=True, verbose_name='Дата начала')
    end_date = models.DateField(blank=True, null=True, verbose_name='Дата окончания')

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'event_uts'
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Intern(models.Model):
    id = models.OneToOneField(Customer, models.DO_NOTHING, db_column='id', primary_key=True, verbose_name='Пользователь')
    role = models.CharField(max_length=100, verbose_name='Роль')

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = False
        db_table = 'intern'
        verbose_name = 'Стажёр'
        verbose_name_plural = 'Стажёры'


class InternTeam(models.Model):
    id_team = models.OneToOneField('Team', models.DO_NOTHING, db_column='id_team', primary_key=True, verbose_name='Команда')
    id_intern = models.ForeignKey(Intern, models.DO_NOTHING, db_column='id_intern', verbose_name='Стажёр')

    class Meta:
        managed = False
        db_table = 'intern_team'
        unique_together = (('id_team', 'id_intern'),)
        verbose_name = 'Стажёр / Команда'
        verbose_name_plural = 'Стажёры / Команды'


class Project(models.Model):
    id_event = models.ForeignKey(EventUts, models.DO_NOTHING, db_column='id_event', verbose_name='Название мероприятия')
    title = models.CharField(max_length=200, verbose_name='Название проекта')
    id_director = models.ForeignKey(Director, models.DO_NOTHING, db_column='id_director', verbose_name='Руководитель')
    start_date = models.DateField(blank=True, null=True, verbose_name='Дата начала')
    end_date = models.DateField(blank=True, null=True, verbose_name='Дата окончания')

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'project'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Stage(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название этапа')
    active = models.BooleanField(verbose_name='Активно')

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'stage'
        verbose_name = 'Этап'
        verbose_name_plural = 'Этапы'


class StageTeam(models.Model):
    id_team = models.OneToOneField('Team', models.DO_NOTHING, db_column='id_team', primary_key=True, verbose_name='Название команды')
    id_stage = models.ForeignKey(Stage, models.DO_NOTHING, db_column='id_stage', verbose_name='Этап')

    class Meta:
        managed = False
        db_table = 'stage_team'
        unique_together = (('id_team', 'id_stage'),)
        verbose_name = 'Этап / Команда'
        verbose_name_plural = 'Этапы / Команды'


class Team(models.Model):
    id_project = models.ForeignKey(Project, models.DO_NOTHING, db_column='id_project', verbose_name='Название проекта')
    title = models.CharField(max_length=200, verbose_name='Название команды')
    id_tutor = models.ForeignKey('Tutor', models.DO_NOTHING, db_column='id_tutor', verbose_name='Куратор')

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'team'
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'


class Tutor(models.Model):
    id = models.OneToOneField(Customer, models.DO_NOTHING, db_column='id', primary_key=True, verbose_name='Пользователь')
    role = models.CharField(max_length=100, verbose_name='Роль', blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = False
        db_table = 'tutor'
        verbose_name = 'Куратор'
        verbose_name_plural = 'Кураторы'