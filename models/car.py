import enum
import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, Enum

from app.app import db


class CarColors(enum.Enum):
    YELLOW = 0
    BLUE = 1
    GRAY = 2

    @classmethod
    def value_of(cls, value):
        for k, v in cls.__members__.items():
            if k == value:
                return v
        else:
            raise ValueError(f"'{cls.__name__}' enum not found for '{value}'")


class CarModels(enum.Enum):
    HATCH = 0
    SEDAN = 1
    CONVERTIBLE = 2


    @classmethod
    def value_of(cls, value):
        for k, v in cls.__members__.items():
            if k == value:
                return v
        else:
            raise ValueError(f"'{cls.__name__}' enum not found for '{value}'")


class Car(db.Model):
    __tablename__ = 'cars'

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    commercial_name = db.Column(
        String(70),
        nullable=False
    )

    owner_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey('owners.id'),
        nullable=False
    )

    color = db.Column(Enum(CarColors), nullable=False)
    model = db.Column(Enum(CarModels), nullable=False)

    def serialize(self):
        return {
            'id': self.id.__str__(), 
            'commercial_name': self.commercial_name,
            'color': self.color.__str__(),
            'model': self.model.__str__(),
            'owner_id': self.owner_id.__str__()
        }
         

def create_car(car: Car):
    db.session.add(car)
    db.session.commit()