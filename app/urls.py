from . import views
from django.urls import path



urlpatterns = [

    path('',views.NameView.as_view()),

]