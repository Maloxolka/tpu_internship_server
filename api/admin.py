from django.contrib import admin

from api.models import Skill, Student, Project, Company, Vacancy, Response


class SkillAdmin(admin.ModelAdmin):
    model = Skill


class StudentAdmin(admin.ModelAdmin):
    model = Student


class ProjectAdmin(admin.ModelAdmin):
    model = Project

class CompanyAdmin(admin.ModelAdmin):
    model = Company


class VacancyAdmin(admin.ModelAdmin):
    model = Vacancy


class ResponseAdmin(admin.ModelAdmin):
    model = Response


admin.site.register(Skill, SkillAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Response, ResponseAdmin)
