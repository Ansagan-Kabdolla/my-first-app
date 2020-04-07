from django.db import models
from vestnik.settings import MEDIA_URL


class Filepdf(models.Model):
    author = models.CharField(max_length=200, verbose_name="Авторы")
    file = models.FileField(upload_to='', verbose_name="Файл")
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    seria = (
        ('mt', 'Математика'),
        ('ph', 'Физика'),
        ('bi', 'Биология'),
        ('ch', 'Химия'),
        ('pd', 'Педагогика'),
        ('lt', 'Литература'),
        ('ek', 'Экономика'),
        ('pr', 'Право'),
    )
    serius = models.CharField(max_length=2, choices=seria, blank=True, default='mt', help_text='Серия публикации')

    def get_absolute_file_upload_url(self):
        return self.file.url

    def __str__(self):
        return self.author


    class Meta:
        verbose_name_plural = "Публикации"
        verbose_name = "Публикация"
        ordering = ['date']
