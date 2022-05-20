from django.contrib.sitemaps import Sitemap
from proj.models import Category, Post

from django.shortcuts import reverse

class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()


class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.filter()

    
    def lastmod(self, obj):
        return obj.created_at