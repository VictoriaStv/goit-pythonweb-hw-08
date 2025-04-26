from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src import schemas, crud
from src.database import SessionLocal
from src.models import Contact

router = APIRouter(prefix="/contacts", tags=["Contacts"])

# Dependency для сесії БД
async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/", response_model=schemas.ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(contact: schemas.ContactCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_contact(db, contact)

@router.get("/", response_model=List[schemas.ContactResponse])
async def get_contacts(db: AsyncSession = Depends(get_db)):
    return await crud.get_contacts(db)

@router.get("/{contact_id}", response_model=schemas.ContactResponse)
async def get_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    contact = await crud.get_contact(db, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@router.put("/{contact_id}", response_model=schemas.ContactResponse)
async def update_contact(contact_id: int, contact_data: schemas.ContactUpdate, db: AsyncSession = Depends(get_db)):
    contact = await crud.update_contact(db, contact_id, contact_data)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    contact = await crud.delete_contact(db, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")

@router.get("/search", response_model=List[schemas.ContactResponse])
async def search(query: str, db: AsyncSession = Depends(get_db)):
    return await crud.search_contacts(db, query)

@router.get("/birthdays", response_model=List[schemas.ContactResponse])
async def upcoming_birthdays(db: AsyncSession = Depends(get_db)):
    return await crud.get_upcoming_birthdays(db)
