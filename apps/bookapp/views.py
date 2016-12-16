from django.shortcuts import render, HttpResponse, redirect
from .models import User, Book, Review
from django.contrib import messages
from itertools import count


def index(request):
    return render(request, "bookapp/index.html")

def register(request):
    result =  User.objects.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['confirm'])
    if result == True:
        email = request.POST['email']
        user = User.objects.filter(email=email)[0]
        request.session['user_id'] = user.id
        return redirect('/books')
    else:
        request.session['errors'] = result[1]
        return redirect('/')

def login(request):
    result = User.objects.login(request.POST['email'], request.POST['password'])
    if result == True:
        email = request.POST['email']
        user = User.objects.filter(email=email)[0]
        request.session['user_id'] = user.id
        return redirect('/books')
    else:
        request.session['errors'] = result[1]
        return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def newbook(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request, "bookapp/addbook.html")

def addbook(request):
    if 'user_id' not in request.session:
        return redirect('/')
    result = Book.objects.addbook(request.POST['title'], request.POST['author'])
    if result[0] == True:
        title = request.POST['title']
        book = Book.objects.filter(title=title)[0]
        id = book.id
        user = User.objects.filter(id = request.session['user_id'])[0]
        review = Review.objects.create(user = user, book = book, review = request.POST['review'], rating = request.POST['rating'])
        return redirect('/book/{}'.format(book.id))
    else:
        request.session['errors'] = result[1]
        return redirect('/addbook')

def addreview(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.filter(id = request.session['user_id'])[0]
    book = Book.objects.filter(id=id)[0]
    review = Review.objects.create(user = user, book = book, review = request.POST['review'], rating = request.POST['rating'])
    return redirect('/book/{}'.format(book.id))

def viewbook(request, id):
    if 'user_id' not in request.session:
        return redirect('/')
    book = Book.objects.filter(id=id)[0]
    reviews = Review.objects.filter(book=book)
    context = {
        "book":book,
        "reviews":reviews
    }
    return render(request, "bookapp/viewbook.html", context)

def books(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.filter(id=request.session['user_id'])[0]
    books = Book.objects.filter().order_by('-id')[:3]
    reviews = Review.objects.filter()
    context = {
        "user":user,
        "books":books,
        "reviews":reviews
    }
    return render(request, "bookapp/books.html", context)

def user(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.filter(id = request.session['user_id'])[0]
    books = Book.objects.filter().order_by('-id')[:3]
    reviews = Review.objects.filter()
    context = {
        "user":user,
        "books":books,
        "reviews":reviews
    }
    return render(request, "bookapp/books.html", context)

def undefined(request):
    return render(request, "bookapp/404.html")
