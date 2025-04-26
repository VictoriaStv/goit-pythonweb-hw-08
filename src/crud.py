from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import or_, extract
from datetime import datetime, timedelta

from src.models import Contact


# Пошук за ім'ям, прізвищем або email
async def search_contacts(db: AsyncSession, query: str):
    result = await db.execute(
        select(Contact).filter(
            or_(
                Contact.first_name.ilike(f"%{query}%"),
                Contact.last_name.ilike(f"%{query}%"),
                Contact.email.ilike(f"%{query}%")
            )
        )
    )
    return result.scalars().all()

# Дні народження протягом 7 днів
async def get_upcoming_birthdays(db: AsyncSession):
    today = datetime.today().date()
    next_week = today + timedelta(days=7)

    result = await db.execute(
        select(Contact).filter(
            extract('month', Contact.birthday) == today.month,
            extract('day', Contact.birthday) >= today.day,
            extract('day', Contact.birthday) <= next_week.day
        )
    )
    return result.scalars().all()
