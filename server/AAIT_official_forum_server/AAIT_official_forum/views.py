from django.shortcuts import render
from rest_framework import permissions,viewsets,renderers,generics
#from rest_framework.filters import DjangoObjectPermissionsFilter
from rest_framework.decorators import api_view
from django.views.generic import View


from AAIT_official_forum.models import Administrator,Article,ArticleBoard,ArticleComment,Goods,PoromodoClock
from AAIT_official_forum.serializers import AdministratorSerializer, PoromodoClockSerializer,ArticleSerializer,ArticleBoardSerializer,ArticleCommentSerializer,GoodsSerializer

# Create your views here.

class AdministratorViewSet(viewsets.ModelViewSet,generics.RetrieveUpdateAPIView,generics.RetrieveDestroyAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer



class ArticleViewSet(viewsets.ModelViewSet,generics.RetrieveUpdateAPIView,generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleBoardViewSet(viewsets.ModelViewSet):
    queryset = ArticleBoard.objects.all()
    serializer_class = ArticleBoardSerializer

class ArticleCommentViewSet(viewsets.ModelViewSet):
    queryset = ArticleComment.objects.all()
    serializer_class = ArticleCommentSerializer

class GoodsViewSet(viewsets.ModelViewSet,generics.RetrieveUpdateAPIView,generics.RetrieveDestroyAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
#zhao


class PoromodoClockViewSet(viewsets.ModelViewSet,generics.RetrieveUpdateAPIView,generics.RetrieveDestroyAPIView):
    queryset = PoromodoClock.objects.all()
    serializer_class = PoromodoClockSerializer
#zhao


def index(request):
    if(request.method=='GET'):
        context = {"msg": "GET请求成功！", "code": 0}
        return render(request, 'index.html', {'context':context})