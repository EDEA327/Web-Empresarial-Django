from django.urls import path
from . import views

urlpatterns = [
    path('',views.blog,name='blog'),
    #! Para que la url tome un elemento...
    #! dinamico se debe pasar entre <> y si se..
    #! Quiere caster se pone type_cast:parametro
    #* Siempre se pasa una string por lo mismo se debe castear
    path('category/<int:category_id>/',views.category,name='category'),
]
