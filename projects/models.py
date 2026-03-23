from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=400, help_text='DRF, PostgreSQL, Celery, pytest etc.')
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True, null=True, help_text='Live Project link if deployed')
    demo_video = models.FileField(upload_to='projects/videos/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='projects/thumbnails/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title