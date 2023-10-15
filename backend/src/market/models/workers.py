from typing import Optional

from pydantic import BaseModel


class WorkerBase(BaseModel):
    pass


class Worker(WorkerBase):
    id: int
    user_id: int
    main_category: Optional[int]
    category_name: Optional[str] = None
    photo: Optional[str]
    name: str
    surname: str
