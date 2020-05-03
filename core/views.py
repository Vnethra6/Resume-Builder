from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Basic_info, Education, Experience, Interest, Skills
from .forms import BasicInfoForm, ExperienceForm, EducationForm, InterestForm, SkillForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def homepage(request):
    return render(request, 'core/homepage.html')


@login_required(login_url='/users/login/')
def preview(request):
    context = {'user': request.user,
               'basic_info': Basic_info.objects.get(user=request.user),
               'education': Education.objects.get(user=request.user),
               'experience': Experience.objects.get(user=request.user),
               'skills': Skills.objects.get(user=request.user),
               'interest': Interest.objects.get(user=request.user)
               }
    return render(request, 'core/preview.html', context)


@login_required(login_url='/users/login/')
def basic_info_check(request):
    if Basic_info.objects.filter(user=request.user).exists():
        return redirect('basic_update', request.user)
    else:
        return redirect('basic_info')


@login_required(login_url='/users/login/')
def experience_info_check(request):
    if Experience.objects.filter(user=request.user).exists():
        return redirect('experience_update', request.user)
    else:
        return redirect('experience')


@login_required(login_url='/users/login/')
def education_info_check(request):
    if Education.objects.filter(user=request.user).exists():
        return redirect('education_update', request.user)
    else:
        return redirect('education')


@login_required(login_url='/users/login/')
def skill_info_check(request):
    if Skills.objects.filter(user=request.user).exists():
        return redirect('skills_update', request.user)
    else:
        return redirect('skills')


@login_required(login_url='/users/login/')
def interest_info_check(request):
    if Interest.objects.filter(user=request.user).exists():
        return redirect('interest_update', request.user)
    else:
        return redirect('interest')


@login_required(login_url='/users/login/')
def resume_builder_section(request):
    return render(request, 'core/resume_sections.html')


class Basic_infoCreateView(LoginRequiredMixin, CreateView):
    model = Basic_info
    template_name = 'core/Basic_info.html'
    form_class = BasicInfoForm
    print("reaching")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExperienceCreateView(CreateView, LoginRequiredMixin):
    model = Experience
    template_name = 'core/Experience.html'
    form_class = ExperienceForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.fname = self.request.user
        return super().form_valid(form)


class EducationCreateView(CreateView,LoginRequiredMixin):
    model = Education
    template_name = 'core/Education.html'
    form_class = EducationForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.fname = self.request.user
        return super().form_valid(form)


class SkillsCreateView(CreateView, LoginRequiredMixin):
    model = Skills
    template_name = 'core/Skills.html'
    form_class = SkillForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.fname = self.request.user
        return super().form_valid(form)


class InterestCreateView(CreateView, LoginRequiredMixin):
    model = Interest
    template_name = 'core/Interest.html'
    form_class = InterestForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.fname = self.request.user
        return super().form_valid(form)


class Basic_infoUpdateView(UpdateView, LoginRequiredMixin):
    model = Basic_info
    template_name = 'core/Basic_info.html'
    form_class = BasicInfoForm

    def get_object(self, queryset=None):
        return self.model.objects.get(user=self.request.user)


class EducationUpdateView(UpdateView, LoginRequiredMixin):
    model = Education
    template_name = 'core/Education.html'
    form_class = EducationForm

    def get_object(self, queryset=None):
        return self.model.objects.get(user=self.request.user)


class ExperienceUpdateView(UpdateView, LoginRequiredMixin):
    model = Experience
    template_name = 'core/Experience.html'
    form_class = ExperienceForm

    def get_object(self, queryset=None):
        return self.model.objects.get(user=self.request.user)


class InterestUpdateView(UpdateView, LoginRequiredMixin):
    model = Interest
    template_name = 'core/Interest.html'
    form_class = InterestForm

    def get_object(self, queryset=None):
        return self.model.objects.get(user=self.request.user)


class SkillsUpdateView(UpdateView, LoginRequiredMixin):
    model = Skills
    template_name = 'core/Skills.html'
    form_class = SkillForm

    def get_object(self, queryset=None):
        return self.model.objects.get(user=self.request.user)
