from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .serializer import ArticleGetSerializer, ArticleSerializer
from rest_framework.decorators import api_view
from ..models import Article
from rest_framework import status
from django.http import HttpResponse


@api_view(['GET'])
def article_view(request):
    if request.method == 'GET':
        queryset = Article.objects.all()
        serializer = ArticleGetSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'detail': 'method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def article_detail(request, pk):
    if request.method == 'GET':
        try:
            queryset = Article.objects.get(id=pk)
        except Exception as e:
            return Response({'detail': f'{e.args}'}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = ArticleGetSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
def article_create(request):
    if request.method == 'POST':
        data = request.data
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({'detail': 'creations are not valid'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def article_delete(request, pk):
    try:
        article = Article.objects.get(id=pk)
    except Article.DoseNotExist:
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'DELETE':
        article.delete()
        return Response({'detail': 'article deleted'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT', 'PATCH'])
def article_update(request, pk):
    try:
        article = Article.objects.get(id=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT' or request.method == 'PATCH':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)








