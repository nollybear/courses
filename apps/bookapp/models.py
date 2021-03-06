from __future__ import unicode_literals
from django.db import models
import re, bcrypt
from bcrypt import hashpw
from itertools import count


class UserManager(models.Manager):
    def register(self, first_name, last_name, email, password, confirm):
        errors = []
        EMAIL_REGEX = (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(first_name) <= 2:
            errors.append("A first name with at least two character is required")
        if len(last_name) <= 2:
            errors.append("A last name with at least two character is required")
        if len(password) == 0:
            errors.append("Password is required")
        elif password != confirm:
            errors.append("Password and confrimation must match")
        if len(email) == 0:
            errors.append("Email is required")
        elif not re.match(EMAIL_REGEX, email):
            errors.append("Valid email is required")
        if len(errors) is not 0:
            return (False, errors)
        else:
            hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            Users = User.objects.create(first_name = first_name, last_name = last_name, email = email, password = hashed)
            return True

    def login(self, email, password):
            errors = []
            print "this is the login function in the class", email
            print "this is the login function in the class", password
            if User.objects.filter(email=email):
                user = User.objects.filter(email=email)[0]
                print "PRINT USER IN LOGIN METHOD", user
                hashed = user.password
                if bcrypt.hashpw(password.encode(), hashed.encode()) == hashed:
                    loggedin = "Successfully created new user"
                    return True
                else:
                    errors.append("Invalid password for this email")
                    return (False, errors)
            else:
                errors.append("Invalid login credentials")
                return (False, errors)

class User(models.Model):
    first_name = models.CharField(max_length=45, default='null')
    last_name = models.CharField(max_length=45, default='null')
    email = models.CharField(max_length=45, default='null')
    password = models.CharField(max_length=255, default='null')
    created_at = models.DateTimeField(auto_now_add = True)
    objects = UserManager()


class BookManager(models.Manager):
    def addbook(self, title, author):
        errors = []
        newbook = ""
        if len(title) <= 2:
            errors.append("A book needs to have at least two character is required")
        if len(author) <= 2:
            errors.append("An author's name needs to have at least two character is required")
        if len(errors) is not 0:
            return (False, errors)
        else:
            Books = Book.objects.create(title = title, author = author)
            newbook = "Successfully created new book"
            return (True, newbook)

class Book(models.Model):
    title = models.CharField(max_length=45, default='null')
    author = models.CharField(max_length=45, default='null')
    created_at = models.DateTimeField(auto_now_add = True)
    objects = BookManager()

class ReviewManager(models.Manager):
    def addbook(self, user, book, review, rating):
        Reviews = Review.objects.create(user = user, book = book, review = review, rating = rating)
        return True

class Review(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    review = models.CharField(max_length=255, default='null')
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    objects = ReviewManager()
