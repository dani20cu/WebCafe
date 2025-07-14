from .models import Social

def social_dict(request):
    diccionario = {}
    sociales= Social.objects.all()
    for social in sociales:
        diccionario[social.key] = social.url
    return diccionario


#clave- valor
# ejemplo
# dict= "LINK_Facebook":"http://facebook.com, "LINK_Twiiter":"http://x.com, "LINK_Instagram":"http://instagram.com, 