# Generated by Django 3.2.8 on 2023-04-10 17:38

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uralapi.functions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('patronymic', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество')),
                ('image', models.ImageField(blank=True, null=True, upload_to=uralapi.functions.upload_to, verbose_name='Фото')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='EvaluationCriteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название критерия оценки')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Критерий оценки',
                'verbose_name_plural': 'Критерии оценки',
            },
        ),
        migrations.CreateModel(
            name='EventUts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название мероприятия')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Дата начала')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата окончания')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название проекта')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Дата начала')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата окончания')),
                ('evaluation_criteria', models.ManyToManyField(blank=True, to='uralapi.EvaluationCriteria', verbose_name='Критерии оценки')),
                ('id_director', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Руководитель')),
                ('id_event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='uralapi.eventuts', verbose_name='Название мероприятия')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='RoleInTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Роль в команде',
                'verbose_name_plural': 'Роли в команде',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='uralapi.user', verbose_name='Пользователь')),
                ('educational_institution', models.CharField(blank=True, max_length=200, null=True, verbose_name='Университет')),
                ('specialization', models.CharField(blank=True, max_length=200, null=True, verbose_name='Специальность')),
                ('academic_degree', models.CharField(blank=True, max_length=200, null=True, verbose_name='Академическая степень')),
                ('course', models.CharField(blank=True, max_length=100, null=True, verbose_name='Курс обучения')),
                ('telephone', models.CharField(blank=True, max_length=16, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='Телефон')),
                ('telegram', models.URLField(blank=True, null=True, verbose_name='Ссылка на телеграмм')),
                ('vk', models.URLField(blank=True, null=True, verbose_name='Ссылка на VK')),
            ],
            options={
                'verbose_name': 'Информация о пользователе',
                'verbose_name_plural': 'Информация о пользователях',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название команды')),
                ('team_chat', models.URLField(blank=True, null=True, verbose_name='Ссылка на чат')),
                ('teg', models.CharField(max_length=200, unique=True, verbose_name='Тег')),
                ('id_project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='uralapi.project', verbose_name='Название проекта')),
                ('id_tutor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Куратор')),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команды',
            },
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название этапа')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Описание')),
                ('start_date', models.DateField(verbose_name='Дата начала')),
                ('end_date', models.DateField(verbose_name='Дата окончания')),
                ('end_estimation_date', models.DateField(verbose_name='Дата окончания оценки')),
                ('evaluation_criteria', models.ManyToManyField(blank=True, to='uralapi.EvaluationCriteria', verbose_name='Критерии оценки')),
                ('id_team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='uralapi.team', verbose_name='Название команды')),
            ],
            options={
                'verbose_name': 'Этап оценивания',
                'verbose_name_plural': 'Этапы оценивания',
            },
        ),
        migrations.CreateModel(
            name='InternTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_intern', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Стажёр')),
                ('id_team', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='uralapi.team', verbose_name='Команда')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='uralapi.roleinteam', verbose_name='Роль')),
            ],
            options={
                'verbose_name': 'Стажёр_Команда',
                'verbose_name_plural': 'Стажёры_Команды',
                'unique_together': {('id_team', 'id_intern')},
            },
        ),
        migrations.CreateModel(
            name='Estimation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_voting', models.DateTimeField(auto_now=True, verbose_name='Время голосования')),
                ('estimation', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(3)], verbose_name='Оценка')),
                ('id_appraiser', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='appraiser', to=settings.AUTH_USER_MODEL, verbose_name='Оценщик')),
                ('id_evaluation_criteria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='uralapi.evaluationcriteria', verbose_name='Критерий оценивания')),
                ('id_intern', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='intern', to=settings.AUTH_USER_MODEL, verbose_name='Стажёр')),
                ('id_stage', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='uralapi.stage', verbose_name='Этап')),
            ],
            options={
                'verbose_name': 'Собранная оценка',
                'verbose_name_plural': 'Собранные оценки',
                'unique_together': {('id_appraiser', 'id_stage', 'id_evaluation_criteria', 'id_intern')},
            },
        ),
    ]
