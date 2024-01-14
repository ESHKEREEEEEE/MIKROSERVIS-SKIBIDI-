from uuid import UUID

from typing import Any, List, Dict

from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status


from app import crud as crud
from app import models, schemas
from app.routers import deps

router = APIRouter()


@router.post(
    "/", response_model=schemas.RequestCreate, status_code=status.HTTP_201_CREATED
)
def create_request(
    *, request: schemas.RequestCreate, db: Session = Depends(deps.get_db)
) -> Any:
    try:
        db_obj = crud.request.create(db, obj_in=request)
        return db_obj
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.get("/", response_model=List[schemas.Request])
def get_requests(
    db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 10
):  # skip=0,limit=10 == 1-10 записи
    requests = crud.request.get_multi(db, skip=skip, limit=limit)  #
    return requests


@router.get("/{request_id}", response_model=schemas.Request)
def get_request_by_id(request_id: UUID, db: Session = Depends(deps.get_db)):
    request = crud.request.get(db, sid=request_id)
    if request is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Request not found"
        )
    return request


@router.put("/{request_id}", response_model=schemas.Request)
def update_request_by_id(
    request_id: UUID,
    update_data: schemas.RequestUpdate,
    db: Session = Depends(deps.get_db),
):
    request = crud.request.get(db, sid=request_id)
    if request is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Request not found"
        )
    updated_request = crud.request.update(db, db_obj=request, obj_in=update_data)
    return updated_request
