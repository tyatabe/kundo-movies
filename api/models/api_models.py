from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
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
        max_length=300,
        examples=["Blade Runner"],
    )

    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "2609fc89-5bed-48e9-aa36-aacb1b5463d4",
                "query_id": "90ab2e9b-f113-4873-9f73-8ff9689acc35",
                "query": "Blade Runner",
            }
        }
