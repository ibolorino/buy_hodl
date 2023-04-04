from typing import Any
import re

from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        pattern = re.compile(r"(?<!^)(?=[A-Z])")
        table_name = pattern.sub("_", cls.__name__).lower().replace("__", "_")
        return table_name