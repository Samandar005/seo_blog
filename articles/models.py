from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    description = models.TextField()
    bod = models.DateField()
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='authors/')
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name)
        super(Author, self).save(*args, **kwargs)

    def get_update_author(self):
        return reverse('articles:author_update', args=[self.pk])

    def get_delete_author(self):
        return reverse('articles:author_delete', args=[self.pk])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')
    image = models.ImageField(upload_to='articles/')
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('articles:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

class Comment(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    comment = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"{self.name}"
