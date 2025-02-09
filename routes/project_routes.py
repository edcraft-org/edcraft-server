from fastapi import APIRouter, HTTPException
from typing import List, Optional
from models import Project, ProjectCreate, ProjectTitleUpdate

project_router = APIRouter()


@project_router.post("/", response_model=Project)
async def add_project(project: ProjectCreate):
    new_project = Project(**project.model_dump())
    await new_project.insert()
    return new_project


@project_router.get("/", response_model=List[Project])
async def get_projects(user_id: Optional[str] = None):
    query = {}
    if user_id:
        query['user_id'] = user_id
    projects = await Project.find(query).to_list()
    return projects


@project_router.get("/{project_id}", response_model=Project)
async def get_project(project_id: str):
    project = await Project.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@project_router.delete("/{project_id}", response_model=str)
async def delete_project(project_id: str):
    project = await Project.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    await project.delete()
    return f"Project {project_id} deleted successfully"


@project_router.put("/{project_id}/title", response_model=Project)
async def rename_project_title(project_id: str, title_update: ProjectTitleUpdate):
    project = await Project.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    project.title = title_update.title
    await project.save()
    return project
