from pydantic import BaseModel
from pydantic_core import core_schema

from .checker import is_valid_mime

class MimeStr(str):
    @classmethod
    def __get_pydantic_core_schema__(cls, source, handler):
        return core_schema.no_info_after_validator_function(
            cls.validate,
            core_schema.str_schema(),
        )

    @classmethod
    def validate(cls, value: str) -> str:
        if not isinstance(value, str):
            raise TypeError("string required")

        if not is_valid_mime(value):
            raise ValueError(f"Invalid MIME type: {value}")

        return cls(value)
    
    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        schema = handler(core_schema)
        schema.update(
            format="mime-type",
            examples=["application/json", "text/plain"]
        )
        return schema