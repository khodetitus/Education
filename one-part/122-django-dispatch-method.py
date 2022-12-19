# views.py in django
from django.shortcuts import render
from django.views import View


class HomeView(View):
    
    def distpatch(self,request,*args,**kwargs):
        kwargs['name'] ='masoud' 
        if method.request == "GET":
            return self.one(request,*args,**kwargs)
        elif method.request == "POST":
            return self.two(request,*args,**kwargs)
        else:
            return super().dispatch(request,*args,**kwargs)

    def one(self,request,*args,**kwargs):
        return render(request,'home.hmtl',{'name':kwargs['name']})
    
    def two(self,request,*args,**kwargs):
        return render(request,'home.hmtl',{'name':kwargs['name']})

    
#or
# in urls.py
from django.urls import path
url_patterns =[
    path('<str:name>/',HomeView.as_view(),name='home')
] 

# in views.py

class HomeView(View):
    
    def distpatch(self,request,*args,**kwargs):
        if kwargs['name'] == "search":
            return self.one(request,*args,**kwargs)
        else:
            return self.two(request,*args,**kwargs)

    def one(self,request,*args,**kwargs):
        return render(request,'home.hmtl',{'name':kwargs['searching']})
    
    def two(self,request,*args,**kwargs):
        return render(request,'home.hmtl',{'name':kwargs['not searching']})