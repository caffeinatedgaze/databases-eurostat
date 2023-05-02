from rest_framework.decorators import api_view
from django.shortcuts import render

from .db import get_db_connector, get_query


@api_view(['GET'])
def main_view(request):
    return render(request, 'main.html')

@api_view(['GET', 'POST'])
def query_view(request, num):
    if request.method == 'GET':
        return render(request, f'query_{num}.html')
    else:
        db = get_db_connector()
        quary = get_query(num)
        data = request.data
        result = db.execute(quary, data)
        return render(request, f'result_{num}.html', context={'result': result})
