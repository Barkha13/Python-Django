from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "Books: ---,{} ----{}".format(self.name, self.desc)

    def __str__(self):
        return "Books: ---,{} ----{}".format(self.name, self.desc)

class Author(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    books = models.ManyToManyField(Book, related_name = "authors")
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "Authors: ---,{} ----{}, ----{}, -----{}".format(self.first_name, self.last_name, self.email, self.notes)

    #to get all the books of author id 3
    #Author.objects.get(id = 3).books.all()

    #to delete the first author of the book id 3
    # b = Book.objects.get(id = 3).authors.first()
    # b.delete()


