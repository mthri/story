from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

import shortuuid

from core.utils.model import BaseModel



class Tag(BaseModel):
    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    name = models.CharField(verbose_name='نام', help_text='نام برچسب', max_length=10)
    accept = models.BooleanField(verbose_name='تایید شده', default=False)

    def __str__(self) -> str:
        return self.name


class Story(BaseModel):
    class Meta:
        verbose_name = 'داستان'
        verbose_name_plural = 'داستان ها'

    id = models.CharField(primary_key=True, max_length=7)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(verbose_name='عنوان', max_length=50)
    slug = models.SlugField()
    preview = models.CharField(verbose_name='پیشن نمایش', max_length=150, null=True, blank=True)
    text = models.TextField(verbose_name='متن داستان')
    tags = models.ManyToManyField(Tag, blank=True)
    view = models.PositiveIntegerField(verbose_name='بازدید', default=0)
    accept = models.BooleanField(verbose_name='تایید شده', default=False)
    

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = shortuuid.ShortUUID().random(length=7)
            if not self.preview:
                self.preview = self.text[:140]
            #fix too long value for preview
            self.preview = self.preview[:140]
            self.preview += ' ...'
            self.slug = slugify(self.title)
        

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title