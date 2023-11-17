from django.db import models


class Student(models.Model):

    username = models.CharField(max_length=100, verbose_name='Name')
    email = models.EmailField()
    password = models.CharField(max_length=16, verbose_name='Password')

    class Meta:
        db_table = 'Student'
        verbose_name_plural = 'Student Data Management'

    def __str__(self):
        return self.username
