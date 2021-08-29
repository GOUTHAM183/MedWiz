from django.urls import path
from .views import (
    PostListView,
    UpdateDetailView,
    PostDetailView,
    MedicineDetailView,
    
    
)
from . import views

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path('contact/', views.contact, name='contact'),
    
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("update/<int:pk>/", UpdateDetailView.as_view(), name="update-detail"),
    path("medicine/<int:pk>/", MedicineDetailView.as_view(), name="medicine-detail"),
    path("about/", views.about, name="about"),
    path("updates/", views.updates, name="updates"),
    path("medicines/", views.medicines, name="medicines"),
    path("search/", views.search, name="search"),
    path("speech_to_text/",views.speech_to_text,name='speech_to_text')
    
]

