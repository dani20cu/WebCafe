from django.shortcuts import render

# Create your views here.
def visitanos(request):
        return render(request, "visitanos/store.html")