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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from slurm_rest.models.v0041_openapi_slurmdbd_stats_resp_statistics_rollups_hourly_duration import V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourlyDuration
from typing import Optional, Set
from typing_extensions import Self

class V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly(BaseModel):
    """
    V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly
    """ # noqa: E501
    count: Optional[StrictInt] = Field(default=None, description="number of hourly rollups since last_run")
    last_run: Optional[StrictInt] = Field(default=None, description="Last time hourly rollup ran (UNIX timestamp)")
    duration: Optional[V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourlyDuration] = None
    __properties: ClassVar[List[str]] = ["count", "last_run", "duration"]

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
        """Create an instance of V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of duration
        if self.duration:
            _dict['duration'] = self.duration.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "count": obj.get("count"),
            "last_run": obj.get("last_run"),
            "duration": V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourlyDuration.from_dict(obj["duration"]) if obj.get("duration") is not None else None
        })
        return _obj


