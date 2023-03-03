from dataclasses import dataclass
from typing import Dict, List
from dataclasses_json import dataclass_json
from dtos.cars_dtos import NewCarDTO


@dataclass_json
@dataclass
class NewOwnerRequestDTO:
    full_name: str
    document_number: str
    cars: List[NewCarDTO]


@dataclass_json
@dataclass
class NewOwnerResponseDTO:
    id: str
    full_name: str
    document_number: str
    is_sale_oportunity: bool
    cars: List[Dict]