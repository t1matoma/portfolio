from django.db import models

class Projects(models.Model):
    title = models.CharField('Name', max_length=25)
    full_text = models.TextField('Project')
    github_link = models.CharField('Github link', max_length=50)
    anons = models.CharField('Anons', max_length=50)
    video_url = models.URLField('Video URL', null=True, blank=True)

    def __str__(self):
        return self.title