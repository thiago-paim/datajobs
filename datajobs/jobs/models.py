from django.db import models


class Job(models.Model):
    jobkey = models.CharField(max_length=50, blank=True, unique=True)
    url = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    relative_time = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    apply_url = models.URLField(blank=True)
    benefits = models.TextField(blank=True)
    html = models.TextField(blank=True)
