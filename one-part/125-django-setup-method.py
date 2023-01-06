from django.views import View
from django.contrib.auth.models import User 
from django.shortcuts import render


"""
   setup()

   initialize attributes shared by all view methods

"""



class HomeView(View):

    def setup(self, request, *args, **kwargs):
        self.users = User.objects.all()
        name = kwargs['name']
        return super().setup(request, *args, **kwargs)

    def get(self,request,name):
        user = self.users
        return render(request, "home:home.html", {"user":user})

    def post(self,request,name):
        user = self.users
        return render(request, "home:home.html", {"user":user})