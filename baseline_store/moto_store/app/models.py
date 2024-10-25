from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from .database import Base
import enum
from datetime import datetime

class VehicleType(enum.Enum):
    CAR = "car"
    MOTORCYCLE = "motorcycle"

class Vehicle(Base):
    __tablename__ = "vehicles"
    
    id = Column(Integer, primary_key=True, index=True)
    type = Column(Enum(VehicleType), nullable=False)
    make = Column(String, index=True)
    model = Column(String, index=True)
    price = Column(Float)
    stock = Column(Integer, default=0)
    
    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "vehicle",
    }

class Car(Vehicle):
    __tablename__ = "cars"
    id = Column(Integer, ForeignKey("vehicles.id"), primary_key=True)
    doors = Column(Integer)  # Number of doors, specific to cars
    
    __mapper_args__ = {
        "polymorphic_identity": VehicleType.CAR,
    }

class Motorcycle(Vehicle):
    __tablename__ = "motorcycles"
    id = Column(Integer, ForeignKey("vehicles.id"), primary_key=True)
    engine_capacity = Column(Float)  # Engine capacity in CC, specific to motorcycles

    __mapper_args__ = {
        "polymorphic_identity": VehicleType.MOTORCYCLE,
    }

class Client(Base):
    __tablename__ = "clients"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, index=True)
    address = Column(String)
    
    sales = relationship("Sale", back_populates="client")

class Sale(Base):
    __tablename__ = "sales"
    
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    sale_date = Column(DateTime, default=datetime.utcnow)
    price = Column(Float)
    
    client = relationship("Client", back_populates="sales")
    vehicle = relationship("Vehicle")
