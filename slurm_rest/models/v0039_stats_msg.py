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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from slurm_rest.models.v0040_stats_msg_rpcs_by_type_inner import V0040StatsMsgRpcsByTypeInner
from slurm_rest.models.v0040_stats_msg_rpcs_by_user_inner import V0040StatsMsgRpcsByUserInner
from typing import Optional, Set
from typing_extensions import Self

class V0039StatsMsg(BaseModel):
    """
    V0039StatsMsg
    """ # noqa: E501
    parts_packed: Optional[StrictInt] = None
    req_time: Optional[StrictInt] = None
    req_time_start: Optional[StrictInt] = None
    server_thread_count: Optional[StrictInt] = None
    agent_queue_size: Optional[StrictInt] = None
    agent_count: Optional[StrictInt] = None
    agent_thread_count: Optional[StrictInt] = None
    dbd_agent_queue_size: Optional[StrictInt] = None
    gettimeofday_latency: Optional[StrictInt] = None
    schedule_cycle_max: Optional[StrictInt] = None
    schedule_cycle_last: Optional[StrictInt] = None
    schedule_cycle_total: Optional[StrictInt] = None
    schedule_cycle_mean: Optional[StrictInt] = None
    schedule_cycle_mean_depth: Optional[StrictInt] = None
    schedule_cycle_per_minute: Optional[StrictInt] = None
    schedule_queue_length: Optional[StrictInt] = None
    jobs_submitted: Optional[StrictInt] = None
    jobs_started: Optional[StrictInt] = None
    jobs_completed: Optional[StrictInt] = None
    jobs_canceled: Optional[StrictInt] = None
    jobs_failed: Optional[StrictInt] = None
    jobs_pending: Optional[StrictInt] = None
    jobs_running: Optional[StrictInt] = None
    job_states_ts: Optional[StrictInt] = None
    bf_backfilled_jobs: Optional[StrictInt] = None
    bf_last_backfilled_jobs: Optional[StrictInt] = None
    bf_backfilled_het_jobs: Optional[StrictInt] = None
    bf_cycle_counter: Optional[StrictInt] = None
    bf_cycle_mean: Optional[StrictInt] = None
    bf_depth_mean: Optional[StrictInt] = None
    bf_depth_mean_try: Optional[StrictInt] = None
    bf_cycle_sum: Optional[StrictInt] = None
    bf_cycle_last: Optional[StrictInt] = None
    bf_last_depth: Optional[StrictInt] = None
    bf_last_depth_try: Optional[StrictInt] = None
    bf_depth_sum: Optional[StrictInt] = None
    bf_depth_try_sum: Optional[StrictInt] = None
    bf_queue_len: Optional[StrictInt] = None
    bf_queue_len_mean: Optional[StrictInt] = None
    bf_queue_len_sum: Optional[StrictInt] = None
    bf_table_size: Optional[StrictInt] = None
    bf_table_size_mean: Optional[StrictInt] = None
    bf_when_last_cycle: Optional[StrictInt] = None
    bf_active: Optional[StrictBool] = None
    rpcs_by_message_type: Optional[List[V0040StatsMsgRpcsByTypeInner]] = Field(default=None, description="RPCs by message type")
    rpcs_by_user: Optional[List[V0040StatsMsgRpcsByUserInner]] = Field(default=None, description="RPCs by user")
    __properties: ClassVar[List[str]] = ["parts_packed", "req_time", "req_time_start", "server_thread_count", "agent_queue_size", "agent_count", "agent_thread_count", "dbd_agent_queue_size", "gettimeofday_latency", "schedule_cycle_max", "schedule_cycle_last", "schedule_cycle_total", "schedule_cycle_mean", "schedule_cycle_mean_depth", "schedule_cycle_per_minute", "schedule_queue_length", "jobs_submitted", "jobs_started", "jobs_completed", "jobs_canceled", "jobs_failed", "jobs_pending", "jobs_running", "job_states_ts", "bf_backfilled_jobs", "bf_last_backfilled_jobs", "bf_backfilled_het_jobs", "bf_cycle_counter", "bf_cycle_mean", "bf_depth_mean", "bf_depth_mean_try", "bf_cycle_sum", "bf_cycle_last", "bf_last_depth", "bf_last_depth_try", "bf_depth_sum", "bf_depth_try_sum", "bf_queue_len", "bf_queue_len_mean", "bf_queue_len_sum", "bf_table_size", "bf_table_size_mean", "bf_when_last_cycle", "bf_active", "rpcs_by_message_type", "rpcs_by_user"]

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
        """Create an instance of V0039StatsMsg from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in rpcs_by_message_type (list)
        _items = []
        if self.rpcs_by_message_type:
            for _item_rpcs_by_message_type in self.rpcs_by_message_type:
                if _item_rpcs_by_message_type:
                    _items.append(_item_rpcs_by_message_type.to_dict())
            _dict['rpcs_by_message_type'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in rpcs_by_user (list)
        _items = []
        if self.rpcs_by_user:
            for _item_rpcs_by_user in self.rpcs_by_user:
                if _item_rpcs_by_user:
                    _items.append(_item_rpcs_by_user.to_dict())
            _dict['rpcs_by_user'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0039StatsMsg from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "parts_packed": obj.get("parts_packed"),
            "req_time": obj.get("req_time"),
            "req_time_start": obj.get("req_time_start"),
            "server_thread_count": obj.get("server_thread_count"),
            "agent_queue_size": obj.get("agent_queue_size"),
            "agent_count": obj.get("agent_count"),
            "agent_thread_count": obj.get("agent_thread_count"),
            "dbd_agent_queue_size": obj.get("dbd_agent_queue_size"),
            "gettimeofday_latency": obj.get("gettimeofday_latency"),
            "schedule_cycle_max": obj.get("schedule_cycle_max"),
            "schedule_cycle_last": obj.get("schedule_cycle_last"),
            "schedule_cycle_total": obj.get("schedule_cycle_total"),
            "schedule_cycle_mean": obj.get("schedule_cycle_mean"),
            "schedule_cycle_mean_depth": obj.get("schedule_cycle_mean_depth"),
            "schedule_cycle_per_minute": obj.get("schedule_cycle_per_minute"),
            "schedule_queue_length": obj.get("schedule_queue_length"),
            "jobs_submitted": obj.get("jobs_submitted"),
            "jobs_started": obj.get("jobs_started"),
            "jobs_completed": obj.get("jobs_completed"),
            "jobs_canceled": obj.get("jobs_canceled"),
            "jobs_failed": obj.get("jobs_failed"),
            "jobs_pending": obj.get("jobs_pending"),
            "jobs_running": obj.get("jobs_running"),
            "job_states_ts": obj.get("job_states_ts"),
            "bf_backfilled_jobs": obj.get("bf_backfilled_jobs"),
            "bf_last_backfilled_jobs": obj.get("bf_last_backfilled_jobs"),
            "bf_backfilled_het_jobs": obj.get("bf_backfilled_het_jobs"),
            "bf_cycle_counter": obj.get("bf_cycle_counter"),
            "bf_cycle_mean": obj.get("bf_cycle_mean"),
            "bf_depth_mean": obj.get("bf_depth_mean"),
            "bf_depth_mean_try": obj.get("bf_depth_mean_try"),
            "bf_cycle_sum": obj.get("bf_cycle_sum"),
            "bf_cycle_last": obj.get("bf_cycle_last"),
            "bf_last_depth": obj.get("bf_last_depth"),
            "bf_last_depth_try": obj.get("bf_last_depth_try"),
            "bf_depth_sum": obj.get("bf_depth_sum"),
            "bf_depth_try_sum": obj.get("bf_depth_try_sum"),
            "bf_queue_len": obj.get("bf_queue_len"),
            "bf_queue_len_mean": obj.get("bf_queue_len_mean"),
            "bf_queue_len_sum": obj.get("bf_queue_len_sum"),
            "bf_table_size": obj.get("bf_table_size"),
            "bf_table_size_mean": obj.get("bf_table_size_mean"),
            "bf_when_last_cycle": obj.get("bf_when_last_cycle"),
            "bf_active": obj.get("bf_active"),
            "rpcs_by_message_type": [V0040StatsMsgRpcsByTypeInner.from_dict(_item) for _item in obj["rpcs_by_message_type"]] if obj.get("rpcs_by_message_type") is not None else None,
            "rpcs_by_user": [V0040StatsMsgRpcsByUserInner.from_dict(_item) for _item in obj["rpcs_by_user"]] if obj.get("rpcs_by_user") is not None else None
        })
        return _obj


