from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=50)
    lat = models.FloatField()  # latitude (широта)
    lng = models.FloatField()  # longitude (долгота)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class User(models.Model):
    ROLE = [('member', 'участник'),
            ('moderator', 'модератор'),
            ('admin', 'администратор')]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=9, choices=ROLE, default='member')
    age = models.PositiveIntegerField()
    locations = models.ManyToManyField(to=Location)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
