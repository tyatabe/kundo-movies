from django.shortcuts import render
import requests
from .forms import SearchForm


def search_movies(request):
    results = []
    total_results = 0
    query = request.GET.get("query", "")  # Get the search query from the request
    page = int(request.GET.get("page", 1))  # Default page value is 1

    if query:  # Only make the API call if there's a query
        response = requests.get(
            "http://localhost:4000/v1/search",
            json={"query": query, "page": page},
            headers={
                "api-key": "e4d6d01e-c849-4f54-9a68-7e8fd44cf3ce"  # TODO: make it work with config.settings.API_KEY
            },
        )
        if response.status_code == 200:
            data = response.json()
            results = data.get("search_results", [])
            total_results = data.get("total_results", 0)

    # Initialize the form with the search query
    form = SearchForm(initial={"query": query})

    # Calculate total pages based on total_results and results per page (assume 10 per page)
    results_per_page = 10
    total_pages = (
        total_results + results_per_page - 1
    ) // results_per_page  # Ceiling division

    context = {
        "form": form,
        "results": results,
        "total_results": total_results,
        "query": query,
        "page": page,
        "total_pages": total_pages,
    }

    return render(request, "search/search.html", context)
