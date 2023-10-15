from uuid import uuid4
from builder.operators import Parameter, Operator, generate_operator, \
    DatumResolvable, StringResolvable


def generate_uuid() -> str:
    return str(uuid4()).upper()


class BadObjectDataError(ValueError):
    pass

