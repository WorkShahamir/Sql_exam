from django.db import models
import datetime


class Language(models.Model):
    name = models.CharField(max_length=50, unique=True)
    month_to_learn = models.IntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name == 'java script':
            self.name = 'Java Script'
        super().save(*args, **kwargs)


class AbstractPerson(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.phone_number and self.phone_number.startswith('0'):
            self.phone_number = '+996' + self.phone_number[1:]
        super().save(*args, **kwargs)


class Student(AbstractPerson):
    work_study_place = models.CharField(max_length=255, blank=True, null=True)
    has_own_notebook = models.BooleanField()
    preferred_os = models.CharField(max_length=20, choices=(
        ('Windows', 'Windows'),
        ('MacOS', 'MacOS'),
        ('Linux', 'Linux'),
    ))

    def __str__(self):
        return f'{self.work_study_place} - {self.has_own_notebook} - {self.preferred_os}'


class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=255, blank=True, null=True)
    experience = models.DateField()

    def __str__(self):
        return f'{self.name}'


class Course(models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_started = models.DateField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)

    def get_end_date(self):
        return self.date_started + datetime.timedelta(days=self.language.month_to_learn * 30)

    def __str__(self):
        return f'{self.name} - {self.language} - {self.date_started}'
