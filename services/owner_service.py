from dtos.owners_dtos import NewOwnerRequestDTO, NewOwnerResponseDTO
from models.owner import Owner, create_owner


def add_owner(owner_data: NewOwnerRequestDTO):
    owner = Owner(
        full_name=owner_data.full_name,
        document_number=owner_data.document_number)
    create_owner(owner)
    for c in owner_data.cars:
        owner.add_car(c)

    r = NewOwnerResponseDTO(
        id=owner.id,
        full_name=owner.full_name,
        document_number=owner.document_number,
        is_sale_oportunity=owner.is_sale_oportunity,
        cars=[c.serialize() for c in owner.cars]
    )
    return r


