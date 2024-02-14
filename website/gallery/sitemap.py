from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Category, Photo

class CategorySitemap(Sitemap):
    priority = 0.7         # 優先度

    def items(self):
        return Category.objects.all()

    def location(self, item):
        return reverse('category_detail', args=[item.pk])  # 'category_detail'はCategory詳細ページのURL名を仮定

class PhotoSitemap(Sitemap):
    priority = 0.9

    def items(self):
        return Photo.objects.all()

    def location(self, item):
        return reverse('photo_detail', args=[item.pk])  # 'photo_detail'はPhoto詳細ページのURL名を仮定
