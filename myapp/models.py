from django.db import models

# Create your models here.
STATE_CHOICES= (
    ("Andhra Pradesh","Andhra Pradesh"), 
    ("Arunachal Pradesh ","Arunachal Pradesh "), 
    ("Assam","Assam"), 
    ("Bihar","Bihar"), 
    ("Chhattisgarh","Chhattisgarh"), 
    ("Goa","Goa"), 
    ("Gujarat","Gujarat"), 
    ("Haryana","Haryana"), 
    ("Himachal Pradesh","Himachal Pradesh"), 
    ("Jammu and Kashmir ","Jammu and Kashmir "), 
    ("Jharkhand","Jharkhand"), ("Karnataka","Karnataka"), 
    ("Kerala","Kerala"), ("Madhya Pradesh","Madhya Pradesh"), 
    ("Maharashtra","Maharashtra"), 
    ("Manipur","Manipur")
)

class Resume(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.PositiveIntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=50)
    mobile=models.PositiveIntegerField()
    email=models.EmailField()
    job_city=models.CharField(max_length=50)
    profile_image=models.ImageField(upload_to='profileimg',blank=True)
    my_resume=models.FileField(upload_to='doc',blank=True)
