from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

admin.site.unregister(Group)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'firstname', 'patronymic',
                    'role_director', 'role_tutor', 'role_intern',
                    'mail', 'password')
    list_display_links = ('id', 'surname')
    search_fields = ('surname', 'firstname', 'patronymic')
    list_filter = ('role_director', 'role_tutor', 'role_intern')


@admin.register(EventUts)
class EventUtsAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    search_fields = ('title', 'start_date')
    list_filter = ('start_date', 'end_date')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id_event', 'title', 'id_director', 'start_date', 'end_date')
    search_fields = ('id_event', 'title', 'id_director')
    list_filter = ('start_date', 'end_date')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('title', 'id_project', 'id_tutor')
    search_fields = ('id_project', 'title', 'id_tutor')
    list_filter = ('title', 'id_project', 'id_tutor')


@admin.register(InternTeam)
class InternTeamAdmin(admin.ModelAdmin):
    list_display = ('id_team', 'id_intern')


@admin.register(StageTeam)
class StageTeamAdmin(admin.ModelAdmin):
    list_display = ('id_team', 'id_stage')


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
    search_fields = ('title', 'active')
    list_filter = ('active',)


@admin.register(EvaluationCriteriaStage)
class EvaluationCriteriaStageAdmin(admin.ModelAdmin):
    list_display = ('id_stage', 'id_evaluationCriteria')


@admin.register(EvaluationCriteria)
class EvaluationCriteriaAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title',)


@admin.register(Intern)
class InternAdmin(admin.ModelAdmin):
    list_display = ('id', 'role')
    search_fields = ('id', 'role')


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'role')
    search_fields = ('id', 'role')


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'role')
    search_fields = ('id', 'role')


@admin.register(Estimation)
class EstimationAdmin(admin.ModelAdmin):
    list_display = ('id_appraiser', 'customer_role', 'id_project', 'id_team', 'id_stage', 'id_intern', 'time_voting')
    search_fields = ('id_appraiser', 'customer_role', 'id_project', 'id_team', 'id_stage', 'id_intern', 'time_voting')
    list_filter = ('id_appraiser', 'customer_role', 'id_project', 'id_team', 'id_stage', 'id_intern', 'time_voting')
    readonly_fields = ('id_appraiser', 'customer_role', 'id_project', 'id_team', 'id_stage', 'id_intern', 'time_voting')

    def has_add_permission(self, request, obj=None):
        return False
