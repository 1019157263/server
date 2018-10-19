from rest_framework import serializers
from AAIT_official_forum.models import Administrator,Article,ArticleBoard,ArticleComment,Goods,PoromodoClock


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields=("article_id","user_id","article_time","title","is_valid","content","article_board_id")


class ArticleBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleBoard
        fields=("article_board_id","board_name","board_description","last_article_id")

class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComment
        fields=("article_comment_id","user_id","article_id","content","time")


class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields=("administrator_id","user_id")


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields=("goods_id","price","stock","goods_image","goods_info","is_online")

class PoromodoClockSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoromodoClock
        fields = ('poromodo_clock_id', 'user_id','clock_count','invalid_poromodo_clock')