"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from adminportal.views import (login_user, dashboard, add_candidate,
                               add_recruiter, delete_recruiter, delete_candidate, reset_password,
                               search_results, skills, suspend_candidate, suspend_recruiter,
                               view_candidate_profile, search_candidate, add_candidate_skills,add_candidate_employment,
                               add_candidate_location, recruiter_list, candidate_list)

urlpatterns = [
    url(r'^login/$', login_user, name='login'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^add_candidate/$', add_candidate, name='add_candidate'),
    url(r'^add_candidate_skills/$', add_candidate_skills, name='add_candidate_skills'),
    url(r'^add_candidate_employment/$', add_candidate_employment, name='add_candidate_employment'),
    url(r'^add_location_details/$', add_candidate_location, name='add_candidate_location'),
    url(r'^add_recruiter/$', add_recruiter, name='add_recruiter'),
    url(r'^delete_recruiter/$', delete_recruiter, name='delete_recruiter'),
    url(r'^delete_candidate/$', delete_candidate, name='delete_candidate'),
    url(r'^reset_password/$', reset_password, name='reset_password'),
    url(r'^search_candidate/$', search_candidate, name='search_candidate'),
    url(r'^search_results/$', search_results, name='search_results'),
    url(r'^skills/$', skills, name='skills'),
    url(r'^suspend_recruiter/$', suspend_recruiter, name='suspend_recruiter'),
    url(r'^suspend_candidate/$', suspend_candidate, name='suspend_candidate'),
    url(r'^view_candidate_profile/$', view_candidate_profile, name='view_candidate_profile'),
    url(r'^recruiter_list/$', recruiter_list, name='recruiter_list'),
    url(r'^candidate_list/$', candidate_list, name='candidate_list'),
    url(r'^admin/', admin.site.urls),
]
