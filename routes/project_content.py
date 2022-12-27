from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from datetime import datetime
from typing import List
from pydantic import BaseModel
import json 





# get projects.json file from  routes folder 


router= APIRouter(
    prefix="/project",
    tags=["Project Content"]

)

@router.get("/", response_description="Get Projects")
async def get_project_content():
    # if response is good return data 
    try:
        with open("routes/projects.json", "r") as f:
            data = json.load(f)
            return data
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})

@router.get("/in_progress", response_description="Get Projects in progress")
async def get_project_content_in_progress():
    # if response is good return data
    try:
        with open("routes/projects.json", "r") as f:
            data = json.load(f)
            return [project for project in data if project["in_progress"]]
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})

@router.get("/completed", response_description="Get Projects completed")
async def get_project_content_completed():
    # if response is good return data
    try:
        with open("routes/projects.json", "r") as f:
            data = json.load(f)
            return [project for project in data if project["completed"]]
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})

# add route to add new project to projects.json
