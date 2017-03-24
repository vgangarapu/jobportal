from __future__ import unicode_literals

from django.db import models

class Candidate(models.Model):
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    gender = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_experienced = models.TextField(blank=True, null=True)  # This field type is a guess.
    image = models.TextField(blank=True, null=True)
    resume = models.TextField(blank=True, null=True)
    age = models.DateField(blank=True, null=True)
    current_ctc = models.FloatField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True, max_length=15)
    linkedin = models.CharField(db_column='linkedIn', max_length=45, blank=True, null=True)  # Field name made lowercase.
    skype = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    years_of_experience = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate'


class CandidateEducation(models.Model):
    candidate_id = models.IntegerField(blank=True, null=True)
    degree_name = models.CharField(max_length=45, blank=True, null=True)
    year_gradudated = models.DateField(blank=True, null=True)
    university = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_education'


class CandidateExprience(models.Model):
    id = models.IntegerField(primary_key=True)
    is_currently_working = models.TextField(blank=True, null=True)  # This field type is a guess.
    company_name = models.CharField(max_length=45, blank=True, null=True)
    company_adress = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    state = models.CharField(max_length=45, blank=True, null=True)
    job_type_id = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_exprience'

class CandidateSkills(models.Model):
    candidate_id = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=128, blank=True, null=True)
    skill = models.CharField(max_length=128, blank=True, null=True)
    experience = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_skills'

class CandidateEmployment(models.Model):
    candidate_id = models.IntegerField(blank=True, null=True)
    current_employer = models.CharField(max_length=55, blank=True, null=True)
    notice_period = models.CharField(max_length=45, blank=True, null=True)
    current_pay = models.CharField(max_length=45, blank=True, null=True)
    desired_pay = models.CharField(max_length=45, blank=True, null=True)
    comments = models.CharField(max_length=128, blank=True, null=True)
    date_available = models.CharField(max_length=45, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'candidate_employment'

class CandidateLocation(models.Model):
    candidate_id = models.IntegerField(blank=True, null=True)
    country_of_citizenship = models.CharField(max_length=45, blank=True, null=True)
    country_living_in = models.CharField(max_length=45, blank=True, null=True)
    state_living_in = models.CharField(max_length=45, blank=True, null=True)
    interested_in_relocating_to = models.CharField(max_length=45, blank=True, null=True)
    current_city_living_in = models.CharField(max_length=45, blank=True, null=True)
    willing_to_relocate = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidate_location'

class RecruiterAccount(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=45, blank=True, null=True)
    retype_password = models.CharField(max_length=45, blank=True, null=True)
    # date_of_birth = models.DateField(blank=True, null=True)
    # gender = models.TextField(blank=True, null=True)  # This field type is a guess.
    # is_active = models.TextField(blank=True, null=True)  # This field type is a guess.
    contact_number = models.BigIntegerField(blank=True, null=True)
    # sms_notification = models.TextField()  # This field type is a guess.
    # email_notification = models.TextField()  # This field type is a guess.
    # user_image = models.TextField(blank=True, null=True)
    # registration = models.DateField(blank=True, null=True)
    # recruiter_name = models.CharField(max_length=55, blank=True, null=True)
    first_name = models.CharField(max_length=55, blank=True, null=True)
    last_name = models.CharField(max_length=55, blank=True, null=True)
    user_acc = models.CharField(max_length=55)
    auth_group = models.IntegerField(blank=True, null=True)
    access_level = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recruiter_account'