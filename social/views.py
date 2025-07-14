from django.shortcuts import render
from.models import Social
# Create your views here.
def services (request):
    sociales= Social.objects.all()
    return render(request, "", {"sociales": sociales})