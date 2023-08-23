from django import forms
from .models import Resume

GENDER_CHOICES=[
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),
]

JOB_CITY_CHOICE = [
 ('Delhi', 'Delhi'),
 ('Pune', 'Pune'),
 ('Mumbai', 'Mumbai'),
 ('Banglore', 'Banglore')
]

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Preferred Job Locations', choices=JOB_CITY_CHOICE, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model=Resume
        fields=['id','name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_image','my_resume']
        
        labels={'name':'Full Name','dob':'Date of Birth','gender':'Gender','locality':'Locality','city':'City','pin':'Pin Code','state':'State','mobile':'Mobile No','email':'Email Id','job_city':'Job City','profile_image':'Profile Image','my_resume':'Resume'}

        widgets = {
   'name':forms.TextInput(attrs={'class':'form-control'}),
   'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
   'locality':forms.TextInput(attrs={'class':'form-control'}),
   'city':forms.TextInput(attrs={'class':'form-control'}),
   'pin':forms.NumberInput(attrs={'class':'form-control'}),
   'state':forms.Select(attrs={'class':'form-select'}),
   'mobile':forms.NumberInput(attrs={'class':'form-control'}),
   'email':forms.EmailInput(attrs={'class':'form-control'}),
  }