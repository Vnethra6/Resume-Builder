from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Basic_info(models.Model):
    fname = models.CharField(max_length=30, verbose_name="First Name")
    lname = models.CharField(max_length=30, verbose_name="Last Name")
    Email = models.EmailField(max_length=32)
    phone = models.CharField(max_length=12)
    address = models.TextField(default='Bangalore')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Basic_Information"

    def __str__(self):
        return self.fname

    def get_absolute_url(self):
        return reverse('resume-builder-sections')


class Experience(models.Model):
    Jobs = (('1', "Software Developer"), ('2', "Associate Engineer"), ('3', "App Developer"), ('4', "TEST Engineer"), (
        '5', "R&D Engineer"))
    Companies = (('1', "ABC"), ('2', "XYZ"), ('3', "EFG"))
    fname = models.CharField(max_length=30, verbose_name="First Name")
    job_title = models.CharField(max_length=1, choices=Jobs)
    company = models.CharField("Company Details", max_length=1, choices=Companies)
    start_date = models.DateField("Start Date")
    end_date = models.DateField("End Date")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Experience"

    def __str__(self):
        return self.fname

    def get_absolute_url(self):
        return reverse('resume-builder-sections')


class Education(models.Model):
    courses = (('1', "EC"), ('2', "CS"), ('3', "ME"))
    institutions = (('1', "sapthagiri college of engineering"), ('2', "XYZ"), ('3', "ABC"))
    fname = models.CharField(max_length=30, verbose_name="First Name")
    course = models.CharField(max_length=1, choices=courses)
    institution = models.CharField(max_length=1, choices=institutions)
    start_date = models.DateField("Start Date")
    end_date = models.DateField("End Date")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Education"

    def __str__(self):
        return self.fname

    def get_absolute_url(self):
        return reverse('resume-builder-sections')

class Interest(models.Model):
    fname = models.CharField(max_length=30, verbose_name="First Name")
    interests = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Interest"

    def __str__(self):
        return self.fname

    def get_absolute_url(self):
        return reverse('resume-builder-sections')


class Skills(models.Model):
    fname = models.CharField(max_length=30, verbose_name="First Name")
    skills = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Skill Set"

    def __str__(self):
        return self.fname

    def get_absolute_url(self):
        return reverse('resume-builder-sections')
