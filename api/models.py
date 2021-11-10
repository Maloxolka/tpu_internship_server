from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db import models


class Skill(models.Model):
    name = models.CharField('Название', max_length=250)

    class Meta:
        db_table = 'skills'
        ordering = ['name']
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField('Имя', max_length=100)
    surname = models.CharField('Фамилия', max_length=100)
    id_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='student_user',
                                verbose_name='Пользователь', db_column='id_user')
    skills = models.ManyToManyField(Skill)
    info = models.TextField('Информация', null=True)
    chat_id = models.IntegerField('Телеграм-чат', null=True)

    class Meta:
        db_table = 'students'
        ordering = ['id_user']
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return f"{self.surname}, {self.name}"


class Project(models.Model):
    name = models.CharField('Название', max_length=250)
    url = models.CharField('Ссылка', max_length=250)
    info = models.TextField('Информация', null=True)
    id_student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='project_student',
                                   verbose_name='Студент', db_column='id_student')

    class Meta:
        db_table = 'projects'
        ordering = ['name']
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField('Название', max_length=250)
    id_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='company_user',
                                verbose_name='Пользователь', db_column='id_user')
    logo_url = models.CharField('Ссылка на логотип', max_length=1000)
    header_url = models.CharField('Ссылка на шапку', max_length=1000)
    site_url = models.CharField('Ссылка на сайт', max_length=1000)
    info = models.TextField('Информация', null=True)

    class Meta:
        db_table = 'companies'
        ordering = ['id_user']
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    name = models.CharField('Название', max_length=250)
    info = models.TextField('Информация', null=True)
    id_company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancy_company',
                                   verbose_name='Компания', db_column='id_company')
    skills = models.ManyToManyField(Skill)
    responses = models.ManyToManyField(Student, through='Response')

    class Meta:
        db_table = 'vacancies'
        ordering = ['name']
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.name


class Response(models.Model):

    class Status(models.TextChoices):
        NEW = 'N', _('New')
        CONSIDERED = 'C', _('Considered')
        ACCEPTED = 'A', _('Accepted')
        DENIED = 'D', _('Denied')

    id_vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='response_vacancy',
                                   verbose_name='Вакансия', db_column='id_vacancy')
    id_student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='response_student',
                                   verbose_name='Студент', db_column='id_student')
    status = models.CharField(
        max_length=1,
        choices=Status.choices,
        default=Status.NEW,
    )

    class Meta:
        db_table = 'responses'
        ordering = ['id_vacancy']
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
