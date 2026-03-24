from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes', null=True)
    title = models.CharField(max_length=255, default="My Resume")
    name = models.CharField(max_length=255, blank=True)
    about = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    linkedin = models.CharField(max_length=255, blank=True)
    github = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    template = models.CharField(max_length=50, default='classic')

    def __str__(self):
        return f"{self.title}"

class Education(models.Model):
    resume = models.ForeignKey(Resume, related_name='educations', on_delete=models.CASCADE)
    degree = models.CharField(max_length=255, blank=True)
    college = models.CharField(max_length=255, blank=True)
    year = models.CharField(max_length=100, blank=True)
    order = models.IntegerField(default=0)

class Experience(models.Model):
    resume = models.ForeignKey(Resume, related_name='experiences', on_delete=models.CASCADE)
    company = models.CharField(max_length=255, blank=True)
    post = models.CharField(max_length=255, blank=True)
    duration = models.CharField(max_length=100, blank=True)
    desc = models.TextField(blank=True)
    order = models.IntegerField(default=0)

class Project(models.Model):
    resume = models.ForeignKey(Resume, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    duration = models.CharField(max_length=100, blank=True)
    desc = models.TextField(blank=True)
    order = models.IntegerField(default=0)

class Skill(models.Model):
    resume = models.ForeignKey(Resume, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

class Language(models.Model):
    resume = models.ForeignKey(Resume, related_name='languages', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

class Achievement(models.Model):
    resume = models.ForeignKey(Resume, related_name='achievements', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
