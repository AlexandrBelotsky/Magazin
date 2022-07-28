from django.db import models

#МЯСО
class Tovar(models.Model):
    c = (
        ('Есть в наличии', 'Есть в наличии'),
        ('Нет в наличии', 'Нет в наличии'),
        )
    name         = models.CharField(max_length=50)
    price        = models.CharField(max_length=60)
    count        = models.IntegerField()
    availability = models.CharField(max_length=30, choices=c)

class Tovar_kura(models.Model):
    c = (
        ('Есть в наличии', 'Есть в наличии'),
        ('Нет в наличии', 'Нет в наличии'),
        )
    name         = models.CharField(max_length=50)
    price        = models.CharField(max_length=60)
    count        = models.IntegerField()
    availability = models.CharField(max_length=30, choices=c)

class Indushation(models.Model):
    c = (
        ('Есть в наличии', 'Есть в наличии'),
        ('Нет в наличии', 'Нет в наличии'),
    )
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=60)
    count = models.IntegerField()
    availability = models.CharField(max_length=30, choices=c)

#мОЛОКО
class Sir(models.Model):
    c = (
        ('Есть в наличии', 'Есть в наличии'),
        ('Нет в наличии', 'Нет в наличии'),
    )
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=60)
    count = models.IntegerField()
    availability = models.CharField(max_length=30, choices=c)

class Moloko(models.Model):
    c = (
        ('Есть в наличии', 'Есть в наличии'),
        ('Нет в наличии', 'Нет в наличии'),
    )
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=60)
    count = models.IntegerField()
    availability = models.CharField(max_length=30, choices=c)


class Eggs(models.Model):
    c = (
        ('Есть в наличии', 'Есть в наличии'),
        ('Нет в наличии', 'Нет в наличии'),
    )
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=60)
    count = models.IntegerField()
    availability = models.CharField(max_length=30, choices=c)

class Tvorog(models.Model):
    c = (
        ('Есть в наличии', 'Есть в наличии'),
        ('Нет в наличии', 'Нет в наличии'),
    )
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=60)
    count = models.IntegerField()
    availability = models.CharField(max_length=30, choices=c)

#Посуда
class Tarelki(models.Model):
    c = (
        ('Есть в наличии', 'Есть в наличии'),
        ('Нет в наличии', 'Нет в наличии'),
    )
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=60)
    count = models.IntegerField()
    availability = models.CharField(max_length=30, choices=c)

class Vilki(models.Model):
    c = (
        ('Есть в наличии', 'Есть в наличии'),
        ('Нет в наличии', 'Нет в наличии'),
    )
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=60)
    count = models.IntegerField()
    availability = models.CharField(max_length=30, choices=c)



class Zakaz(models.Model):
    w = (
        ('Перезвонить мне', 'Перезвонить мне'),
        ('Не звонить мне', 'Не звонить мне'),
    )
    name        = models.CharField(max_length=50)
    email       = models.EmailField(max_length=60)
    city        = models.CharField(max_length=50)
    tel         = models.IntegerField()
    choice      = models.CharField(max_length=20, choices=w)
    opisanie    = models.TextField(max_length=200)
    count       = models.IntegerField()

