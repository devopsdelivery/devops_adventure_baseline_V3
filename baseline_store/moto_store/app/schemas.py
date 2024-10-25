from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
import enum

class VehicleTypeEnum(str, enum.Enum):
    car = "car"
    motorcycle = "motorcycle"

class VehicleBase(BaseModel):
    make: str
    model: str
    price: float
    stock: int
    type: VehicleTypeEnum

class CarCreate(VehicleBase):
    doors: int

class Car(VehicleBase):
    id: int
    doors: int

    class Config:
        orm_mode = True

class MotorcycleCreate(VehicleBase):
    engine_capacity: float

class Motorcycle(VehicleBase):
    id: int
    engine_capacity: float

    class Config:
        orm_mode = True

class ClientBase(BaseModel):
    name: str
    email: str
    phone: str
    address: Optional[str] = None

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int
    sales: List[int] = []

    class Config:
        orm_mode = True

class SaleBase(BaseModel):
    client_id: int
    vehicle_id: int
    price: float

class SaleCreate(SaleBase):
    pass

class Sale(SaleBase):
    id: int
    sale_date: datetime

    class Config:
        orm_mode = True
