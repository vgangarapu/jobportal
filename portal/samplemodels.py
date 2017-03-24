# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from __future__ import unicode_literals
#
# from django.db import models
#
#
# class Companylogo(models.Model):
#     id = models.IntegerField()
#     companyid = models.IntegerField()
#     image = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'Companylogo'
#
#
# class JobLocation(models.Model):
#     job_location_id = models.IntegerField(primary_key=True)
#     address = models.CharField(max_length=300, blank=True, null=True)
#     city = models.CharField(max_length=45, blank=True, null=True)
#     state = models.CharField(max_length=45, blank=True, null=True)
#     zip = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'Job_location'
#
#
# class Jobtype(models.Model):
#     jobtype_id = models.IntegerField(db_column='Jobtype_id', primary_key=True)  # Field name made lowercase.
#     jobtype_name = models.CharField(db_column='Jobtype_name', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     jobtypedescription = models.CharField(max_length=300, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'Jobtype'
#
#
# class BusinessStream(models.Model):
#     business_stream_name = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'business_stream'
#
#
# class CandidateEducation(models.Model):
#     candidate_id = models.IntegerField(blank=True, null=True)
#     degree_name = models.CharField(max_length=45, blank=True, null=True)
#     year_gradudated = models.DateField(blank=True, null=True)
#     university = models.CharField(max_length=45, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'candidate_education'
#
#
# class CandidateExprience(models.Model):
#     candidate_id = models.IntegerField(primary_key=True)
#     iscurrentjob = models.TextField(blank=True, null=True)  # This field type is a guess.
#     company_name = models.CharField(max_length=45, blank=True, null=True)
#     company_adress = models.CharField(max_length=255, blank=True, null=True)
#     country = models.CharField(max_length=45, blank=True, null=True)
#     city = models.CharField(max_length=45, blank=True, null=True)
#     state = models.CharField(max_length=45, blank=True, null=True)
#     jobtypeid = models.IntegerField(blank=True, null=True)
#     startdate = models.DateField(blank=True, null=True)
#     enddate = models.DateField(blank=True, null=True)
#     description = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'candidate_exprience'
#
#
# class CandidateProfile(models.Model):
#     candidate_id = models.IntegerField(primary_key=True)
#     firstname = models.CharField(max_length=45, blank=True, null=True)
#     lastname = models.CharField(max_length=45, blank=True, null=True)
#     gender = models.TextField(blank=True, null=True)  # This field type is a guess.
#     is_experienced = models.TextField(blank=True, null=True)  # This field type is a guess.
#     candidate_image = models.TextField(blank=True, null=True)
#     candidate_resume = models.TextField(db_column='candidate_Resume', blank=True, null=True)  # Field name made lowercase.
#     candidate_age = models.DateField(blank=True, null=True)
#     candidate_ctc = models.FloatField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'candidate_profile'
#
#
# class Company(models.Model):
#     id = models.IntegerField(primary_key=True)
#     companyname = models.CharField(max_length=255)
#     profile_description = models.CharField(max_length=400, blank=True, null=True)
#     business_stream_id = models.IntegerField()
#     eatablishmentdate = models.DateField(blank=True, null=True)
#     companywebsite = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'company'
#
#
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class Jobpost(models.Model):
#     jobpost_id = models.AutoField(primary_key=True)
#     jobtype_id = models.IntegerField(blank=True, null=True)
#     company_id = models.IntegerField()
#     hidecompanydetails = models.TextField(db_column='Hidecompanydetails', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     jobdescription = models.CharField(max_length=255, blank=True, null=True)
#     jobposteddate = models.DateField(blank=True, null=True)
#     jobloacation_id = models.IntegerField(blank=True, null=True)
#     numberofvacancys = models.IntegerField(blank=True, null=True)
#     isactive = models.TextField(blank=True, null=True)  # This field type is a guess.
#     skillsetid = models.IntegerField(blank=True, null=True)
#     added_advantage_skillid = models.IntegerField(db_column='added_ advantage_skillid', blank=True, null=True)  # Field renamed to remove unsuitable characters.
#
#     class Meta:
#         managed = False
#         db_table = 'jobpost'
#
#
# class RecruiterAccount(models.Model):
#     email = models.CharField(max_length=255)
#     password = models.CharField(max_length=45, blank=True, null=True)
#     date_of_birth = models.DateField(blank=True, null=True)
#     gender = models.TextField(blank=True, null=True)  # This field type is a guess.
#     is_active = models.TextField(blank=True, null=True)  # This field type is a guess.
#     contact_number = models.BigIntegerField()
#     sms_notification = models.TextField()  # This field type is a guess.
#     email_notification = models.TextField()  # This field type is a guess.
#     user_image = models.TextField(blank=True, null=True)
#     registration = models.DateField(blank=True, null=True)
#     recruiter_name = models.CharField(max_length=55, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'recruiter_account'
#
#
# class Recruiterlog(models.Model):
#     recruiter_account_id = models.IntegerField()
#     last_login_date = models.DateField(blank=True, null=True)
#     last_job_applied_date = models.DateField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'recruiterlog'
#
#
# class Skillset(models.Model):
#     skillset_id = models.IntegerField(primary_key=True)
#     skill_name = models.CharField(max_length=45, blank=True, null=True)
#     skill_description = models.CharField(db_column='Skill_description', max_length=300, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'skillset'
