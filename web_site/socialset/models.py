from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    nickname = models.OneToOneField(User, on_delete=models.CASCADE )
    bio = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)


class Follow(models.Model):
    follower = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='follow')
    following = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='following')
    created_at = models.DateTimeField()


class Post(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='post')
    image = models.ImageField(blank=True, null=True)
    caption = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    likes = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='likes')
    hashtag = models.CharField(max_length= 20)


class PostLike(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='web')
    created_at = models.DateTimeField()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='text')
    text = models.TextField()
    created_at = models.DateTimeField()
    likes  = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='creat')


class CommentLike(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='commentlike')
    comment = models.TextField()
    created_at =models.DateTimeField()


class Story(models.Model):
    user =  models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='story')
    image = models.ImageField( blank=True, null=True)
    video = models.FileField()
    created_at = models.DateTimeField()
    expires_at = models.DateTimeField()


class Group(models.Model):
    name = models.CharField(max_length= 30)
    description = models.TextField()
    creator = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='group')
    members = models.CharField(max_length=60)
    join_key = models.CharField(max_length=60)
