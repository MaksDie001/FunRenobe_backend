from django.urls import path
from .views import *
urlpatterns = [
    path("",Renobe_chapters_API.as_view()),
    path("chapter/<str:pk>",Renobe_chapters_List.as_view()),
    path("renobe/<slug:slug>",One_Renobe_API.as_view()),
    path("<int:pk>",One_Renobe_API.as_view()),
    path("home/<int:pk>",hz.as_view(),name="home"),
    path('<int:pk>/like/', AddLike.as_view(), name='like'),
    path('<int:pk>/dislike/', AddDislike.as_view(), name='dislike'),
]