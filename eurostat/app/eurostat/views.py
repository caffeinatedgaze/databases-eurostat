from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from .db import (
    run_query,
    search_housing,
    search_consumer,
    search_job,
    details_housing,
    details_consumer,
    details_job
)

QUERY_PARAMS_MAP = {
    1: ("from_year", "to_year"),
    2: ("limit",),
    3: ("year", "quarter"),
    4: ("from_year", "to_year"),
    5: ("limit",),
    6: ("year",),
    7: ("from_year", "to_year"),
    8: ("limit",),
    9: ("year", "quarter"),
}

QUERY_TABLES_MAP = {
    "housing": details_housing,
    "consumer": details_consumer,
    "job": details_job,
}


@api_view(["GET"])
def main_view(request):
    return render(request, "main.html")


@api_view(["GET", "POST"])
def query_view(request, num):
    if request.method == "GET":
        return render(request, f"query_{num}.html")
    else:
        return render(
            request,
            f"result_{num}.html",
            context={
                "result": run_query(
                    num, *[int(request.data[param]) for param in QUERY_PARAMS_MAP[num]]
                )
            },
        )


@api_view(["GET"])
def search(request: HttpRequest):
    q = request.GET.get("q", "")
    table = request.GET.get("table", "")

    if not q or not table:
        return JsonResponse(
            {"detail": "Specify q and table query parameters"},
            status=400,
        )

    if table == "housing":
        result = search_housing(q)
    elif table == "consumer":
        result = search_consumer(q)
    elif table == "job":
        result = search_job(q)
    else:
        return JsonResponse(
            {
                "detail": f"No such table: {table}. Choose either housing, consumer, or job"
            },
            status=400,
        )

    return JsonResponse(
        result,
        safe=False,
    )



@api_view(["GET"])
def detail_view(request, table, num):
    
    table_query = QUERY_TABLES_MAP.get(table)

    if table_query is None:
        return JsonResponse(
            {
                "detail": f"No such table: {table}. Choose either housing, consumer, or job"
            },
            status=404,
        )

    return JsonResponse(
        table_query(num),
        safe=False,
    )
