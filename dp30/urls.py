"""dp30 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dp30app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createtopic/',views.createtopic,name='createtopic'),
    path('createwebpage/',views.createwebpage,name='createwebpage'),
    path('createaccess/',views.createaccess,name='createaccess'),
    path('displaytopic/<id>',views.displaytopic,name='displaytopic'),
    path('displaywebpage/<webid>',views.displaywebpage,name='displaywebpage'),
    path('displayaccessdetail/<aid>',views.displayaccess,name='displayaccess'),
    path('searchwebpage/',views.searchwebpage,name='searchwebppage'),
    path('update/topic/<tid>',views.updatetopic,name="updatetopic"),
    path('update/webpage/<id>',views.updatewebpage,name="updatewebpage"),
    path('delete/topic/<id>',views.deletetopic,name="deletetopic"),
    path('displayimage/<did>',views.displayimage,name="dispimage"),
    path('topic_form/',views.topic_form,name="topicmodel_form"),
    path('web_form/',views.web_form,name="webform"),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)