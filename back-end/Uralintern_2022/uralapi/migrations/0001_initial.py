# Generated by Django 3.2.8 on 2022-12-12 13:08

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
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
                ('username', models.CharField(blank=True, max_length=100, null=True, verbose_name='----!')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('firstname', models.CharField(max_length=100, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=100, verbose_name='Отчество')),
                ('role_director', models.BooleanField(default=False, verbose_name='Роль руководителя')),
                ('role_tutor', models.BooleanField(default=False, verbose_name='Роль куратора')),
                ('role_intern', models.BooleanField(default=True, verbose_name='Роль стажёра')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('unhashed_password', models.CharField(blank=True, max_length=20, null=True, verbose_name='Пароль')),
                ('educational_institution', models.CharField(blank=True, max_length=500, null=True, verbose_name='Университет')),
                ('specialization', models.CharField(blank=True, max_length=500, null=True, verbose_name='Специальность')),
                ('course', models.CharField(blank=True, max_length=2, null=True, verbose_name='Курс обучения')),
                ('telephone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Телефон')),
                ('telegram', models.URLField(blank=True, null=True, verbose_name='Ссылка на телеграмм')),
                ('vk', models.URLField(blank=True, null=True, verbose_name='Ссылка на VK')),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
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
                ('description', models.CharField(max_length=1000, verbose_name='Описание')),
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
                ('title', models.CharField(max_length=200, verbose_name='Название мероприятия')),
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
                ('title', models.CharField(max_length=200, verbose_name='Название проекта')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Дата начала')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата окончания')),
                ('id_event', models.ForeignKey(db_column='id_event', on_delete=django.db.models.deletion.DO_NOTHING, to='uralapi.eventuts', verbose_name='Название мероприятия')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='uralapi.customer', verbose_name='Пользователь')),
                ('role_director', models.CharField(max_length=100, verbose_name='Роль')),
            ],
            options={
                'verbose_name': 'Руководитель',
                'verbose_name_plural': 'Руководители',
            },
        ),
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='uralapi.customer', verbose_name='Пользователь')),
                ('role_intern', models.CharField(max_length=100, verbose_name='Роль')),
            ],
            options={
                'verbose_name': 'Стажёр',
                'verbose_name_plural': 'Стажёры',
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='uralapi.customer', verbose_name='Пользователь')),
                ('role_tutor', models.CharField(blank=True, max_length=100, verbose_name='Роль')),
            ],
            options={
                'verbose_name': 'Куратор',
                'verbose_name_plural': 'Кураторы',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название команды')),
                ('team_chat', models.URLField(blank=True, null=True, verbose_name='Ссылка на чат')),
                ('id_project', models.ForeignKey(db_column='id_project', on_delete=django.db.models.deletion.DO_NOTHING, to='uralapi.project', verbose_name='Название проекта')),
                ('id_tutor', models.ForeignKey(db_column='id_tutor', on_delete=django.db.models.deletion.DO_NOTHING, to='uralapi.tutor', verbose_name='Куратор')),
                ('interns', models.ManyToManyField(blank=True, to='uralapi.Intern', verbose_name='Стажёры')),
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
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Дата начала')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата окончания')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание')),
                ('evaluation_criteria', models.ManyToManyField(default=None, to='uralapi.EvaluationCriteria', verbose_name='Критерии оценки')),
                ('id_project', models.ForeignKey(db_column='id_project', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='uralapi.project', verbose_name='Название проекта')),
                ('id_team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='uralapi.team', verbose_name='Название команды')),
            ],
            options={
                'verbose_name': 'Этап оценивания',
                'verbose_name_plural': 'Этапы оценивания',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='id_director',
            field=models.ForeignKey(db_column='id_director', on_delete=django.db.models.deletion.DO_NOTHING, to='uralapi.director', verbose_name='Руководитель'),
        ),
        migrations.CreateModel(
            name='Estimation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_role', models.CharField(max_length=23, verbose_name='Роль пользователя')),
                ('time_voting', models.DateTimeField(auto_now=True, verbose_name='Время голосования')),
                ('competence1', models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(3)], verbose_name='Вовлеченность')),
                ('competence2', models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(3)], verbose_name='Организованность')),
                ('competence3', models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(3)], verbose_name='Обучаемость')),
                ('competence4', models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(-1), django.core.validators.MaxValueValidator(3)], verbose_name='Командность')),
                ('id_appraiser', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Оценщик')),
                ('id_project', models.ForeignKey(db_column='id_project', on_delete=django.db.models.deletion.DO_NOTHING, to='uralapi.project', verbose_name='Проект')),
                ('id_stage', models.ForeignKey(db_column='id_stage', on_delete=django.db.models.deletion.DO_NOTHING, to='uralapi.stage', verbose_name='Этап')),
                ('id_team', models.ForeignKey(db_column='id_team', on_delete=django.db.models.deletion.DO_NOTHING, to='uralapi.team', verbose_name='Команда')),
                ('id_intern', models.ForeignKey(db_column='id_intern', on_delete=django.db.models.deletion.DO_NOTHING, to='uralapi.intern', verbose_name='Стажёр')),
            ],
            options={
                'verbose_name': 'Собранная оценка',
                'verbose_name_plural': 'Собранные оценки',
                'unique_together': {('id_appraiser', 'id_team', 'id_stage', 'id_intern')},
            },
        ),
    ]
