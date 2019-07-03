from django.db import models
from datetime import datetime


class bannerModel(models.Model):
    name = models.CharField(max_length=200, verbose_name='广告名')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name