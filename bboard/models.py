from django.db import models


class BbManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-published')


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')
    objects = models.Manager()
    reverse = BbManager()

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']


class RubricManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('order', 'name')

    def order_by_bb_count(self):
        return super().get_queryset().annotate(cnt=models.Count('bb')).order_by('-cnt')


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')
    order = models.SmallIntegerField(default=0, db_index=True)
    objects = models.Manager()
    bbs = RubricManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['order', 'name']


class RevRubric(Rubric):
    class Meta:
        proxy = True
        ordering = ['-name']


