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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from slurm_rest.models.v0040_process_exit_code_verbose import V0040ProcessExitCodeVerbose
from slurm_rest.models.v0040_step_cpu import V0040StepCPU
from slurm_rest.models.v0040_step_nodes import V0040StepNodes
from slurm_rest.models.v0040_step_statistics import V0040StepStatistics
from slurm_rest.models.v0040_step_step import V0040StepStep
from slurm_rest.models.v0040_step_task import V0040StepTask
from slurm_rest.models.v0040_step_tasks import V0040StepTasks
from slurm_rest.models.v0040_step_time import V0040StepTime
from slurm_rest.models.v0040_step_tres import V0040StepTres
from typing import Optional, Set
from typing_extensions import Self

class V0040Step(BaseModel):
    """
    V0040Step
    """ # noqa: E501
    time: Optional[V0040StepTime] = None
    exit_code: Optional[V0040ProcessExitCodeVerbose] = None
    nodes: Optional[V0040StepNodes] = None
    tasks: Optional[V0040StepTasks] = None
    pid: Optional[StrictStr] = None
    cpu: Optional[V0040StepCPU] = Field(default=None, alias="CPU")
    kill_request_user: Optional[StrictStr] = None
    state: Optional[List[StrictStr]] = None
    statistics: Optional[V0040StepStatistics] = None
    step: Optional[V0040StepStep] = None
    task: Optional[V0040StepTask] = None
    tres: Optional[V0040StepTres] = None
    __properties: ClassVar[List[str]] = ["time", "exit_code", "nodes", "tasks", "pid", "CPU", "kill_request_user", "state", "statistics", "step", "task", "tres"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['PENDING', 'RUNNING', 'SUSPENDED', 'COMPLETED', 'CANCELLED', 'FAILED', 'TIMEOUT', 'NODE_FAIL', 'PREEMPTED', 'BOOT_FAIL', 'DEADLINE', 'OUT_OF_MEMORY', 'LAUNCH_FAILED', 'UPDATE_DB', 'REQUEUED', 'REQUEUE_HOLD', 'SPECIAL_EXIT', 'RESIZING', 'CONFIGURING', 'COMPLETING', 'STOPPED', 'RECONFIG_FAIL', 'POWER_UP_NODE', 'REVOKED', 'REQUEUE_FED', 'RESV_DEL_HOLD', 'SIGNALING', 'STAGE_OUT']):
                raise ValueError("each list item must be one of ('PENDING', 'RUNNING', 'SUSPENDED', 'COMPLETED', 'CANCELLED', 'FAILED', 'TIMEOUT', 'NODE_FAIL', 'PREEMPTED', 'BOOT_FAIL', 'DEADLINE', 'OUT_OF_MEMORY', 'LAUNCH_FAILED', 'UPDATE_DB', 'REQUEUED', 'REQUEUE_HOLD', 'SPECIAL_EXIT', 'RESIZING', 'CONFIGURING', 'COMPLETING', 'STOPPED', 'RECONFIG_FAIL', 'POWER_UP_NODE', 'REVOKED', 'REQUEUE_FED', 'RESV_DEL_HOLD', 'SIGNALING', 'STAGE_OUT')")
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
        """Create an instance of V0040Step from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of time
        if self.time:
            _dict['time'] = self.time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of exit_code
        if self.exit_code:
            _dict['exit_code'] = self.exit_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nodes
        if self.nodes:
            _dict['nodes'] = self.nodes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tasks
        if self.tasks:
            _dict['tasks'] = self.tasks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cpu
        if self.cpu:
            _dict['CPU'] = self.cpu.to_dict()
        # override the default output from pydantic by calling `to_dict()` of statistics
        if self.statistics:
            _dict['statistics'] = self.statistics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of step
        if self.step:
            _dict['step'] = self.step.to_dict()
        # override the default output from pydantic by calling `to_dict()` of task
        if self.task:
            _dict['task'] = self.task.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tres
        if self.tres:
            _dict['tres'] = self.tres.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0040Step from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "time": V0040StepTime.from_dict(obj["time"]) if obj.get("time") is not None else None,
            "exit_code": V0040ProcessExitCodeVerbose.from_dict(obj["exit_code"]) if obj.get("exit_code") is not None else None,
            "nodes": V0040StepNodes.from_dict(obj["nodes"]) if obj.get("nodes") is not None else None,
            "tasks": V0040StepTasks.from_dict(obj["tasks"]) if obj.get("tasks") is not None else None,
            "pid": obj.get("pid"),
            "CPU": V0040StepCPU.from_dict(obj["CPU"]) if obj.get("CPU") is not None else None,
            "kill_request_user": obj.get("kill_request_user"),
            "state": obj.get("state"),
            "statistics": V0040StepStatistics.from_dict(obj["statistics"]) if obj.get("statistics") is not None else None,
            "step": V0040StepStep.from_dict(obj["step"]) if obj.get("step") is not None else None,
            "task": V0040StepTask.from_dict(obj["task"]) if obj.get("task") is not None else None,
            "tres": V0040StepTres.from_dict(obj["tres"]) if obj.get("tres") is not None else None
        })
        return _obj

