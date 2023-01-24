from django.urls import path
from . import views

urlpatterns = [
    #! Para que la url tome un elemento...
    #! dinamico se debe pasar entre <> y si se..
    #! Quiere caster se pone type_cast:parametro
    #* Siempre se pasa una string por lo mismo se debe castear
    path('<int:page_id>/<slug:page_slug>/',views.page,name='page'),
]
