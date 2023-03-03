from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class LoginRequestDTO:
    email: str
    password: str


@dataclass_json
@dataclass
class RegisterRequestDTO:
    email: str
    full_name: str
    password: str


@dataclass_json
@dataclass
class RegisterResponseDTO:
    id: str
    email: str
    full_name: str
