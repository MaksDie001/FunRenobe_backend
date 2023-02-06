from django.views.generic import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class One_Renobe_API(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Renobe.objects.all()
    serializer_class = Renobe_Serializer

class Renobe_chapters_List(generics.ListAPIView):
    serializer_class = Renobe_chapters_list_serializers

    def get_queryset(self):
        x=self.kwargs["pk"]
        return Renobe_chapters.objects.filter(renobe__slug=x)

class Renobe_chapters_API(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Renobe_chapters.objects.all()
    serializer_class =  Renobe_chapters_serializers

class hz(DetailView):
    template_name = "backend/home.html"
    context_object_name = "renobe"
    model = Renobe

class AddLike(LoginRequiredMixin, View):

    def post(self, request, pk, *args, **kwargs):
        post = Renobe.objects.get(pk=pk)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break


        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)

        return HttpResponseRedirect(reverse('home', args=[str(pk)]))




class AddDislike(LoginRequiredMixin, View):

    def post(self, request, pk, *args, **kwargs):
        post = Renobe.objects.get(pk=pk)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)



        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)

        if is_dislike:
            post.dislikes.remove(request.user)

        return HttpResponseRedirect(reverse('home', args=[str(pk)]))
