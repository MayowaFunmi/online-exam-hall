import random
import string

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
# Create your models here.
# from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver

def random_code(digit=7, letter=3):
    sample_str = ''.join((random.choice(string.digits) for i in range(digit)))
    sample_str += ''.join((random.choice(string.ascii_uppercase) for i in range(letter)))

    sample_list = list(sample_str)
    final_string = ''.join(sample_list)
    return final_string


'''
def id_gen(size=10, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
'''


class CustomUser(AbstractUser):
    unique_id = models.CharField(default=random_code, max_length=10)
    STATUS = [
        ('candidate', 'candidate'),
        ('examiner', 'examiner')
    ]
    status = models.CharField(choices=STATUS, max_length=20, default=False)


User = get_user_model()

class SchoolAdmin(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.admin.last_name} {self.admin.first_name} ({self.admin.unique_id})'


class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('user',)
        verbose_name = 'Candidate'
        verbose_name_plural = 'Candidates'

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name} ({self.user.unique_id})'


class CandidateProfile(models.Model):
    candidate = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name = models.CharField(max_length=25, help_text='Enter your middle name here if any', null=True)
    # STATUS = [('candidate', 'candidate'),]
    # status = models.CharField(choices=STATUS, max_length=10, default='candidate')
    GENDER = [
        ('Male', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(choices=GENDER, max_length=10, null=True)
    date_of_birth = models.DateField(help_text='Format: YYYY-MM-DD', null=True)
    age = models.BigIntegerField(null=True)
    address = models.CharField(max_length=300, null=True)
    RELIGION = [
        ('Christianity', 'Christianity'),
        ('Islam', 'Islam'),
    ]
    religion = models.CharField(choices=RELIGION, max_length=20, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    # phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    height = models.CharField(max_length=200, null=True, help_text='Provide height in decimal (e.g 1.63)')
    hobbies = models.CharField(max_length=200, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/%Y/%m/%d/', null=True)
    about_me = models.TextField(max_length=300, help_text='Write something about yourself, not more than 300 words', null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('candidate',)
        verbose_name = 'Candidate Profile'
        verbose_name_plural = 'Candidate Profiles'

    def __str__(self):
        return f'{self.candidate.last_name} {self.candidate.first_name} ({self.candidate.unique_id})'


class Examiner(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('user',)
        verbose_name = 'Examiner'
        verbose_name_plural = 'Examiners'

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name} ({self.user.unique_id})'


class ExaminerProfile(models.Model):
    examiner = models.OneToOneField(User, on_delete=models.CASCADE)
    TITLE = [
        ('Mr', 'Mister'),
        ('Mrs', 'Mistress'),
        ('Dr', 'Doctor'),
        ('Prof', 'Professor'),
        ('Engr', 'Engineer'),
        ('Chief', 'Chief'),
    ]
    title = models.CharField(choices=TITLE, max_length=10, null=True)
    middle_name = models.CharField(max_length=25, help_text='Enter your middle name here if any', null=True)
    # STATUS = [('examiner', 'examiner'),]
    # status = models.CharField(choices=STATUS, max_length=10, default='candidate')

    QUALIFICATION = [
        ('NCE', 'NCE'),
        ('HND', 'HND'),
        ('B.Sc', 'B.Sc'),
        ('M.Sc', 'M.Sc'),
        ('PhD', 'PhD'),
    ]
    qualification = models.CharField(choices=QUALIFICATION, max_length=8, null=True)
    document = models.FileField(upload_to='documents/%Y/%m/%d/', null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/%Y/%m/%d/', null=True)
    discipline = models.CharField(max_length=200, null=True)
    published_work = models.URLField(max_length=200, null=True)
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(choices=GENDER, max_length=10, null=True)
    date_of_birth = models.DateField(help_text='Format: YYYY-MM-DD', null=True)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=300, null=True)
    RELIGION = [
        ('Christian', 'Christianity'),
        ('Muslim', 'Islam'),
    ]
    religion = models.CharField(choices=RELIGION, max_length=20, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    # phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    height = models.CharField(max_length=200, null=True, help_text='Provide height in decimal (e.g 1.63)')
    about_me = models.TextField(max_length=300, help_text='Write something about yourself, not more than 300 words' ,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('examiner',)
        verbose_name = 'Examiner Profile'
        verbose_name_plural = 'Examiner Profiles'

    def __str__(self):
        return f'{self.title} {self.examiner.first_name} {self.examiner.last_name} ({self.examiner.unique_id})'


class Location(models.Model):
    user = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    local_govt = models.CharField(max_length=100, null=True, blank=True)
    city_or_town = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=100, null=True, blank=True)
    check_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} ({self.country})'


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_staff:
            SchoolAdmin.objects.create(admin=instance)
        if instance.status == 'candidate':
            Candidate.objects.create(user=instance)
            CandidateProfile.objects.create(candidate=instance)
        if instance.status == 'examiner':
            Examiner.objects.create(user=instance)
            ExaminerProfile.objects.create(examiner=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.status == 'admin':
        instance.schooladmin.save()
    if instance.status == 'candidate':
        instance.candidate.save()
        instance.candidateprofile.save()
    if instance.status == 'examiner':
        instance.examiner.save()
        instance.examinerprofile.save()

# model for candidates to register for exams
# create another app for examiners to set questions and students to register for and write exams
