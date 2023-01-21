from django.db import models

# Create your models here.

class MyYear(models.Model):
    name = models.CharField(max_length=16, unique=True)
    date = models.DateField(blank=True)  # для отображения года
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=16, unique=True)
    caption = models.CharField(max_length=16)        # публикуется caption, а не name
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name + ' [' + self.caption + ']'

# это заметка, состоящая из списка карточек
class History(models.Model):
    name = models.CharField(max_length=16, unique=True)
    caption = models.CharField(max_length=64)        # публикуется caption, а не name
    brief = models.TextField(blank=True)             # краткое описание истории
    description = models.TextField(blank=True)       # для внутреннего пользования
    date = models.DateField(blank=True)              # для отображения месяца и года
    preview = models.ImageField(blank=True)
    visible = models.BooleanField()                  # для публикации/скрытия
    year = models.ForeignKey(MyYear, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Это карточка, из списка которых состоит заметка History
class Card(models.Model):
    # К сожалению, ссылки внутри класса сделать "не разрешает"
    sort_number = models.IntegerField()      # для сортировки карточек внутри "истории"
    txt1 = models.TextField(blank=True)
    picture = models.ImageField(blank=True)
    txt2 = models.TextField(blank=True)
    txt_url = models.TextField(blank=True)   # для описания ссылки на внешний источник
    ref_url = models.URLField(blank=True)    # для ссылки на внешний источник
    history = models.ForeignKey(History, on_delete=models.CASCADE)
    visible = models.BooleanField()          # для публикации/скрытия

    def __str__(self):
        return str(self.id) + ' / h=' + str(self.history) + ' / n=' + str(self.sort_number)






