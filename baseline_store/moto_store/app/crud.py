from sqlalchemy.orm import Session
from . import models, schemas

def create_car(db: Session, car: schemas.CarCreate):
    db_car = models.Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def create_motorcycle(db: Session, motorcycle: schemas.MotorcycleCreate):
    db_motorcycle = models.Motorcycle(**motorcycle.dict())
    db.add(db_motorcycle)
    db.commit()
    db.refresh(db_motorcycle)
    return db_motorcycle

def get_cars(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Car).offset(skip).limit(limit).all()

def get_motorcycles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Motorcycle).offset(skip).limit(limit).all()

def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_clients(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Client).offset(skip).limit(limit).all()

def create_sale(db: Session, sale: schemas.SaleCreate):
    db_sale = models.Sale(**sale.dict())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

def get_sales(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Sale).offset(skip).limit(limit).all()
