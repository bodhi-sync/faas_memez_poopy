from typing import Dict

from fastapi import HTTPException
from pydantic import BaseModel

FUNCTION_NAME = 'templatefn'
FUNCTION_VERSION = '1.0.0'
FUNCTION_SUMMARY = "A function that does this"
FUNCTION_RESPONSE_DESC = "Definition of object returned by function"


class RequestModel(BaseModel):
    data: Dict


class ResponseModel(BaseModel):
    data: Dict


def logic(req: RequestModel) -> ResponseModel:
    try:
        res = ResponseModel(data=req.data)
    except Exception:
        raise HTTPException(status_code=500, detail=f"An API Error occurred")
    return res


async def logic_async(req: RequestModel) -> ResponseModel:
    try:
        res = ResponseModel(data=req.data)
    except Exception:
        raise HTTPException(status_code=500, detail=f"An API Error occurred")
    return res


def handle(req):
    """handle a request to the function
    Args:
        req (dict): request body
    """
    return logic(req)


async def handle_async(req):
    """handle a request to the function
    Args:
        req (dict): request body
    """
    return await logic_async(req)


async def handle_async_stream(req):
    """handle a request to the function asynchronously and with a stream.
    
    We assume to use async for this for all other IO.
    Args:
        req (dict): request body
    """
    yield await logic_async(req)
