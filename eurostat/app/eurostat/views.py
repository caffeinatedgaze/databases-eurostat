from rest_framework.decorators import api_view
from django.shortcuts import render

from .db import run_query


QUERY_PARAMS_MAP = {
    1: ('from_year', 'to_year'),
    2: ('limit', ),
    3: ('year', 'quarter'),
    4: ('from_year', 'to_year'),
    5: ('limit', ),
    6: ('year', ),
    7: ('from_year', 'to_year'),
    8: ('limit', ),
    9: ('year', 'quarter'),
}


@api_view(['GET'])
def main_view(request):
    return render(request, 'main.html')

@api_view(['GET', 'POST'])
def query_view(request, num):
    if request.method == 'GET':
        return render(request, f'query_{num}.html')
    else:
        return render(
            request,
            f'result_{num}.html',
            context={
                'result': run_query(num, *[int(request.data[param]) for param in QUERY_PARAMS_MAP[num]])
            }
        )
