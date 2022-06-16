"""Render HTML webpages"""
from django.http import HttpRequest, HttpResponse

def home_view(request: HttpRequest) -> HttpResponse:
    """
    Take in a request (Django sends request)
    Return HTML as a response
    """
    name = "Justin"
    HTML_STRING = f"<h1>Hello {name}</h1>"
    return HttpResponse(HTML_STRING)
