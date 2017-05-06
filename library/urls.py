from django.conf.urls import  url
from library import views
from django.conf.urls.static import static
#from django.views import static
import os
from online import  settings


urlpatterns = [

    url(r'^$', views.login, name='login'),
    url(r'^login/$',views.login,name = 'login'),
    url(r'^regist/$',views.regist,name = 'regist'),
    url(r'^index/$',views.index,name = 'index'),
    url(r'^logout/$',views.logout,name = 'logout'),


   ]

urlpatterns +=  static(r'/book/',document_root=os.path.join(settings.BASE_DIR,'library','book'))
urlpatterns +=  static(r'/book/',document_root=os.path.join(settings.BASE_DIR,'library','book','*'))