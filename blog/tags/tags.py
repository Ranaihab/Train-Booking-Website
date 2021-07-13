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

@register.simple_tag
def tripSeat(trip):
    book = Book.objects.filter(trip = trip.id)
    bookSeats = book.values_list('seatTrain', flat=True)
    seats = []
    i = 1
    while i <= trip.seats:
        if i not in bookSeats:
            seats.append(i)
        i = i+1
    return seats
