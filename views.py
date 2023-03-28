from rest_framework import viewsets, permissions
from .models import Author, Book
from .serializers import AuthorSerializer, AuthorSerializerBase, BookSerializer, BookSerializerBase


class AuthorViewSet(viewsets.ModelViewSet):

        serializer_class = AuthorSerializer
        queryset = Author.objects.all()
        
        def get_serializer_class(self):
                if self.request.version == '2.0':
                        return AuthorSerializerBase
                return AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
        serializer_class = BookSerializer
        queryset = Book.objects.all()
        
        def get_serializer_class(self):
                if self.request.method in ['GET']:
                        return BookSerializer
                return BookSerializerBase
