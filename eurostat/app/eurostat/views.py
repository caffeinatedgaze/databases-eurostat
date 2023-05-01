from rest_framework.decorators import api_view
from django.shortcuts import render


@api_view(['GET'])
def main_view(request):
    return render(request, 'main.html')

@api_view(['GET'])
def query_view(request, num):
    return render(request, f'query_{num}.html')
