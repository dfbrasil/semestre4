from django.db.models import Count
from django.shortcuts import render
from .models import Book, Author, Review, Profile


def query_examples(request):
    # Consulta simples com filter
    books_by_title = Book.objects.filter(title__icontains='teste')

    # Consulta com lookup para buscar autores por nome
    authors_by_name = Author.objects.filter(name__icontains='nome do autor')

    # Consulta many-to-many (livros com uma determinada tag)
    books_with_tag = Book.objects.filter(tags__name='Ficção')

    # Consulta com relacionamento reverso (todos os livros de um autor)
    books_of_author = Book.objects.filter(author__name='Esther Cardoso')

    # Consulta agregada (por exemplo, número de livros de um autor)
    num_books_of_author = Book.objects.filter(author__name='nome do autor').count()
    
    #Consultas com lookup para buscar autores por bio
    authors_with_bio = Author.objects.filter(bio__icontains='Dolores')
    
    #Consultas com Livros com Avaliações Altas
    high_level_books = Book.objects.filter(reviews__rating__gte=4)
    
    #consultas de Perfil de Usuários com Websites Específicos
    users_websites = Profile.objects.filter(website__icontains='freitas')
    
    #Consultas de Listar Livros sem Avaliações
    books_without_reviews = Book.objects.filter(reviews__isnull=True)
    
    #consultas Autores com Maior Número de Livros
    authors_with_more_books = Author.objects.annotate(num_books=Count('books')).order_by('-num_books')
    
    #Consultas com Livros com Resumos Longos
    long_summary_books = []
    for book in Book.objects.all():
        if len(book.summary.split()) > 150:
            long_summary_books.append(book)

    #Consultas Avaliaçoõs de Livros de um Autor Específico
    author_id = 1  # Substitua pelo ID do autor desejado
    reviews_of_author_books = Review.objects.filter(book__author__id=author_id)
    
    #Consultas de Livros com Múltiplas Tags
    books_with_multiple_tags = Book.objects.annotate(num_tags=Count('tags')).filter(num_tags__gt=1)


    # Envie todas as consultas para o template
    context = {
        'books_by_title': books_by_title,
        'authors_by_name': authors_by_name,
        'books_with_tag': books_with_tag,
        'books_of_author': books_of_author,
        'num_books_of_author': num_books_of_author,
        'authors_with_bio': authors_with_bio,
        'high_level_books': high_level_books,
        'users_websites': users_websites,
        'books_without_reviews': books_without_reviews,
        'authors_with_more_books': authors_with_more_books,
        'long_summary_books': long_summary_books,
        'reviews_of_author_books': reviews_of_author_books,
        'books_with_multiple_tags': books_with_multiple_tags,
    }

    return render(request, 'core/teste1.html', context)
