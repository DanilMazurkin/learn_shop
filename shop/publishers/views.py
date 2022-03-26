from django.shortcuts import render
from django.views.generic import ListView
from publishers.models import Publisher


class PublisherList(ListView):
    model = Publisher
    paginate_by = 3
