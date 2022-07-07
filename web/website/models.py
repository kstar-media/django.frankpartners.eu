from django.db import models

class service(models.Model):
    GROUP = (
        ('ESG', 'ESG'),
        ('Integrity', 'Integrity'),
        ('Investigations', 'Investigations'),
    )

    title = models.CharField(max_length=500, blank=True, null=True)
    group = models.CharField(
        max_length=20,
        choices=GROUP,
        default='ESG',
        db_index=True,
    )
    headline = models.CharField(max_length=500, blank=True, null=True)
    intro = models.CharField(max_length=1000, blank=True, null=True)
    background_image = models.ImageField(upload_to ='uploads/', blank=True, null=True)
    service1_headline = models.CharField(max_length=500, blank=True, null=True)
    service1_icon = models.CharField(max_length=500, blank=True, null=True)
    service1_text = models.CharField(max_length=1000, blank=True, null=True)
    service2_headline = models.CharField(max_length=500, blank=True, null=True)
    service2_icon = models.CharField(max_length=500, blank=True, null=True)
    service2_text = models.CharField(max_length=1000, blank=True, null=True)
    service3_headline = models.CharField(max_length=500, blank=True, null=True)
    service3_icon = models.CharField(max_length=500, blank=True, null=True)
    service3_text = models.CharField(max_length=1000, blank=True, null=True)
    service_link = models.URLField(blank=True, null=True)


class team(models.Model):
    firstname = models.CharField(max_length=500, blank=True, null=True)
    lastname = models.CharField(max_length=500, blank=True, null=True)
    position = models.CharField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=500, blank=True, null=True)
    pic = models.ImageField(upload_to ='team/', blank=True, null=True) 
    linkedin = models.URLField (max_length=2000, blank=True, null=True)
    bio = models.CharField(max_length=50000, blank=True, null=True)
    languages = models.CharField(max_length=2000, blank=True, null=True)
    since = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)

class home(models.Model):
    headline = models.CharField(max_length=1000, blank=True, null=True)
    intro = models.CharField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to ='uploads/', blank=True, null=True)
    text = models.CharField(max_length=1000, blank=True, null=True)

class value(models.Model):
    headline = models.CharField(max_length=500, blank=True, null=True)
    intro = models.CharField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to ='uploads/', blank=True, null=True)
    text = models.CharField(max_length=1000, blank=True, null=True)

class about(models.Model):
    headline = models.CharField(max_length=500, blank=True, null=True)
    intro = models.CharField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to ='uploads/', blank=True, null=True)
    text = models.CharField(max_length=1000, blank=True, null=True)