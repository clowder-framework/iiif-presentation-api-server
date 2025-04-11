import json
from urllib.parse import urljoin

from fastapi import APIRouter, HTTPException
from fastapi import Request
from iiif_prezi3 import Manifest

from app.core.config import settings

router = APIRouter(prefix="/manifests", tags=["manifests"])


@router.get("/{image_filename_prefix}/manifest.json")
async def read_manifests(image_filename_prefix, request: Request):
    base_url = urljoin(str(request.base_url), settings.API_V1_STR)
    manifest = Manifest(id=f"{base_url}/manifest.json",
                        label={"en": ["A whole-slide microscopy image."]},
                        behavior="individuals")
    # TODO: See if there is a way to generalize this endpoint. Currently, this is tied to the ncsa.file.czi extractor.
    try:
        canvas_1 = manifest.make_canvas_from_iiif(
            url=f"{settings.IIIF_IMAGE_API_SERVER_URL}/{image_filename_prefix}{settings.x_pol_postfix}/info.json",
            id=f"{base_url}/canvas/p1",
            label={"en": ["A whole-slide microscopy image. Cross Polarized"]},
        )

        canvas_2 = manifest.make_canvas_from_iiif(
            url=f"{settings.IIIF_IMAGE_API_SERVER_URL}/{image_filename_prefix}{settings.p_pol_postfix}/info.json",
            id=f"{base_url}/canvas/p2",
            label={"en": ["A whole-slide microscopy image. P Polarized"]},
        )
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    return json.loads(manifest.json(indent=2))
