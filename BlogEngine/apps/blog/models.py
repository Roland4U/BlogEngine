from django.db import models
from django.urls import reverse
# from django.core.urlresolvers import reverse
from django.utils.text import slugify
from time import time
from django.contrib.auth.models import User

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + str(int(time()))


class Post(models.Model):
    title = models.CharField(max_length=70, db_index=True)
    slug = models.SlugField(max_length=70, unique=True, blank=True)
    body = models.TextField(db_index=True)
    tags = models.ManyToManyField('Tag', related_name='posts', blank=True)
    autor = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("blog:post_det", kwargs={"slug": self.slug})
   
    def get_edit_url(self):
        return reverse("blog:post_edit", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)       
        super().save(*args, **kwargs) # Call the real save() method

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    comment_text = models.TextField(db_index=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.autor

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

class Tag(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('blog:tag_det', kwargs={'slug': self.slug})

    def get_edit_url(self):
        return reverse("blog:tag_edit", kwargs={"slug": self.slug})


    def __str__(self):
        return self.title    

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

