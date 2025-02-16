from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=150, verbose_name="Faculty name")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Kafedra(models.Model):
    name = models.CharField(max_length=150, verbose_name="Cafeteria name")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Subject(models.Model):
    name = models.CharField(max_length=150, verbose_name="Subject name")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    kafedra = models.ForeignKey(Kafedra, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        subject_name = self.subject.name if self.subject else 'No subject'
        return f"{self.first_name} {self.last_name} - {subject_name}"

    class Meta:
        ordering = ["last_name", "first_name"]


class Group(models.Model):
    name = models.CharField(max_length=50)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['faculty__name', 'name']


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        group_name = self.group.name if self.group else 'No group'
        return f"{self.first_name} {self.last_name} - {group_name}"

    class Meta:
        ordering = ['group__name', 'first_name', 'last_name']
