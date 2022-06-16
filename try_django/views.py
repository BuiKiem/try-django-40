"""Render HTML webpages"""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def home_view(request: HttpRequest) -> HttpResponse:
    """
    Take in a request (Django sends request)
    Return HTML as a response
    """
    return render(request, "index.html")
