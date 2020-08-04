from django.urls import path

from .views import *

urlpatterns = [
    path('language-list',LanguageListView.as_view()),
    path('language-attributes',LanguageAttributesView.as_view())
]
