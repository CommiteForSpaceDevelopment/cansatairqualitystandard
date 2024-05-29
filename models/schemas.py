from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func
from sqlalchemy import Sequence

Base = declarative_base()

class Measurement(Base):
    __tablename__ = 'measurements'

    id = Column(Integer,Sequence('measurements_id_seq'), primary_key=True)
    temperature = Column(Float)
    humidity = Column(Float)
    co2 = Column(Float)
    timestamp = Column(String(50), default=func.now())

    location_id = Column(Integer, ForeignKey('locations.id'))
    location = relationship("Location", back_populates="measurements")
    


class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer,Sequence('location_id_seq'), primary_key=True)
    gps_location = Column(String(50))
    location_name = Column(String(100))
    location_description = Column(String(200))
    password=Column(String(100))
    username=Column(String(100))
    measurements = relationship("Measurement", back_populates="location")