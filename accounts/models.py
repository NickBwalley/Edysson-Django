from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError("Users must have an Email Address!")
		if not username:
			raise ValueError("Users must have a Username")

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)
		user.set_password(password)
		user.save(using=self._db)
		return user
		
		
	def create_superuser(self, email, username, password):
		user = self.create_user(
			email = self.normalize_email(email),
			username=username,
			password=password,		
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.is_verified = True
		user.save(using=self._db)
		return user	

def get_profile_image_filepath(self, filename):
	return f'profile_pics/{self.pk}/{"profile_pic.png"}'


def get_default_profile_image():
	return "default_profile_pic.jpg"


class user(AbstractBaseUser):

	alphanumeric = RegexValidator(r'^[A-Za-z0-9_.]*$', 'Only Letters, Numbers, Underscores and Periods are allowed!')
	# Regex to match 10 to 12 digits only
	# phonenumber = RegexValidator(r'^[0-9]{10,12}$', 'Only Numerical characters are allowed! (Must be 10-12Digits)')

	username		= models.CharField(max_length=30, unique=True, validators=[alphanumeric])
	email 			= models.EmailField(verbose_name="email", max_length=60, unique=True)
	# phonenumber 	= models.CharField(max_length=30, unique=True, validators=[phonenumber])
	country 		= models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)	
	profile_pic 	= models.ImageField(null=True, blank=True, default=get_default_profile_image, upload_to=get_profile_image_filepath)
	bio 			= models.CharField(max_length=40, default="Hey there...", blank=True, null=True)
	date_joined 	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login		= models.DateTimeField(verbose_name='last login', auto_now=True)
	hide_email		= models.BooleanField(default=True)
	hide_phonenumber= models.BooleanField(default=True)
	is_active 		= models.BooleanField(default=True)
	is_admin 		= models.BooleanField(default=False)
	is_verified  	= models.BooleanField(default=False)
	is_staff 		= models.BooleanField(default=False)
	is_superuser 	= models.BooleanField(default=False)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']
	
	objects = MyAccountManager()

	def __str__(self):
		return self.username

	def get_profile_image_filename(self):
		return str(self.profile_pics)[str(self.profile_pics).index(f'profile_pics/{self.pk}/'):]

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True

# class Profile(models.Model):
# 	user 			= models.OneToOneField(user, on_delete=models.CASCADE)
# 	profile_pic 	= models.ImageField(null=True, default="default_profile_pic.jpg", upload_to="profile_pics")
# 	bio 			= models.CharField(max_length=40, default="Hey there...")

# 	def __str__(self):
# 		return self.user.email

# signals
# @receiver(post_save, sender=user)
# def create_user_profile(sender, instance, created, **kwargs):
# 	if created:
# 		Profile.objects.create(user=instance)

# @receiver(post_save, sender=user)
# def save_user_profile(sender, instance, **kwargs):
# 	instance.profile.save()