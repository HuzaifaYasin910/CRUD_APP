from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib import messages
from .models import *
from .forms import BookForm
from django.core.exceptions import ValidationError
# Create your views here.
def home(request):
    books = Book.objects.all()
    return render(request,"crudapp/home.html", {'books' : books})

def add_author(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Author.objects.create(name=name)
    authors = Author.objects.all()
    return render(request,"crudapp/add_author.html",{'authors':authors,})
def del_author(request,author_pk):
    get_object_or_404(Author,pk=author_pk).delete()
    return redirect('/add_author')



def add_language(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Language.objects.create(name=name)
    language = Language.objects.all()
    print(language)
    return render(request,"crudapp/add_language.html",{'languages':language,})

def del_language(request,language_pk):
    get_object_or_404(Language,pk=language_pk).delete()
    return redirect('/add_language')

def add_category(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Category.objects.create(name=name)
    category = Category.objects.all()
    return render(request,"crudapp/add_category.html",{'categories':category,})

def del_category(request,category_pk):
    get_object_or_404(Category,pk=category_pk).delete()
    return redirect('/add_category')


    
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        isbn = request.POST.get('isbn')
        language_id = int(request.POST.get('language'))
        date_published = request.POST.get('date_published')
        author_name = request.POST.get('author')
        category_ids = request.POST.getlist('categories') 
        
        language_instance = Language.objects.get(id=language_id)
        
        
        author_instance, created = Author.objects.get_or_create(name=author_name)
        
        book_instance = Book.objects.create(
            title=title,
            isbn=isbn,
            language=language_instance,
            date_published=date_published,
        )
        
        book_instance.author.set([author_instance])
        book_instance.categories.set(category_ids)
        
        return redirect('/')
    else:
        form = BookForm()
    
    languages = Language.objects.all()
    authors = Author.objects.all()
    categories = Category.objects.all()
    context = {
        'languages': languages,
        'authors': authors,
        'categories': categories,
        'form': form,
    }
    
    return render(request, 'crudapp/add_book.html', context)

def del_book(request,book_pk):
    get_object_or_404(Book,pk=book_pk).delete()
    return redirect('/')

def update_book(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)  

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)  
        if form.is_valid():
            book.title = form.cleaned_data['title']
            book.isbn = form.cleaned_data['isbn']  
            book.language = form.cleaned_data['language']  
            author = form.cleaned_data['author'] 
            book.author.set(author)    
            categories = form.cleaned_data['categories']
            book.categories.set(categories)     
            book.save() 
            return redirect('/')  
    else:
        form = BookForm(instance=book)
    context = {'form': form, 'book': book}
    return render(request, 'crudapp/update_book.html', context)