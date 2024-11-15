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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from slurm_rest.models.v0040_job_comment import V0040JobComment
from slurm_rest.models.v0040_job_mcs import V0040JobMcs
from slurm_rest.models.v0040_job_reservation import V0040JobReservation
from slurm_rest.models.v0040_job_state import V0040JobState
from slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_array import V0041OpenapiSlurmdbdJobsRespJobsInnerArray
from slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_association import V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation
from slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_derived_exit_code import V0041OpenapiSlurmdbdJobsRespJobsInnerDerivedExitCode
from slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_het import V0041OpenapiSlurmdbdJobsRespJobsInnerHet
from slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_priority import V0041OpenapiSlurmdbdJobsRespJobsInnerPriority
from slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_required import V0041OpenapiSlurmdbdJobsRespJobsInnerRequired
from slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner import V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInner
from slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time import V0041OpenapiSlurmdbdJobsRespJobsInnerTime
from slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_tres import V0041OpenapiSlurmdbdJobsRespJobsInnerTres
from slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_wckey import V0041OpenapiSlurmdbdJobsRespJobsInnerWckey
from typing import Optional, Set
from typing_extensions import Self

class V0041OpenapiSlurmdbdJobsRespJobsInner(BaseModel):
    """
    V0041OpenapiSlurmdbdJobsRespJobsInner
    """ # noqa: E501
    account: Optional[StrictStr] = None
    comment: Optional[V0040JobComment] = None
    allocation_nodes: Optional[StrictInt] = None
    array: Optional[V0041OpenapiSlurmdbdJobsRespJobsInnerArray] = None
    association: Optional[V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation] = None
    block: Optional[StrictStr] = None
    cluster: Optional[StrictStr] = None
    constraints: Optional[StrictStr] = None
    container: Optional[StrictStr] = None
    derived_exit_code: Optional[V0041OpenapiSlurmdbdJobsRespJobsInnerDerivedExitCode] = None
    time: Optional[V0041OpenapiSlurmdbdJobsRespJobsInnerTime] = None
    exit_code: Optional[V0041OpenapiSlurmdbdJobsRespJobsInnerDerivedExitCode] = None
    extra: Optional[StrictStr] = None
    failed_node: Optional[StrictStr] = None
    flags: Optional[List[StrictStr]] = None
    group: Optional[StrictStr] = None
    het: Optional[V0041OpenapiSlurmdbdJobsRespJobsInnerHet] = None
    job_id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    licenses: Optional[StrictStr] = None
    mcs: Optional[V0040JobMcs] = None
    nodes: Optional[StrictStr] = None
    partition: Optional[StrictStr] = None
    hold: Optional[StrictBool] = Field(default=None, description="Hold (true) or release (false) job")
    priority: Optional[V0041OpenapiSlurmdbdJobsRespJobsInnerPriority] = None
    qos: Optional[StrictStr] = None
    required: Optional[V0041OpenapiSlurmdbdJobsRespJobsInnerRequired] = None
    kill_request_user: Optional[StrictStr] = None
    reservation: Optional[V0040JobReservation] = None
    script: Optional[StrictStr] = None
    stdin_expanded: Optional[StrictStr] = Field(default=None, description="Job stdin with expanded fields")
    stdout_expanded: Optional[StrictStr] = Field(default=None, description="Job stdout with expanded fields")
    stderr_expanded: Optional[StrictStr] = Field(default=None, description="Job stderr with expanded fields")
    stdout: Optional[StrictStr] = None
    stderr: Optional[StrictStr] = None
    stdin: Optional[StrictStr] = None
    state: Optional[V0040JobState] = None
    steps: Optional[List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInner]] = None
    submit_line: Optional[StrictStr] = None
    tres: Optional[V0041OpenapiSlurmdbdJobsRespJobsInnerTres] = None
    used_gres: Optional[StrictStr] = None
    user: Optional[StrictStr] = None
    wckey: Optional[V0041OpenapiSlurmdbdJobsRespJobsInnerWckey] = None
    working_directory: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["account", "comment", "allocation_nodes", "array", "association", "block", "cluster", "constraints", "container", "derived_exit_code", "time", "exit_code", "extra", "failed_node", "flags", "group", "het", "job_id", "name", "licenses", "mcs", "nodes", "partition", "hold", "priority", "qos", "required", "kill_request_user", "reservation", "script", "stdin_expanded", "stdout_expanded", "stderr_expanded", "stdout", "stderr", "stdin", "state", "steps", "submit_line", "tres", "used_gres", "user", "wckey", "working_directory"]

    @field_validator('flags')
    def flags_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['NONE', 'CLEAR_SCHEDULING', 'NOT_SET', 'STARTED_ON_SUBMIT', 'STARTED_ON_SCHEDULE', 'STARTED_ON_BACKFILL', 'START_RECEIVED']):
                raise ValueError("each list item must be one of ('NONE', 'CLEAR_SCHEDULING', 'NOT_SET', 'STARTED_ON_SUBMIT', 'STARTED_ON_SCHEDULE', 'STARTED_ON_BACKFILL', 'START_RECEIVED')")
        return value

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
        """Create an instance of V0041OpenapiSlurmdbdJobsRespJobsInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of comment
        if self.comment:
            _dict['comment'] = self.comment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of array
        if self.array:
            _dict['array'] = self.array.to_dict()
        # override the default output from pydantic by calling `to_dict()` of association
        if self.association:
            _dict['association'] = self.association.to_dict()
        # override the default output from pydantic by calling `to_dict()` of derived_exit_code
        if self.derived_exit_code:
            _dict['derived_exit_code'] = self.derived_exit_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of time
        if self.time:
            _dict['time'] = self.time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of exit_code
        if self.exit_code:
            _dict['exit_code'] = self.exit_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of het
        if self.het:
            _dict['het'] = self.het.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mcs
        if self.mcs:
            _dict['mcs'] = self.mcs.to_dict()
        # override the default output from pydantic by calling `to_dict()` of priority
        if self.priority:
            _dict['priority'] = self.priority.to_dict()
        # override the default output from pydantic by calling `to_dict()` of required
        if self.required:
            _dict['required'] = self.required.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reservation
        if self.reservation:
            _dict['reservation'] = self.reservation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in steps (list)
        _items = []
        if self.steps:
            for _item_steps in self.steps:
                if _item_steps:
                    _items.append(_item_steps.to_dict())
            _dict['steps'] = _items
        # override the default output from pydantic by calling `to_dict()` of tres
        if self.tres:
            _dict['tres'] = self.tres.to_dict()
        # override the default output from pydantic by calling `to_dict()` of wckey
        if self.wckey:
            _dict['wckey'] = self.wckey.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0041OpenapiSlurmdbdJobsRespJobsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "account": obj.get("account"),
            "comment": V0040JobComment.from_dict(obj["comment"]) if obj.get("comment") is not None else None,
            "allocation_nodes": obj.get("allocation_nodes"),
            "array": V0041OpenapiSlurmdbdJobsRespJobsInnerArray.from_dict(obj["array"]) if obj.get("array") is not None else None,
            "association": V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation.from_dict(obj["association"]) if obj.get("association") is not None else None,
            "block": obj.get("block"),
            "cluster": obj.get("cluster"),
            "constraints": obj.get("constraints"),
            "container": obj.get("container"),
            "derived_exit_code": V0041OpenapiSlurmdbdJobsRespJobsInnerDerivedExitCode.from_dict(obj["derived_exit_code"]) if obj.get("derived_exit_code") is not None else None,
            "time": V0041OpenapiSlurmdbdJobsRespJobsInnerTime.from_dict(obj["time"]) if obj.get("time") is not None else None,
            "exit_code": V0041OpenapiSlurmdbdJobsRespJobsInnerDerivedExitCode.from_dict(obj["exit_code"]) if obj.get("exit_code") is not None else None,
            "extra": obj.get("extra"),
            "failed_node": obj.get("failed_node"),
            "flags": obj.get("flags"),
            "group": obj.get("group"),
            "het": V0041OpenapiSlurmdbdJobsRespJobsInnerHet.from_dict(obj["het"]) if obj.get("het") is not None else None,
            "job_id": obj.get("job_id"),
            "name": obj.get("name"),
            "licenses": obj.get("licenses"),
            "mcs": V0040JobMcs.from_dict(obj["mcs"]) if obj.get("mcs") is not None else None,
            "nodes": obj.get("nodes"),
            "partition": obj.get("partition"),
            "hold": obj.get("hold"),
            "priority": V0041OpenapiSlurmdbdJobsRespJobsInnerPriority.from_dict(obj["priority"]) if obj.get("priority") is not None else None,
            "qos": obj.get("qos"),
            "required": V0041OpenapiSlurmdbdJobsRespJobsInnerRequired.from_dict(obj["required"]) if obj.get("required") is not None else None,
            "kill_request_user": obj.get("kill_request_user"),
            "reservation": V0040JobReservation.from_dict(obj["reservation"]) if obj.get("reservation") is not None else None,
            "script": obj.get("script"),
            "stdin_expanded": obj.get("stdin_expanded"),
            "stdout_expanded": obj.get("stdout_expanded"),
            "stderr_expanded": obj.get("stderr_expanded"),
            "stdout": obj.get("stdout"),
            "stderr": obj.get("stderr"),
            "stdin": obj.get("stdin"),
            "state": V0040JobState.from_dict(obj["state"]) if obj.get("state") is not None else None,
            "steps": [V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInner.from_dict(_item) for _item in obj["steps"]] if obj.get("steps") is not None else None,
            "submit_line": obj.get("submit_line"),
            "tres": V0041OpenapiSlurmdbdJobsRespJobsInnerTres.from_dict(obj["tres"]) if obj.get("tres") is not None else None,
            "used_gres": obj.get("used_gres"),
            "user": obj.get("user"),
            "wckey": V0041OpenapiSlurmdbdJobsRespJobsInnerWckey.from_dict(obj["wckey"]) if obj.get("wckey") is not None else None,
            "working_directory": obj.get("working_directory")
        })
        return _obj


