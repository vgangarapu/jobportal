from django.http import *
from django.shortcuts import render
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

import json
import simplejson

from models import (Candidate, CandidateEducation, CandidateExprience,
                    RecruiterAccount, CandidateSkills,CandidateEmployment, CandidateLocation)

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        return HttpResponseRedirect('/dashboard/')
        # user = authenticate(username=username, password=password)
        # if user is not None:
        #     if user.is_active:
        #         login(request, user)
        #         return HttpResponseRedirect('/dashboard/')
    return render(request, 'recruiter-login.html', context={})

def dashboard(request):
    return render(request, 'index.html', context={})

def add_candidate(request):
    if request.POST:
        post_data = request.POST
        profile_url, resume_url = upload_candidate_files(request.FILES)
        candidate = Candidate()
        candidate.first_name = post_data['first_name']
        candidate.last_name = post_data['last_name']
        candidate.phone = post_data['ph_no']
        if Candidate.objects.filter(phone = candidate.phone).exists():
            return errormessage("Phone Number Exists")
        candidate.email = post_data['email_id']
        if Candidate.objects.filter(email = candidate.email).exists():
            return errormessage("Email already exists")
        candidate.skype = post_data['skype_id']
        candidate.linkedin = post_data['linkedin']
        candidate.years_of_experience = int(post_data['work_exp_years']) * 12 + int(post_data['work_exp_months'])
        candidate.image = profile_url
        candidate.resume = resume_url
        candidate.save()
        return HttpResponse(json.dumps({"candidate_id":candidate.id}), content_type='application/json')
    else:
        return render(request, 'add-candidate-profile.html', context={})

def upload_candidate_files(files):
    picture_file_name = files['upload_picture']
    resume_name = files['upload_resume']
    fs = FileSystemStorage()
    picture_storage = fs.save(picture_file_name.name, picture_file_name)
    resume_storage = fs.save(resume_name.name, resume_name)
    return fs.url(picture_storage), fs.url(resume_storage)

def add_candidate_skills(request):
    if request.POST:
        post_data = request.POST
        candidate_id = post_data['candidate_id']
        if not candidate_id:
            return HttpResponse(json.dumps({"status": False, "msg": "Candidate Not yet Added."}), content_type='application/json')
        skills = json.loads(post_data['skills'])
        for skill in skills['data']:
            cskills = CandidateSkills()
            cskills.candidate_id = candidate_id
            cskills.skill = skill['skills']
            cskills.category = skill['name']
            cskills.experience = skill['years']
            cskills.save()
        return HttpResponse(json.dumps({"status": True, "msg": "Candidate Updated."}),
                            content_type='application/json')
    return HttpResponse(json.dumps({"status": False, "msg": "Candidate Skills Not Updated."}),
                        content_type='application/json')

def add_candidate_location(request):
    if request.POST:
        post_data = request.POST
        cand = CandidateLocation()
        cand.candidate_id = post_data['candidate_id']
        cand.country_of_citizenship = post_data['country_citizen']
        cand.country_living_in = post_data['country_living']
        cand.state_living_in = post_data['state_living']
        cand.interested_in_relocating_to = post_data['country_intrested']
        cand.current_city_living_in = post_data['country_city_living']
        cand.willing_to_relocate = post_data['relocate_willing']
        cand.save();
        return HttpResponse(json.dumps({"status": True, "msg": "Candidate Location details updated."}),
                            content_type='application/json')
    return HttpResponse(json.dumps({"status": False, "msg": "Candidate Location details Not Updated."}),
                        content_type='application/json')

def add_candidate_employment(request):
    if request.POST:
        post_data = request.POST
        candidate_id = post_data['candidate_id']
        if not candidate_id:
            return HttpResponse(json.dumps({"status": False, "msg": "Candidate Not yet Added."}), content_type='application/json')
        employment = json.loads(post_data['employment'])
        for employment in employment['data']:
            cemployment = CandidateEmployment()
            cemployment.candidate_id = candidate_id
            cemployment.current_employer = employment['current_employer']
            cemployment.notice_period = employment['notice_period']
            cemployment.current_pay = employment['current_pay']
            cemployment.desired_pay = employment['desired_pay']
            cemployment.comments = employment['comments']
            cemployment.date_available = employment['date_available']
            cemployment.save()
        return HttpResponse(json.dumps({"status": True, "msg": "Candidate Updated."}),
                            content_type='application/json')
    return HttpResponse(json.dumps({"status": False, "msg": "Candidate Employment Not Updated."}),
                        content_type='application/json')


def add_recruiter(request):
    if request.POST:
        post_data = request.POST
        #profile_url, resume_url = upload_candidate_files(request.FILES)
        recruiter_account = RecruiterAccount()
        recruiter_account.first_name = post_data['first_name']
        recruiter_account.last_name = post_data['last_name']
        recruiter_account.email = post_data['email_id']
        if Candidate.objects.filter(email = recruiter_account.email).exists():
            return errormessage("Email already exists")
        recruiter_account.user_acc = post_data['user_acc']
        recruiter_account.password = post_data['password']
        recruiter_account.retype_password = post_data['retype_password']
        recruiter_account.access_level = post_data['access_level']
        recruiter_account.save()
        return HttpResponse(json.dumps({"recruiter_account_id": recruiter_account.id}), content_type='application/json')
    else:
        return render(request, 'add-recruiter.html', context={})

def delete_recruiter(request):
    return render(request, 'delete-recruiter.html', context={})

def delete_candidate(request):
    return render(request, 'delete-candidate.html', context={})

def reset_password(request):
    return render(request, 'reset-password.html', context={})

def search_candidate(request):
    return render(request, 'search.html', context={})

def search_results(request):
    return render(request, 'search-results.html', context={})

def skills(request):
    return render(request, 'skills.html', context={})

def suspend_candidate(request):
    return render(request, 'suspend-candidate.html', context={})

def suspend_recruiter(request):
    return render(request, 'suspend-recruiter.html', context={})

def view_candidate_profile(request):
    return render(request, 'view-candidate-profile.html', context={})

def recruiter_list(request):
    return render(request, 'recruiter-list.html', context={})

def candidate_list(request):
    return render(request, 'candidate-list.html', context={})

def errormessage(msg):
    # To return error messages
    # isinstance(msg, basestring)
    response = HttpResponse(json.dumps(msg), content_type='application/json')
    response.status_code = 400
    return response