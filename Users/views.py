from django.shortcuts import render

# Create your views here.


class ModelCreateView(CreateView):
    model = Model
    template_name = ".html"
