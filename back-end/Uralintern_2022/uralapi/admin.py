from django.contrib import admin

from .forms import *
from .models import *
from .functions import generate_password
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources

admin.site.unregister(Group)


class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer
        fields = ('id', 'surname', 'firstname', 'patronymic', 'email', 'unhashed_password', 'role_director', 'role_tutor', 'role_intern')

    def before_save_instance(self, instance, using_transactions, dry_run):
        if not instance.unhashed_password:
            instance.unhashed_password = generate_password()
        return instance


@admin.register(Customer)
class CustomerAdmin(UserAdmin, ImportExportActionModelAdmin):
    add_form = CustomerCreationForm
    form = CustomUserChangeForm
    resource_class = CustomerResource
    model = Customer
    fieldsets = (
        (None, {'fields': ('surname', 'firstname', 'patronymic', 'email', 'unhashed_password', 'role_director', 'role_tutor', 'role_intern')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_superuser', 'is_staff'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'surname', 'firstname', 'patronymic', 'role_director', 'role_tutor', 'role_intern', 'password1', 'password2', 'is_random_password'),
        }),
    )

    list_display = ('id', 'surname', 'firstname', 'patronymic',
                    'role_director', 'role_tutor', 'role_intern',
                    'email', 'unhashed_password')
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
    list_filter = ('id_event', 'id_director', 'start_date', 'end_date')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('title', 'id_project', 'id_tutor')
    search_fields = ('id_project', 'title', 'id_tutor')
    list_filter = ('id_project', 'id_tutor')
    filter_horizontal = ['interns', 'stages']


@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
    search_fields = ('title', 'active')
    list_filter = ('active',)
    filter_horizontal = ['evaluation_criteria', ]


@admin.register(EvaluationCriteria)
class EvaluationCriteriaAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title',)


@admin.register(Intern)
class InternAdmin(admin.ModelAdmin):
    list_display = ('id', 'role_intern')
    search_fields = ('id', 'role')

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'role_tutor')
    search_fields = ('id', 'role')

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'role_director')
    search_fields = ('id', 'role')

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Estimation)
class EstimationAdmin(admin.ModelAdmin):
    list_display = ('id_appraiser', 'customer_role', 'id_project', 'id_team', 'id_stage', 'id_intern', 'time_voting')
    search_fields = ('id_appraiser', 'customer_role', 'id_project', 'id_team', 'id_stage', 'id_intern', 'time_voting')
    list_filter = ('id_appraiser', 'customer_role', 'id_project', 'id_team', 'id_stage', 'id_intern', 'time_voting')
    readonly_fields = ('id_appraiser', 'customer_role', 'id_project', 'id_team', 'id_stage', 'id_intern', 'time_voting')

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
