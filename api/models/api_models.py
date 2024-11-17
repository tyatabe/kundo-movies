from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
    user_id: str = Field(
        default="some-id",
        description="An UUID string unique to a user",
        max_length=36,
        examples=["2609fc89-5bed-48e9-aa36-aacb1b5463d4"],
    )
    query_id: str = Field(
        default="some-id",
        description="An UUID string unique to a query",
        max_length=36,
        examples=["90ab2e9b-f113-4873-9f73-8ff9689acc35"],
    )
    query: str = Field(
        default=None,
        description="A string representing the search query",
        max_length=100,
        examples=["Blade Runner"],
    )
    page: int = Field(
        default=1,
        description="An integer representing the page number of the search results",
        ge=1,
        examples=[1],
    )

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "2609fc89-5bed-48e9-aa36-aacb1b5463d4",
                "query_id": "90ab2e9b-f113-4873-9f73-8ff9689acc35",
                "query": "Blade Runner",
                "page": 1,
            }
        }


class SearchResponse(BaseModel):
    user_id: str = Field(
        default=None,
        description="An UUID string unique to a user",
        max_length=36,
        examples=["2609fc89-5bed-48e9-aa36-aacb1b5463d4"],
    )
    query_id: str = Field(
        default=None,
        description="An UUID string unique to a query",
        max_length=36,
        examples=["90ab2e9b-f113-4873-9f73-8ff9689acc35"],
    )
    query: str = Field(
        default=None,
        description="A string representing the search query",
        max_length=100,
        examples=["Blade Runner"],
    )
    page: int = Field(
        default=1,
        description="An integer representing the page number of the search results",
        ge=1,
        examples=[1],
    )
    total_results: int = Field(
        default=0,
        description="An integer representing the total number of search results",
        ge=0,
        examples=[1],
    )
    search_results: list = Field(
        default=[],
        description="A list of dictionaries containing details of the search results",
        examples=[
            [
                {
                    "Title": "Blade Runner",
                    "Year": "1982",
                    "Plot": "A blade runner must pursue and terminate four replicants who stole a ship in space and "
                    "have returned to Earth to find their creator.",
                    "Poster": "https://m.media-amazon.com/images/M"
                    "/MV5BOWQ4YTBmNTQtMDYxMC00NGFjLTkwOGQtNzdhNmY1Nzc1MzUxXkEyXkFqcGc@._V1_SX300.jpg",
                    "Ratings": [
                        {"Source": "Internet Movie Database", "Value": "8.1/10"},
                        {"Source": "Rotten Tomatoes", "Value": "89%"},
                        {"Source": "Metacritic", "Value": "84/100"},
                    ],
                    "Response": "True",
                }
            ]
        ],
    )

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "2609fc89-5bed-48e9-aa36-aacb1b5463d4",
                "query_id": "90ab2e9b-f113-4873-9f73-8ff9689acc35",
                "query": "Blade Runner",
                "page": 1,
                "total_results": 1,
                "search_results": [
                    {
                        "Title": "Blade Runner",
                        "Year": "1982",
                        "Plot": "A blade runner must pursue and terminate four replicants who stole a ship in space "
                        "and have returned to Earth to find their creator.",
                        "Poster": "https://m.media-amazon.com/images/M"
                        "/MV5BOWQ4YTBmNTQtMDYxMC00NGFjLTkwOGQtNzdhNmY1Nzc1MzUxXkEyXkFqcGc@._V1_SX300.jpg",
                        "Ratings": [
                            {"Source": "Internet Movie Database", "Value": "8.1/10"},
                            {"Source": "Rotten Tomatoes", "Value": "89%"},
                            {"Source": "Metacritic", "Value": "84/100"},
                        ],
                        "Response": "True",
                    }
                ],
            }
        }
