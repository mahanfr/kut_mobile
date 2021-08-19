from django.db import models

class Staff(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_image = models.ImageField('staff_images',blank=True,null=True)
    group = models.ForeignKey('staff.StaffGroup',models.SET_NULL,blank=True,null=True)
    institute = models.ForeignKey('staff.StaffInstitute',models.SET_NULL,blank=True,null=True)
    responsibility = models.CharField(max_length=255)
    internal_phone_line = models.CharField(max_length=255,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    education = models.CharField(max_length=255,blank=True,null=True)
    date_joind = models.DateField(blank=True,null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class StaffGroup(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class StaffInstitute(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name