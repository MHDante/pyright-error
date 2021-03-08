from typing import Union
from typing_extensions import Annotated, get_origin
assert get_origin(Union[int, str]) is Union
assert get_origin(Annotated[int, "cheem"]) is Annotated
