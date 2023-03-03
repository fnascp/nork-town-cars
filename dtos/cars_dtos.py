from dataclasses import dataclass
from dataclasses_json import dataclass_json

from models.car import Car


@dataclass_json
@dataclass
class NewCarDTO:
    commercial_name: str
    model: str
    color: str


@dataclass_json
@dataclass
class CarInOwnerListDTO:
    id: str
    commercial_name: str
    color: str
    model: str

    def __init__(self, car: Car):
        self.id = car.id.__str__()
        self.commercial_name = car.commercial_name
        self.color = car.color.__str__()
        self.model = car.color.__str__()


