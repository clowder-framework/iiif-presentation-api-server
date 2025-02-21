import json
from urllib.parse import urljoin

from fastapi import APIRouter, HTTPException
from fastapi import Request
from iiif_prezi3 import Manifest

from app.core.config import settings

router = APIRouter(prefix="/manifests", tags=["manifests"])


@router.get("/{image_filename}/manifest.json")
async def read_manifests(image_filename, request: Request):
    base_url = urljoin(str(request.base_url), settings.API_V1_STR)
    manifest = Manifest(id=f"{base_url}/manifest.json",
                        label={"en": ["A whole-slide microscopy image."]})
    try:
        manifest.make_canvas_from_iiif(
            url=f"{settings.IIIF_IMAGE_API_SERVER_URL}/{image_filename}/info.json",
            id=f"{base_url}/canvas/p1")
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    return json.loads(manifest.json(indent=2))
