from api.api_be.processor import process_search_request
from api.models.api_models import SearchRequest, SearchResponse
from fastapi import APIRouter, HTTPException, Security, Depends
from fastapi.security.api_key import APIKeyHeader
from starlette.status import HTTP_401_UNAUTHORIZED
from api.config import settings

router = APIRouter()
api_keys = settings.API_KEY
api_key_header = APIKeyHeader(name="api-key", auto_error=False)

# TODO: add logger


async def api_key_auth(api_key: str = Security(api_key_header)):
    if api_key is None or api_key not in api_keys or api_keys is None:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )
    return None


@router.get("/search", response_model=SearchResponse, tags=["search"])
async def search(search_request: SearchRequest, api_key: str = Depends(api_key_auth)):
    """
    Search for movies using the OMDB API
    """
    return await process_search_request(search_request)
