"""AAIT_official_forum_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# 配置路由之后即为RESTful API
from django.contrib import admin
from django.urls import path
from AAIT_official_forum import views
from rest_framework.routers import DefaultRouter,url
from django.views.generic import TemplateView
from django.urls import include

administrator_list=views.AdministratorViewSet.as_view({'get':'list','post':'create'})
administrator_detail=views.AdministratorViewSet.as_view({'get':'retrieve'})

article_detail=views.ArticleViewSet.as_view({'get':'retrieve'})
article_list=views.ArticleViewSet.as_view({'get':'list','post':'create'})

goods_list=views.GoodsViewSet.as_view({'get':'list','post':'create'})
goods_detail=views.GoodsViewSet.as_view({'get':'retrieve'})

poromodoclock_list=views.PoromodoClockViewSet.as_view({'get':'list','post':'create'})
poromodoclock_detail=views.PoromodoClockViewSet.as_view({'get':'retrieve'})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('administrator/',administrator_list),
    url(r'administrator_edit/id/(?P<pk>[0-9]+)$',administrator_detail),
    url(r'article_detail/id/(?P<pk>[0-9]+)$', article_detail),
    path('article/', article_list),
    url('goods/', goods_list),
    url(r'goods_detail/id/(?P<pk>[0-9]+)$', goods_detail),
    url('poromodoclock/', poromodoclock_list),
    url(r'poromodoclock_detail/id/(?P<pk>[0-9]+)$', poromodoclock_detail),
]
