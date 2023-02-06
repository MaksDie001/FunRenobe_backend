from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar_img = models.ImageField(upload_to="photos/%Y/%m/%d/")
    last_join = models.DateTimeField(auto_now_add=True,null=True,auto_created=True)
    is_writer = models.BooleanField(default=False,null=True)
    phone = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.username


class Renobe_chapters(models.Model):
    chapter_title = models.CharField(max_length=155)
    chapter_text_fiel = models.FileField(upload_to="text/%Y/%m/%d/",null=True)
    translators = models.ManyToManyField(User, related_name="transletor")
    date_time=models.DateTimeField(auto_created=True,auto_now_add=True,null=True)
    audio = models.FileField(upload_to="audio/%Y/%m/%d/")
    chapter_number = models.IntegerField(default=0)
    renobe=models.ForeignKey("Renobe",related_name="Renobe",on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.chapter_title


class Renobe(models.Model):
    slug=models.SlugField()
    writer_user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    writer_is_text = models.CharField(max_length=155,null=True,blank=True)
    renobe_name = models.CharField(max_length=255)
    renobe_title = models.TextField()
    renobe_img=models.ImageField(upload_to="photos/%Y/%m/%d/")
    date_join = models.DateField(auto_created=True,auto_now_add=True)
    last_update = models.DateTimeField(auto_created=True, auto_now_add=True)
    tags = models.ManyToManyField("Tags")
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.renobe_name



class Group(models.Model):
    name = models.CharField(max_length=155)
    group_admin = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="group_admin",null=True)
    group_members = models.ManyToManyField(User, related_name="group_members")
    title = models.TextField()
    group_tematic = models.TextField()
    group_tematic_tags = models.ManyToManyField("Tags")
    date_join = models.DateField(auto_created=True)


class Tags(models.Model):
    tags = models.CharField(max_length=55,unique=True)
    description_short = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.tags

class Comment(models.Model):
    text = models.TextField
    date = models.DateTimeField(auto_created=True, auto_now_add=True)
    self = models.ForeignKey("Comment", on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    post = models.ForeignKey(Renobe, on_delete=models.SET_NULL,null=True)


class Team_group(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL,null=True)

