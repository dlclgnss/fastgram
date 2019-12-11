from django.shortcuts import render
from django.views.generic.base import TemplateView #해당 템플릿이 있을경우 렌더링을 해준다.
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class HomeView(TemplateView):
    @method_decorator(login_required)
    def dispatch(self,request,*arg,**kwargs):
        return super(HomeView,self).dispatch(request,*arg,**kwargs)

    template_name = 'home.html'
