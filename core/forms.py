from django import forms
from .models import Basic_info, Experience, Education, Interest, Skills


class BasicInfoForm(forms.ModelForm):
    class Meta:
        model = Basic_info
        fields = '__all__'
        exclude = ['user']


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
        exclude = ['fname', 'user']


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'
        exclude = ['fname', 'user']


class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = '__all__'
        exclude = ['fname', 'user']


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'
        exclude = ['fname','user']

        
