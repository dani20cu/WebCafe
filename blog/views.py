from django.shortcuts import render
from.models import Post, Category

# Create your views here.
def blogs (request):
        blogs= Post.objects.all()
        categorias= Category.objects.all()
        return render(request, "blog/blog.html", {"categorias": categorias, "blogs": blogs})

