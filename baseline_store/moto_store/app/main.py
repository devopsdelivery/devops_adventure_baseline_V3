from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, Base, get_db

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

@app.post("/cars/", response_model=schemas.Car)
def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)):
    return crud.create_car(db=db, car=car)

@app.post("/motorcycles/", response_model=schemas.Motorcycle)
def create_motorcycle(motorcycle: schemas.MotorcycleCreate, db: Session = Depends(get_db)):
    return crud.create_motorcycle(db=db, motorcycle=motorcycle)

@app.get("/cars/", response_model=list[schemas.Car])
def read_cars(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_cars(db=db, skip=skip, limit=limit)

@app.get("/motorcycles/", response_model=list[schemas.Motorcycle])
def read_motorcycles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_motorcycles(db=db, skip=skip, limit=limit)

@app.post("/clients/", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    return crud.create_client(db=db, client=client)

@app.get("/clients/", response_model=list[schemas.Client])
def read_clients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_clients(db=db, skip=skip, limit=limit)

@app.post("/sales/", response_model=schemas.Sale)
def create_sale(sale: schemas.SaleCreate, db: Session = Depends(get_db)):
    return crud.create_sale(db=db, sale=sale)

@app.get("/sales/", response_model=list[schemas.Sale])
def read_sales(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_sales(db=db, skip=skip, limit=limit)
