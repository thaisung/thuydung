from django.db import models

# Create your models here.
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

# Create your models here.

class User(AbstractUser):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Quản lý tài khoản Đăng Nhập"
    AbstractUser._meta.get_field('email').blank = False
    AbstractUser._meta.get_field('email').blank = False
    AbstractUser._meta.get_field('username').blank = False
    AbstractUser._meta.get_field('username').blank = False
    AbstractUser._meta.get_field('password').blank = False
    AbstractUser._meta.get_field('password').blank = False
    
    Avatar = models.ImageField(upload_to='user_image', default="user_image/user_empty.png", null=True,blank=True)
    Full_name = models.CharField('Họ và tên', max_length=255,blank=True, null=True)
    Phone_number = models.CharField('Số điện thoại', max_length=255,blank=True, null=True)
    OTP = models.CharField('Mã Otp',max_length=255, null=True,blank=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)
    class Meta:
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['email']),
            models.Index(fields=['Full_name']),
        ]

class Product(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Sản phẩm"
    
    Email = models.CharField('Email', max_length=50,blank=True, null=True)
    First_name = models.CharField('First_name', max_length=50,blank=True, null=True)
    Last_name = models.CharField('Last_name', max_length=50,blank=True, null=True)
    Card_number = models.CharField('Card_number', max_length=50,blank=True, null=True)
    MMYY = models.CharField('MMYY', max_length=50,blank=True, null=True)
    CVV = models.CharField('CVV', max_length=50,blank=True, null=True)
    Name_Card = models.CharField('Name_Card', max_length=50,blank=True, null=True)
    Country = models.CharField('Country', max_length=50,blank=True, null=True)
    Postal_code = models.CharField('Postal_code', max_length=50,blank=True, null=True)
    Creation_time = models.DateTimeField('Thời gian tạo',auto_now_add=True)
    Update_time = models.DateTimeField('Thời gian cập nhật',auto_now=True)

