from django.db import models

class Film(models.Model):

    title = models.CharField('Titulo', max_length=100)
    description = models.TextField('Descrição')
    director = models.CharField('Diretor', max_length=100)
    producer = models.CharField('Produtora', max_length=100)
    release_date = models.DateField('Produzido em', blank=True, null=True)
    rt_score = models.IntegerField('Nota')
    image = models.ImageField(upload_to="films/images", verbose_name='Imagem', null=True, blank=True)
    folder_image = models.ImageField(upload_to="films/images", verbose_name='Imagem principal', null=True, blank=True)
    url = models.URLField('URL', null=True, blank=True)

    class Meta:
        db_table = 'film'
        ordering = ['rt_score']

    def __str__(self):
        return self.title

class Serie(models.Model):

    title = models.CharField('Titulo', max_length=100)
    description = models.TextField('Descrição')
    director = models.CharField('Diretor', max_length=100)
    temps = models.IntegerField('Temporadas')
    release_date = models.DateField('Produzido em', blank=True, null=True)
    rt_score = models.IntegerField('Nota')
    image = models.ImageField(upload_to="series/images", verbose_name='Imagem', null=True, blank=True)
    folder_image = models.ImageField(upload_to="series/images", verbose_name='Imagem principal', null=True, blank=True)
    url = models.URLField('URL', null=True, blank=True)

    class Meta:
        db_table = 'serie'
        ordering = ['temps']

    def __str__(self):
        return self.title
