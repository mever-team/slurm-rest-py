# coding: utf-8

"""
    Slurm REST API

    API to access and control Slurm

    The version of the OpenAPI document: Slurm-24.05.2&openapi/slurmdbd&openapi/v0.0.39&openapi/dbv0.0.39&openapi/slurmctld
    Contact: sales@schedmd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from slurm_rest.models.dbv0039_error import Dbv0039Error
from slurm_rest.models.dbv0039_meta import Dbv0039Meta
from slurm_rest.models.dbv0039_warning import Dbv0039Warning
from slurm_rest.models.v0039_user import V0039User
from typing import Optional, Set
from typing_extensions import Self

class Dbv0039UserInfo(BaseModel):
    """
    Dbv0039UserInfo
    """ # noqa: E501
    meta: Optional[Dbv0039Meta] = None
    errors: Optional[List[Dbv0039Error]] = Field(default=None, description="Slurm errors")
    warnings: Optional[List[Dbv0039Warning]] = Field(default=None, description="Slurm warnings")
    users: Optional[List[V0039User]] = None
    __properties: ClassVar[List[str]] = ["meta", "errors", "warnings", "users"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Dbv0039UserInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict['meta'] = self.meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item_errors in self.errors:
                if _item_errors:
                    _items.append(_item_errors.to_dict())
            _dict['errors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in warnings (list)
        _items = []
        if self.warnings:
            for _item_warnings in self.warnings:
                if _item_warnings:
                    _items.append(_item_warnings.to_dict())
            _dict['warnings'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in users (list)
        _items = []
        if self.users:
            for _item_users in self.users:
                if _item_users:
                    _items.append(_item_users.to_dict())
            _dict['users'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Dbv0039UserInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "meta": Dbv0039Meta.from_dict(obj["meta"]) if obj.get("meta") is not None else None,
            "errors": [Dbv0039Error.from_dict(_item) for _item in obj["errors"]] if obj.get("errors") is not None else None,
            "warnings": [Dbv0039Warning.from_dict(_item) for _item in obj["warnings"]] if obj.get("warnings") is not None else None,
            "users": [V0039User.from_dict(_item) for _item in obj["users"]] if obj.get("users") is not None else None
        })
        return _obj


