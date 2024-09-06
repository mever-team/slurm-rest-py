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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from slurm_rest.models.v0039_error import V0039Error
from slurm_rest.models.v0039_meta import V0039Meta
from slurm_rest.models.v0039_warning import V0039Warning
from typing import Optional, Set
from typing_extensions import Self

class V0039JobSubmissionResponse(BaseModel):
    """
    V0039JobSubmissionResponse
    """ # noqa: E501
    meta: Optional[V0039Meta] = None
    errors: Optional[List[V0039Error]] = Field(default=None, description="Slurm errors")
    warnings: Optional[List[V0039Warning]] = Field(default=None, description="Slurm warnings")
    job_id: Optional[StrictInt] = Field(default=None, description="new job ID")
    step_id: Optional[StrictStr] = Field(default=None, description="new job step ID")
    job_submit_user_msg: Optional[StrictStr] = Field(default=None, description="Message to user from job_submit plugin")
    __properties: ClassVar[List[str]] = ["meta", "errors", "warnings", "job_id", "step_id", "job_submit_user_msg"]

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
        """Create an instance of V0039JobSubmissionResponse from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0039JobSubmissionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "meta": V0039Meta.from_dict(obj["meta"]) if obj.get("meta") is not None else None,
            "errors": [V0039Error.from_dict(_item) for _item in obj["errors"]] if obj.get("errors") is not None else None,
            "warnings": [V0039Warning.from_dict(_item) for _item in obj["warnings"]] if obj.get("warnings") is not None else None,
            "job_id": obj.get("job_id"),
            "step_id": obj.get("step_id"),
            "job_submit_user_msg": obj.get("job_submit_user_msg")
        })
        return _obj


