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
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=100, blank=True, null=True)
#     description = models.CharField(max_length=300, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'Jobtype'
#
#
# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=80)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#
#
# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
#
#
# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)
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
# class Candidate(models.Model):
#     first_name = models.CharField(max_length=45, blank=True, null=True)
#     last_name = models.CharField(max_length=45, blank=True, null=True)
#     gender = models.TextField(blank=True, null=True)  # This field type is a guess.
#     is_experienced = models.TextField(blank=True, null=True)  # This field type is a guess.
#     image = models.TextField(blank=True, null=True)
#     resume = models.TextField(blank=True, null=True)
#     age = models.DateField(blank=True, null=True)
#     current_ctc = models.FloatField(blank=True, null=True)
#     phone = models.IntegerField(blank=True, null=True)
#     linkedin = models.CharField(db_column='linkedIn', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     skype = models.CharField(max_length=45, blank=True, null=True)
#     email = models.CharField(max_length=45, blank=True, null=True)
#     years_of_experience = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'candidate'
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
#     id = models.IntegerField(primary_key=True)
#     is_currently_working = models.TextField(blank=True, null=True)  # This field type is a guess.
#     company_name = models.CharField(max_length=45, blank=True, null=True)
#     company_adress = models.CharField(max_length=255, blank=True, null=True)
#     country = models.CharField(max_length=45, blank=True, null=True)
#     city = models.CharField(max_length=45, blank=True, null=True)
#     state = models.CharField(max_length=45, blank=True, null=True)
#     job_type_id = models.IntegerField(blank=True, null=True)
#     start_date = models.DateField(blank=True, null=True)
#     end_date = models.DateField(blank=True, null=True)
#     description = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'candidate_exprience'
#
#
# class Company(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=255)
#     profile_description = models.CharField(max_length=400, blank=True, null=True)
#     business_stream_id = models.IntegerField()
#     eatablishment_date = models.DateField(blank=True, null=True)
#     website = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'company'
#
#
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
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
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'
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
#     retype_password = models.CharField(max_length=45, blank=True, null=True)
#     # date_of_birth = models.DateField(blank=True, null=True)
#     # gender = models.TextField(blank=True, null=True)  # This field type is a guess.
#     # is_active = models.TextField(blank=True, null=True)  # This field type is a guess.
#     # contact_number = models.BigIntegerField()
#     # sms_notification = models.TextField()  # This field type is a guess.
#     # email_notification = models.TextField()  # This field type is a guess.
#     # user_image = models.TextField(blank=True, null=True)
#     # registration = models.DateField(blank=True, null=True)
#     # recruiter_name = models.CharField(max_length=55, blank=True, null=True)
#     first_name = models.CharField(max_length=55, blank=True, null=True)
#     last_name = models.CharField(max_length=55, blank=True, null=True)
#     user_id = models.CharField(max_length=55, blank=True, null=True)
#     auth_group = models.IntegerField(blank=True, null=True)
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
