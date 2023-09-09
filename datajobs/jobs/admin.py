from django.contrib import admin
from jobs.models import Job


class BaseInputFieldFilter(admin.SimpleListFilter):
    template = "jobs/admin_input_filter.html"

    def lookups(self, request, model_admin):
        return ((None, None),)


class TitleFilter(BaseInputFieldFilter):
    title = "title"
    parameter_name = "title"

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(title__icontains=value)


class CompanyFilter(BaseInputFieldFilter):
    title = "company"
    parameter_name = "company"

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(company__icontains=value)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("id", "jobkey", "title", "company", "updated")
    list_filter = (TitleFilter, CompanyFilter, "created", "updated")
