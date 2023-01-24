from .models import Link


def context_dict(request):
    links = Link.objects.all() #* Lista tipo QuerySet
    #! Recorremos cada enlace para crear un nuevo valor en context
    context = {link.key:link.url for link in links}

    return context
