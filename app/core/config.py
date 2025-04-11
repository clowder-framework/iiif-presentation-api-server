from typing import List

from pydantic import AnyHttpUrl, BaseSettings, Field
from pydantic.class_validators import validator


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "iiif-presentation-server"
    CORS_ORIGINS: List[AnyHttpUrl] = Field(default_factory=list)
    IIIF_IMAGE_API_SERVER_URL: str = "http://localhost:8182/iiif/3"
    x_pol_postfix: str = "_x_pol_rgb_lzw_bigtiff.tif"
    p_pol_postfix: str = "_p_pol_rgb_lzw_bigtiff.tif"

    @validator("CORS_ORIGINS", pre=True, always=True)
    def set_cors_origins(cls, v):
        return v or [
            "http://localhost:3000",
            "http://localhost:3001",
            "http://localhost:3002",
            "http://localhost:4444",
        ]


settings = Settings()
