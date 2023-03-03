from typing import List
import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, Boolean
from sqlalchemy.exc import IntegrityError

from app.app import db
from dtos.cars_dtos import NewCarDTO
from exceptions.erros import CarLimitExcededExistsError, OwnerAlreadyExistsError
from models.car import Car, CarModels, CarColors, create_car


class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    document_number = db.Column(String(30), unique=True, nullable=False)
    full_name = db.Column(String(70), index=True, nullable=False)
    is_sale_oportunity = db.Column(Boolean, nullable=False, default=True)
    cars = db.relationship('Car', backref='owners', cascade='delete')

    def add_car(self, car: NewCarDTO):
        if len(self.cars) == 3:
            raise CarLimitExcededExistsError
         
        c = Car(
            commercial_name=car.commercial_name,
            model=CarModels.value_of(car.model),
            color=CarColors.value_of(car.color),
            owner_id=self.id)
        create_car(c)


    @staticmethod
    def get_car_count(owner_id):
        return Car.query.filter_by(owner_id=owner_id).count()
        


def create_owner(owner):
    try:
        db.session.add(owner)
        db.session.commit()
    except IntegrityError:
        raise OwnerAlreadyExistsError


