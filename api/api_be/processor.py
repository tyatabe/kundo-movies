import asyncio
from api.models.api_models import SearchRequest, SearchResponse
from api.search_constants import DISPLAY_FIELDS
from api.config import settings
import requests


async def search_omdb(
    search_string: str, page: int = None, search_type: str = None
) -> dict:
    """
    Search the OMDB API for a movie title or IMDb ID
    :param search_string: movie title or IMDb ID
    :param page: page number of search results
    :param search_type: "s" for movie title, "i" for IMDb ID
    :return: dict with search results (list of titles or title details)
    """
    if search_type not in ["s", "i"]:
        raise ValueError("search_type must be 's' (movie title) or 'i' (IMDb ID)")

    params = {
        "apikey": settings.OMDB_API_KEY,
    }
    if search_type == "s":
        params["s"] = search_string
        params["page"] = page
    elif search_type == "i":
        params["i"] = search_string
    response = requests.get(settings.OMDB_URL, params=params)
    return response.json()


async def process_search_request(search_request: SearchRequest) -> SearchResponse:
    """
    Process a search request
    :param search_request: SearchRequest object
    :return: SearchResponse object
    """
    search_string = search_request.query
    page = search_request.page
    search_title_results = await search_omdb(search_string, page, search_type="s")
    if search_title_results["Response"] == "True":
        total_results = int(search_title_results["totalResults"])
        title_ids = [
            title_dict["imdbID"] for title_dict in search_title_results["Search"]
        ]
        title_details = await asyncio.gather(
            *[search_omdb(title_id, search_type="i") for title_id in title_ids]
        )
        title_details_return = []
        for title in title_details:
            title_details_return_dict = {}
            for key in title.keys():
                if DISPLAY_FIELDS.get(key, False):
                    title_details_return_dict[key] = title[key]
            title_details_return.append(title_details_return_dict)
        response = SearchResponse(
            user_id=search_request.user_id,
            query_id=search_request.query_id,
            query=search_request.query,
            page=search_request.page,
            total_results=total_results,
            search_results=title_details_return,
        )
    else:
        response = SearchResponse(
            user_id=search_request.user_id,
            query_id=search_request.query_id,
            query=search_request.query,
            page=search_request.page,
            total_results=0,
            search_results=[],
        )

    return response
