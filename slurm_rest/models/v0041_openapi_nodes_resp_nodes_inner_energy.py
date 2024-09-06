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

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id import V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId
from typing import Optional, Set
from typing_extensions import Self

class V0041OpenapiNodesRespNodesInnerEnergy(BaseModel):
    """
    V0041OpenapiNodesRespNodesInnerEnergy
    """ # noqa: E501
    average_watts: Optional[StrictInt] = None
    base_consumed_energy: Optional[StrictInt] = None
    consumed_energy: Optional[StrictInt] = None
    current_watts: Optional[V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId] = None
    previous_consumed_energy: Optional[StrictInt] = None
    last_collected: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["average_watts", "base_consumed_energy", "consumed_energy", "current_watts", "previous_consumed_energy", "last_collected"]

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
        """Create an instance of V0041OpenapiNodesRespNodesInnerEnergy from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of current_watts
        if self.current_watts:
            _dict['current_watts'] = self.current_watts.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0041OpenapiNodesRespNodesInnerEnergy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "average_watts": obj.get("average_watts"),
            "base_consumed_energy": obj.get("base_consumed_energy"),
            "consumed_energy": obj.get("consumed_energy"),
            "current_watts": V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId.from_dict(obj["current_watts"]) if obj.get("current_watts") is not None else None,
            "previous_consumed_energy": obj.get("previous_consumed_energy"),
            "last_collected": obj.get("last_collected")
        })
        return _obj


