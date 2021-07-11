from blog.models import Book
from django.template.loader import get_template
from django import template

register = template.Library()


@register.simple_tag
def books(username):
    book = Book.objects.filter(user = username)
    return book

@register.simple_tag
def bookSeat(book):
    seats = book.seatTrain.all()
    return seats

@register.simple_tag
def bookPrice(book):
    count = book.seatTrain.count()
    price = count * book.trip.price
    return price
