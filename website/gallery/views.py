from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Category, Photo
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def gallery(request):
    category = request.GET.get("category")
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {"categories": categories, "photos": photos}
    return render(request, "gallery/gallery.html", context)


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, "gallery/photo.html", {"photo": photo})

@login_required
def addPhoto(request):
    categories = Category.objects.all()

    if request.method == "POST":
        data = request.POST
        images = request.FILES.getlist("images")

        if data["category"] != "none":
            category = Category.objects.get(id=data["category"])
        elif data["category_new"] != "":
            category, created = Category.objects.get_or_create(
                name=data["category_new"]
            )
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data["description"],
                image=image,
            )

        return redirect("gallery")

    context = {"categories": categories}
    return render(request, "gallery/add.html", context)


class LicenseView(TemplateView):
    template_name = "license.html"

@login_required
def deletePhoto(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    if request.method == "POST":
        photo.delete()
        return redirect("gallery")

    return render(request, "gallery/delete.html", {"photo": photo})
