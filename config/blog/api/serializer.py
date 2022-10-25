from rest_framework import serializers
from ..models import Article


class ArticleGetSerializer(serializers.ModelSerializer):
    cat_name = serializers.CharField(source='cat.name', read_only=True)

    class Meta:

        model = Article
        fields = ['id', 'title', 'cat_id', 'cat_name', 'slug', 'image', 'content', 'zone_cat', 'created_at']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'cat', 'slug', 'image', 'content', 'zone_cat', "views", 'created_at']
        extra_kwargs = {
             'views': {'read_only': True}
        }



