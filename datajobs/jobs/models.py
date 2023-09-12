from typing import Dict

from django.db import models
from django.forms.models import model_to_dict


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

    def to_dict(self) -> Dict[str, str]:
        d = model_to_dict(self)
        d.pop("id")
        d.pop("html")
        d["url"] = self.get_complete_url()
        d["created"] = self.created.isoformat()
        d["updated"] = self.updated.isoformat()
        return d

    def get_complete_url(self) -> str:
        return f"https://www.indeed.com/viewjob?jk={self.jobkey}"
