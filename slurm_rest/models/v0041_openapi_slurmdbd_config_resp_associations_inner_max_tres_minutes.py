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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from slurm_rest.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_min_tres_per import V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMinTresPer
from slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner import V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner
from typing import Optional, Set
from typing_extensions import Self

class V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes(BaseModel):
    """
    V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes
    """ # noqa: E501
    total: Optional[List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]] = None
    per: Optional[V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMinTresPer] = None
    __properties: ClassVar[List[str]] = ["total", "per"]

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
        """Create an instance of V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in total (list)
        _items = []
        if self.total:
            for _item_total in self.total:
                if _item_total:
                    _items.append(_item_total.to_dict())
            _dict['total'] = _items
        # override the default output from pydantic by calling `to_dict()` of per
        if self.per:
            _dict['per'] = self.per.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxTresMinutes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "total": [V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.from_dict(_item) for _item in obj["total"]] if obj.get("total") is not None else None,
            "per": V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMinTresPer.from_dict(obj["per"]) if obj.get("per") is not None else None
        })
        return _obj


