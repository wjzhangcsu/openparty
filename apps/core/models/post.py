# -*- coding: utf-8 -*-
from django.db import models

from apps.member.models import Member


class Post(models.Model):

    content = models.TextField(u'内容', blank=False) # post_content
    content_type = models.CharField(u'内容格式', blank=False, max_length=80, default='html')
    title = models.CharField(u'标题', blank=False, max_length=512) # post_title
    summary = models.TextField(u'摘要', blank=True) # post_excerpt
    status = models.IntegerField(blank=False, null=False, default=0) #post_status
    post_name = models.CharField(u'短名称(引用url)', blank=True, max_length=256) # post_name 'open' -> 10
    to_ping = models.CharField(u'Ping文章', blank=True, max_length=512) # to_ping
    created_at = models.DateTimeField(u'创建时间', blank=False, null=False, auto_now_add=True) # post_date
    modified_at = models.DateTimeField(u'更新时间', blank=False, null=False, auto_now=True) # post_modified
    guid = models.CharField(u'Canonical网址', blank=True, max_length=512) # guid
    
    author = models.CharField(u'发表人', blank=False, max_length=256)
    created_by = models.ForeignKey(Member, related_name='post_created', verbose_name=u"创建人")
    comment_count = models.IntegerField(u'评论数量', blank=False, null=False, default=0) # comment_count

    class Meta:
        app_label = 'core'
