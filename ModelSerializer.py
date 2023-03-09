from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=32)
    birthday_year = models.PositiveIntegerField()


def __str__(self):
    return self.name


class Biography(models.Model):
    text = models.TextField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Book(models.Model):
    name = models.CharField(max_length=32)
    authors = models.ManyToManyField(Author)

class Article(models.Model):
    name = models.CharField(max_length=32)
    author = models.ForeignKey(Author, models.PROTECT)

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BiographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Biography
        fields = ['text', 'author']


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Article
        exclude = ['name']

class BookSerializer(serializers.ModelSerializer):
    authors = serializers.StringRelatedField(many=True)
    class Meta:
        model = Book
        fields = '__all__'


author1 = Author.objects.create(name='Грин', birthday_year=1880)
serializer = AuthorSerializer(author1)
print(serializer.data) # {'id': 17, 'name': 'Грин', 'birthday_year': 1880}

biography = Biography.objects.create(text='Некоторая биография', author=author1)
serializer = BiographySerializer(biography)
print(serializer.data) # {'text': 'Некоторая биография', 'author': 17}

article = Article.objects.create(name='Некоторая статья', author=author1)
serializer = ArticleSerializer(article)
print(serializer.data) # {'id': 8, 'author': OrderedDict([('id', 17), ('name','Грин'), ('birthday_year', 1880)])}


author2 = Author.objects.create(name='Пушкин', birthday_year=1799)
book = Book.objects.create(name='Некоторая книга')
book.authors.add(author1)
book.authors.add(author2)
book.save()

serializer = BookSerializer(book)
print(serializer.data) # {'id': 9, 'authors': ['Грин', 'Пушкин'], 'name':'Некоторая книга'}