from django.db import models

# Create your models here.

class Modern(models.Model):
    title = models.TextField(max_length=3000, null=False, blank=False)
    status = models.CharField(max_length=100, null=False, blank=False, default='New')
    time = models.CharField(max_length=150, null=True, blank=True)


    class Meta:
        db_table = 'articles'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.id}. {self.time}: {self.title}'
