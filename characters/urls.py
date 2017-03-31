from django.conf.urls import url
from.views import list_characters, character_detail

urlpatterns = [
    url(r'characters/(?P<pk>[0-9]+)/', character_detail),
    url(r'characters/$', list_characters)
]