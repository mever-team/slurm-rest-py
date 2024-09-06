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
from slurm_rest.models.v0041_openapi_slurmdbd_stats_resp_statistics_rollups_daily import V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDaily
from slurm_rest.models.v0041_openapi_slurmdbd_stats_resp_statistics_rollups_hourly import V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly
from slurm_rest.models.v0041_openapi_slurmdbd_stats_resp_statistics_rollups_monthly import V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthly
from typing import Optional, Set
from typing_extensions import Self

class V0041OpenapiSlurmdbdStatsRespStatisticsRollups(BaseModel):
    """
    V0041OpenapiSlurmdbdStatsRespStatisticsRollups
    """ # noqa: E501
    hourly: Optional[V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly] = None
    daily: Optional[V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDaily] = None
    monthly: Optional[V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthly] = None
    __properties: ClassVar[List[str]] = ["hourly", "daily", "monthly"]

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
        """Create an instance of V0041OpenapiSlurmdbdStatsRespStatisticsRollups from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of hourly
        if self.hourly:
            _dict['hourly'] = self.hourly.to_dict()
        # override the default output from pydantic by calling `to_dict()` of daily
        if self.daily:
            _dict['daily'] = self.daily.to_dict()
        # override the default output from pydantic by calling `to_dict()` of monthly
        if self.monthly:
            _dict['monthly'] = self.monthly.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0041OpenapiSlurmdbdStatsRespStatisticsRollups from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hourly": V0041OpenapiSlurmdbdStatsRespStatisticsRollupsHourly.from_dict(obj["hourly"]) if obj.get("hourly") is not None else None,
            "daily": V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDaily.from_dict(obj["daily"]) if obj.get("daily") is not None else None,
            "monthly": V0041OpenapiSlurmdbdStatsRespStatisticsRollupsMonthly.from_dict(obj["monthly"]) if obj.get("monthly") is not None else None
        })
        return _obj

