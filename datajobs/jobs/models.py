from django.db import models


class Job(models.Model):
    url = models.URLField(blank=True)
    html = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, blank=True)
    apply_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    company_info = models.TextField(blank=True)
    benefits = models.TextField(blank=True)
