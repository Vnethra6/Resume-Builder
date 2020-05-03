from django.conf.urls import url
from .views import homepage
from .views import Basic_infoCreateView, resume_builder_section, basic_info_check, experience_info_check,\
    ExperienceCreateView, education_info_check, EducationCreateView, SkillsCreateView, skill_info_check,\
    interest_info_check, InterestCreateView, Basic_infoUpdateView, EducationUpdateView, ExperienceUpdateView,\
    InterestUpdateView, SkillsUpdateView, preview

"""basic_info, education, experience, interest, skills, , download"""

urlpatterns = [
    url(r'^basic_info/$', basic_info_check, name='basic_info_check'),
    url(r'^experience_info/$', experience_info_check, name='experience_check'),
    url(r'^education_info/$', education_info_check, name='education_check'),
    url(r'^skills_info/$', skill_info_check, name='skills_check'),
    url(r'^interest_info/$', interest_info_check, name='interest_check'),

    url(r'^basic_create/$', Basic_infoCreateView.as_view(), name='basic_info'),
    url(r'^experience_create/$', ExperienceCreateView.as_view(), name='experience'),
    url(r'^education_create/$', EducationCreateView.as_view(), name='education'),
    url(r'^skills_create/$', SkillsCreateView.as_view(), name='skills'),
    url(r'^interest_create/$', InterestCreateView.as_view(), name='interest'),
    url(r'^resume-builder-section/$', resume_builder_section, name='resume-builder-sections'),

    url(r'^basic_update/(?P<user>\w+)/update/$', Basic_infoUpdateView.as_view(), name='basic_update'),
    url(r'^education_update/(?P<user>\w+)/update/$', EducationUpdateView.as_view(), name='education_update'),
    url(r'^experience_update/(?P<user>\w+)/update/$', ExperienceUpdateView.as_view(), name='experience_update'),
    url(r'^interest_update/(?P<user>\w+)/update/$', InterestUpdateView.as_view(), name='interest_update'),
    url(r'^skills_update/(?P<user>\w+)/update/$', SkillsUpdateView.as_view(), name='skills_update'),

    url(r'^preview/$', preview, name='preview'),


    url(r'', homepage, name='homepage'),
]
