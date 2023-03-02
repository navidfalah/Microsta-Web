from django.contrib import admin
from django.urls import path
from document import views


urlpatterns = [
    path('', views.document_view, name="document_view"),
    
]
