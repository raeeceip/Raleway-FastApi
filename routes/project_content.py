from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from datetime import datetime
from typing import List
from ..schemas import BlogContent, BlogContentResponse, db
from .. import oauth2


router= APIRouter(
    prefix="/project",
    tags=["Project Content"]

)

@router.post("/", response_description="Create Project Content", response_model=BlogContentResponse)
def create_project():
    # each post request creates a json file 
    # with the name of the project
    pass


@router.get("/{id}", response_description="Get Project Post", response_model= BlogContentResponse)
def get_project_post(id: str):
    # get the project post by id
    # return the project post
    return 





@router.get("/", response_description="Get Project Posts", response_model= List[BlogContentResponse])
def get_project_posts():
    # get all the project posts
    # return the project posts
    return  
    