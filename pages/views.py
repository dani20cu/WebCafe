from django.shortcuts import render, get_object_or_404
from.models import Page

# Create your views here.
def pages (request, page_id):
    paginas= get_object_or_404(Page, id=page_id)
    return render(request, "pages/politica.html", {"pages": paginas})
#
#def pages (request):
#   return render(request, "pages/politica.html")