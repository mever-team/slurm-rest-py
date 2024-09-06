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
from slurm_rest.models.v0039_float64_no_val import V0039Float64NoVal
from slurm_rest.models.v0039_job_info_power import V0039JobInfoPower
from slurm_rest.models.v0039_job_res import V0039JobRes
from slurm_rest.models.v0039_uint16_no_val import V0039Uint16NoVal
from slurm_rest.models.v0039_uint32_no_val import V0039Uint32NoVal
from slurm_rest.models.v0039_uint64_no_val import V0039Uint64NoVal
from typing import Optional, Set
from typing_extensions import Self

class V0039JobInfo(BaseModel):
    """
    V0039JobInfo
    """ # noqa: E501
    account: Optional[StrictStr] = None
    accrue_time: Optional[StrictInt] = None
    admin_comment: Optional[StrictStr] = None
    allocating_node: Optional[StrictStr] = None
    array_job_id: Optional[V0039Uint32NoVal] = None
    array_task_id: Optional[V0039Uint32NoVal] = None
    array_max_tasks: Optional[V0039Uint32NoVal] = None
    array_task_string: Optional[StrictStr] = None
    association_id: Optional[StrictInt] = None
    batch_features: Optional[StrictStr] = None
    batch_flag: Optional[StrictBool] = None
    batch_host: Optional[StrictStr] = None
    flags: Optional[List[StrictStr]] = None
    burst_buffer: Optional[StrictStr] = None
    burst_buffer_state: Optional[StrictStr] = None
    cluster: Optional[StrictStr] = None
    cluster_features: Optional[StrictStr] = None
    command: Optional[StrictStr] = None
    comment: Optional[StrictStr] = None
    container: Optional[StrictStr] = None
    container_id: Optional[StrictStr] = None
    contiguous: Optional[StrictBool] = None
    core_spec: Optional[StrictInt] = None
    thread_spec: Optional[StrictInt] = None
    cores_per_socket: Optional[V0039Uint16NoVal] = None
    billable_tres: Optional[V0039Float64NoVal] = None
    cpus_per_task: Optional[V0039Uint16NoVal] = None
    cpu_frequency_minimum: Optional[V0039Uint32NoVal] = None
    cpu_frequency_maximum: Optional[V0039Uint32NoVal] = None
    cpu_frequency_governor: Optional[V0039Uint32NoVal] = None
    cpus_per_tres: Optional[StrictStr] = None
    cron: Optional[StrictStr] = None
    deadline: Optional[StrictInt] = None
    delay_boot: Optional[V0039Uint32NoVal] = None
    dependency: Optional[StrictStr] = None
    derived_exit_code: Optional[V0039Uint32NoVal] = None
    eligible_time: Optional[StrictInt] = None
    end_time: Optional[StrictInt] = None
    excluded_nodes: Optional[StrictStr] = None
    exit_code: Optional[V0039Uint32NoVal] = None
    extra: Optional[StrictStr] = None
    failed_node: Optional[StrictStr] = None
    features: Optional[StrictStr] = None
    federation_origin: Optional[StrictStr] = None
    federation_siblings_active: Optional[StrictStr] = None
    federation_siblings_viable: Optional[StrictStr] = None
    gres_detail: Optional[List[StrictStr]] = None
    group_id: Optional[StrictInt] = None
    group_name: Optional[StrictStr] = None
    het_job_id: Optional[V0039Uint32NoVal] = None
    het_job_id_set: Optional[StrictStr] = None
    het_job_offset: Optional[V0039Uint32NoVal] = None
    job_id: Optional[StrictInt] = None
    job_resources: Optional[V0039JobRes] = None
    job_size_str: Optional[List[StrictStr]] = None
    job_state: Optional[StrictStr] = None
    last_sched_evaluation: Optional[StrictInt] = None
    licenses: Optional[StrictStr] = None
    mail_type: Optional[List[StrictStr]] = None
    mail_user: Optional[StrictStr] = None
    max_cpus: Optional[V0039Uint32NoVal] = None
    max_nodes: Optional[V0039Uint32NoVal] = None
    mcs_label: Optional[StrictStr] = None
    memory_per_tres: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    network: Optional[StrictStr] = None
    nodes: Optional[StrictStr] = None
    nice: Optional[StrictInt] = None
    tasks_per_core: Optional[V0039Uint16NoVal] = None
    tasks_per_tres: Optional[V0039Uint16NoVal] = None
    tasks_per_node: Optional[V0039Uint16NoVal] = None
    tasks_per_socket: Optional[V0039Uint16NoVal] = None
    tasks_per_board: Optional[V0039Uint16NoVal] = None
    cpus: Optional[V0039Uint32NoVal] = None
    node_count: Optional[V0039Uint32NoVal] = None
    tasks: Optional[V0039Uint32NoVal] = None
    partition: Optional[StrictStr] = None
    prefer: Optional[StrictStr] = None
    memory_per_cpu: Optional[V0039Uint64NoVal] = None
    memory_per_node: Optional[V0039Uint64NoVal] = None
    minimum_cpus_per_node: Optional[V0039Uint16NoVal] = None
    minimum_tmp_disk_per_node: Optional[V0039Uint32NoVal] = None
    power: Optional[V0039JobInfoPower] = None
    preempt_time: Optional[StrictInt] = None
    preemptable_time: Optional[StrictInt] = None
    pre_sus_time: Optional[StrictInt] = None
    hold: Optional[StrictBool] = Field(default=None, description="Hold (true) or release (false) job")
    priority: Optional[V0039Uint32NoVal] = None
    profile: Optional[List[StrictStr]] = None
    qos: Optional[StrictStr] = None
    reboot: Optional[StrictBool] = None
    required_nodes: Optional[StrictStr] = None
    minimum_switches: Optional[StrictInt] = None
    requeue: Optional[StrictBool] = None
    resize_time: Optional[StrictInt] = None
    restart_cnt: Optional[StrictInt] = None
    resv_name: Optional[StrictStr] = None
    scheduled_nodes: Optional[StrictStr] = None
    selinux_context: Optional[StrictStr] = None
    shared: Optional[List[StrictStr]] = None
    exclusive: Optional[List[StrictStr]] = None
    oversubscribe: Optional[StrictBool] = None
    show_flags: Optional[List[StrictStr]] = None
    sockets_per_board: Optional[StrictInt] = None
    sockets_per_node: Optional[V0039Uint16NoVal] = None
    start_time: Optional[StrictInt] = None
    state_description: Optional[StrictStr] = None
    state_reason: Optional[StrictStr] = None
    standard_error: Optional[StrictStr] = None
    standard_input: Optional[StrictStr] = None
    standard_output: Optional[StrictStr] = None
    submit_time: Optional[StrictInt] = None
    suspend_time: Optional[StrictInt] = None
    system_comment: Optional[StrictStr] = None
    time_limit: Optional[V0039Uint32NoVal] = None
    time_minimum: Optional[V0039Uint32NoVal] = None
    threads_per_core: Optional[V0039Uint16NoVal] = None
    tres_bind: Optional[StrictStr] = None
    tres_freq: Optional[StrictStr] = None
    tres_per_job: Optional[StrictStr] = None
    tres_per_node: Optional[StrictStr] = None
    tres_per_socket: Optional[StrictStr] = None
    tres_per_task: Optional[StrictStr] = None
    tres_req_str: Optional[StrictStr] = None
    tres_alloc_str: Optional[StrictStr] = None
    user_id: Optional[StrictInt] = None
    user_name: Optional[StrictStr] = None
    maximum_switch_wait_time: Optional[StrictInt] = None
    wckey: Optional[StrictStr] = None
    current_working_directory: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["account", "accrue_time", "admin_comment", "allocating_node", "array_job_id", "array_task_id", "array_max_tasks", "array_task_string", "association_id", "batch_features", "batch_flag", "batch_host", "flags", "burst_buffer", "burst_buffer_state", "cluster", "cluster_features", "command", "comment", "container", "container_id", "contiguous", "core_spec", "thread_spec", "cores_per_socket", "billable_tres", "cpus_per_task", "cpu_frequency_minimum", "cpu_frequency_maximum", "cpu_frequency_governor", "cpus_per_tres", "cron", "deadline", "delay_boot", "dependency", "derived_exit_code", "eligible_time", "end_time", "excluded_nodes", "exit_code", "extra", "failed_node", "features", "federation_origin", "federation_siblings_active", "federation_siblings_viable", "gres_detail", "group_id", "group_name", "het_job_id", "het_job_id_set", "het_job_offset", "job_id", "job_resources", "job_size_str", "job_state", "last_sched_evaluation", "licenses", "mail_type", "mail_user", "max_cpus", "max_nodes", "mcs_label", "memory_per_tres", "name", "network", "nodes", "nice", "tasks_per_core", "tasks_per_tres", "tasks_per_node", "tasks_per_socket", "tasks_per_board", "cpus", "node_count", "tasks", "partition", "prefer", "memory_per_cpu", "memory_per_node", "minimum_cpus_per_node", "minimum_tmp_disk_per_node", "power", "preempt_time", "preemptable_time", "pre_sus_time", "hold", "priority", "profile", "qos", "reboot", "required_nodes", "minimum_switches", "requeue", "resize_time", "restart_cnt", "resv_name", "scheduled_nodes", "selinux_context", "shared", "exclusive", "oversubscribe", "show_flags", "sockets_per_board", "sockets_per_node", "start_time", "state_description", "state_reason", "standard_error", "standard_input", "standard_output", "submit_time", "suspend_time", "system_comment", "time_limit", "time_minimum", "threads_per_core", "tres_bind", "tres_freq", "tres_per_job", "tres_per_node", "tres_per_socket", "tres_per_task", "tres_req_str", "tres_alloc_str", "user_id", "user_name", "maximum_switch_wait_time", "wckey", "current_working_directory"]

    @field_validator('flags')
    def flags_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['KILL_INVALID_DEPENDENCY', 'NO_KILL_INVALID_DEPENDENCY', 'HAS_STATE_DIRECTORY', 'TESTING_BACKFILL', 'GRES_BINDING_ENFORCED', 'TEST_NOW_ONLY', 'SEND_JOB_ENVIRONMENT', 'SPREAD_JOB', 'PREFER_MINIMUM_NODE_COUNT', 'JOB_KILL_HURRY', 'SKIP_TRES_STRING_ACCOUNTING', 'SIBLING_CLUSTER_UPDATE_ONLY', 'HETEROGENEOUS_JOB', 'EXACT_TASK_COUNT_REQUESTED', 'EXACT_CPU_COUNT_REQUESTED', 'TESTING_WHOLE_NODE_BACKFILL', 'TOP_PRIORITY_JOB', 'ACCRUE_COUNT_CLEARED', 'GRED_BINDING_DISABLED', 'JOB_WAS_RUNNING', 'JOB_ACCRUE_TIME_RESET', 'CRON_JOB', 'EXACT_MEMORY_REQUESTED', 'USING_DEFAULT_ACCOUNT', 'USING_DEFAULT_PARTITION', 'USING_DEFAULT_QOS', 'USING_DEFAULT_WCKEY', 'DEPENDENT', 'MAGNETIC', 'PARTITION_ASSIGNED', 'BACKFILL_ATTEMPTED', 'SCHEDULING_ATTEMPTED', 'SAVE_BATCH_SCRIPT']):
                raise ValueError("each list item must be one of ('KILL_INVALID_DEPENDENCY', 'NO_KILL_INVALID_DEPENDENCY', 'HAS_STATE_DIRECTORY', 'TESTING_BACKFILL', 'GRES_BINDING_ENFORCED', 'TEST_NOW_ONLY', 'SEND_JOB_ENVIRONMENT', 'SPREAD_JOB', 'PREFER_MINIMUM_NODE_COUNT', 'JOB_KILL_HURRY', 'SKIP_TRES_STRING_ACCOUNTING', 'SIBLING_CLUSTER_UPDATE_ONLY', 'HETEROGENEOUS_JOB', 'EXACT_TASK_COUNT_REQUESTED', 'EXACT_CPU_COUNT_REQUESTED', 'TESTING_WHOLE_NODE_BACKFILL', 'TOP_PRIORITY_JOB', 'ACCRUE_COUNT_CLEARED', 'GRED_BINDING_DISABLED', 'JOB_WAS_RUNNING', 'JOB_ACCRUE_TIME_RESET', 'CRON_JOB', 'EXACT_MEMORY_REQUESTED', 'USING_DEFAULT_ACCOUNT', 'USING_DEFAULT_PARTITION', 'USING_DEFAULT_QOS', 'USING_DEFAULT_WCKEY', 'DEPENDENT', 'MAGNETIC', 'PARTITION_ASSIGNED', 'BACKFILL_ATTEMPTED', 'SCHEDULING_ATTEMPTED', 'SAVE_BATCH_SCRIPT')")
        return value

    @field_validator('mail_type')
    def mail_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['BEGIN', 'END', 'FAIL', 'REQUEUE', 'TIME=100%', 'TIME=90%', 'TIME=80%', 'TIME=50%', 'STAGE_OUT', 'ARRAY_TASKS', 'INVALID_DEPENDENCY']):
                raise ValueError("each list item must be one of ('BEGIN', 'END', 'FAIL', 'REQUEUE', 'TIME=100%', 'TIME=90%', 'TIME=80%', 'TIME=50%', 'STAGE_OUT', 'ARRAY_TASKS', 'INVALID_DEPENDENCY')")
        return value

    @field_validator('profile')
    def profile_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['NOT_SET', 'NONE', 'ENERGY', 'LUSTRE', 'NETWORK', 'TASK']):
                raise ValueError("each list item must be one of ('NOT_SET', 'NONE', 'ENERGY', 'LUSTRE', 'NETWORK', 'TASK')")
        return value

    @field_validator('shared')
    def shared_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['none', 'oversubscribe', 'user', 'mcs']):
                raise ValueError("each list item must be one of ('none', 'oversubscribe', 'user', 'mcs')")
        return value

    @field_validator('exclusive')
    def exclusive_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['true', 'false', 'user', 'mcs']):
                raise ValueError("each list item must be one of ('true', 'false', 'user', 'mcs')")
        return value

    @field_validator('show_flags')
    def show_flags_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['ALL', 'DETAIL', 'MIXED', 'LOCAL', 'SIBLING', 'FEDERATION', 'FUTURE']):
                raise ValueError("each list item must be one of ('ALL', 'DETAIL', 'MIXED', 'LOCAL', 'SIBLING', 'FEDERATION', 'FUTURE')")
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
        """Create an instance of V0039JobInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of array_job_id
        if self.array_job_id:
            _dict['array_job_id'] = self.array_job_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of array_task_id
        if self.array_task_id:
            _dict['array_task_id'] = self.array_task_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of array_max_tasks
        if self.array_max_tasks:
            _dict['array_max_tasks'] = self.array_max_tasks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cores_per_socket
        if self.cores_per_socket:
            _dict['cores_per_socket'] = self.cores_per_socket.to_dict()
        # override the default output from pydantic by calling `to_dict()` of billable_tres
        if self.billable_tres:
            _dict['billable_tres'] = self.billable_tres.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cpus_per_task
        if self.cpus_per_task:
            _dict['cpus_per_task'] = self.cpus_per_task.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cpu_frequency_minimum
        if self.cpu_frequency_minimum:
            _dict['cpu_frequency_minimum'] = self.cpu_frequency_minimum.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cpu_frequency_maximum
        if self.cpu_frequency_maximum:
            _dict['cpu_frequency_maximum'] = self.cpu_frequency_maximum.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cpu_frequency_governor
        if self.cpu_frequency_governor:
            _dict['cpu_frequency_governor'] = self.cpu_frequency_governor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of delay_boot
        if self.delay_boot:
            _dict['delay_boot'] = self.delay_boot.to_dict()
        # override the default output from pydantic by calling `to_dict()` of derived_exit_code
        if self.derived_exit_code:
            _dict['derived_exit_code'] = self.derived_exit_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of exit_code
        if self.exit_code:
            _dict['exit_code'] = self.exit_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of het_job_id
        if self.het_job_id:
            _dict['het_job_id'] = self.het_job_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of het_job_offset
        if self.het_job_offset:
            _dict['het_job_offset'] = self.het_job_offset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of job_resources
        if self.job_resources:
            _dict['job_resources'] = self.job_resources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of max_cpus
        if self.max_cpus:
            _dict['max_cpus'] = self.max_cpus.to_dict()
        # override the default output from pydantic by calling `to_dict()` of max_nodes
        if self.max_nodes:
            _dict['max_nodes'] = self.max_nodes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tasks_per_core
        if self.tasks_per_core:
            _dict['tasks_per_core'] = self.tasks_per_core.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tasks_per_tres
        if self.tasks_per_tres:
            _dict['tasks_per_tres'] = self.tasks_per_tres.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tasks_per_node
        if self.tasks_per_node:
            _dict['tasks_per_node'] = self.tasks_per_node.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tasks_per_socket
        if self.tasks_per_socket:
            _dict['tasks_per_socket'] = self.tasks_per_socket.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tasks_per_board
        if self.tasks_per_board:
            _dict['tasks_per_board'] = self.tasks_per_board.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cpus
        if self.cpus:
            _dict['cpus'] = self.cpus.to_dict()
        # override the default output from pydantic by calling `to_dict()` of node_count
        if self.node_count:
            _dict['node_count'] = self.node_count.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tasks
        if self.tasks:
            _dict['tasks'] = self.tasks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of memory_per_cpu
        if self.memory_per_cpu:
            _dict['memory_per_cpu'] = self.memory_per_cpu.to_dict()
        # override the default output from pydantic by calling `to_dict()` of memory_per_node
        if self.memory_per_node:
            _dict['memory_per_node'] = self.memory_per_node.to_dict()
        # override the default output from pydantic by calling `to_dict()` of minimum_cpus_per_node
        if self.minimum_cpus_per_node:
            _dict['minimum_cpus_per_node'] = self.minimum_cpus_per_node.to_dict()
        # override the default output from pydantic by calling `to_dict()` of minimum_tmp_disk_per_node
        if self.minimum_tmp_disk_per_node:
            _dict['minimum_tmp_disk_per_node'] = self.minimum_tmp_disk_per_node.to_dict()
        # override the default output from pydantic by calling `to_dict()` of power
        if self.power:
            _dict['power'] = self.power.to_dict()
        # override the default output from pydantic by calling `to_dict()` of priority
        if self.priority:
            _dict['priority'] = self.priority.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sockets_per_node
        if self.sockets_per_node:
            _dict['sockets_per_node'] = self.sockets_per_node.to_dict()
        # override the default output from pydantic by calling `to_dict()` of time_limit
        if self.time_limit:
            _dict['time_limit'] = self.time_limit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of time_minimum
        if self.time_minimum:
            _dict['time_minimum'] = self.time_minimum.to_dict()
        # override the default output from pydantic by calling `to_dict()` of threads_per_core
        if self.threads_per_core:
            _dict['threads_per_core'] = self.threads_per_core.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0039JobInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "account": obj.get("account"),
            "accrue_time": obj.get("accrue_time"),
            "admin_comment": obj.get("admin_comment"),
            "allocating_node": obj.get("allocating_node"),
            "array_job_id": V0039Uint32NoVal.from_dict(obj["array_job_id"]) if obj.get("array_job_id") is not None else None,
            "array_task_id": V0039Uint32NoVal.from_dict(obj["array_task_id"]) if obj.get("array_task_id") is not None else None,
            "array_max_tasks": V0039Uint32NoVal.from_dict(obj["array_max_tasks"]) if obj.get("array_max_tasks") is not None else None,
            "array_task_string": obj.get("array_task_string"),
            "association_id": obj.get("association_id"),
            "batch_features": obj.get("batch_features"),
            "batch_flag": obj.get("batch_flag"),
            "batch_host": obj.get("batch_host"),
            "flags": obj.get("flags"),
            "burst_buffer": obj.get("burst_buffer"),
            "burst_buffer_state": obj.get("burst_buffer_state"),
            "cluster": obj.get("cluster"),
            "cluster_features": obj.get("cluster_features"),
            "command": obj.get("command"),
            "comment": obj.get("comment"),
            "container": obj.get("container"),
            "container_id": obj.get("container_id"),
            "contiguous": obj.get("contiguous"),
            "core_spec": obj.get("core_spec"),
            "thread_spec": obj.get("thread_spec"),
            "cores_per_socket": V0039Uint16NoVal.from_dict(obj["cores_per_socket"]) if obj.get("cores_per_socket") is not None else None,
            "billable_tres": V0039Float64NoVal.from_dict(obj["billable_tres"]) if obj.get("billable_tres") is not None else None,
            "cpus_per_task": V0039Uint16NoVal.from_dict(obj["cpus_per_task"]) if obj.get("cpus_per_task") is not None else None,
            "cpu_frequency_minimum": V0039Uint32NoVal.from_dict(obj["cpu_frequency_minimum"]) if obj.get("cpu_frequency_minimum") is not None else None,
            "cpu_frequency_maximum": V0039Uint32NoVal.from_dict(obj["cpu_frequency_maximum"]) if obj.get("cpu_frequency_maximum") is not None else None,
            "cpu_frequency_governor": V0039Uint32NoVal.from_dict(obj["cpu_frequency_governor"]) if obj.get("cpu_frequency_governor") is not None else None,
            "cpus_per_tres": obj.get("cpus_per_tres"),
            "cron": obj.get("cron"),
            "deadline": obj.get("deadline"),
            "delay_boot": V0039Uint32NoVal.from_dict(obj["delay_boot"]) if obj.get("delay_boot") is not None else None,
            "dependency": obj.get("dependency"),
            "derived_exit_code": V0039Uint32NoVal.from_dict(obj["derived_exit_code"]) if obj.get("derived_exit_code") is not None else None,
            "eligible_time": obj.get("eligible_time"),
            "end_time": obj.get("end_time"),
            "excluded_nodes": obj.get("excluded_nodes"),
            "exit_code": V0039Uint32NoVal.from_dict(obj["exit_code"]) if obj.get("exit_code") is not None else None,
            "extra": obj.get("extra"),
            "failed_node": obj.get("failed_node"),
            "features": obj.get("features"),
            "federation_origin": obj.get("federation_origin"),
            "federation_siblings_active": obj.get("federation_siblings_active"),
            "federation_siblings_viable": obj.get("federation_siblings_viable"),
            "gres_detail": obj.get("gres_detail"),
            "group_id": obj.get("group_id"),
            "group_name": obj.get("group_name"),
            "het_job_id": V0039Uint32NoVal.from_dict(obj["het_job_id"]) if obj.get("het_job_id") is not None else None,
            "het_job_id_set": obj.get("het_job_id_set"),
            "het_job_offset": V0039Uint32NoVal.from_dict(obj["het_job_offset"]) if obj.get("het_job_offset") is not None else None,
            "job_id": obj.get("job_id"),
            "job_resources": V0039JobRes.from_dict(obj["job_resources"]) if obj.get("job_resources") is not None else None,
            "job_size_str": obj.get("job_size_str"),
            "job_state": obj.get("job_state"),
            "last_sched_evaluation": obj.get("last_sched_evaluation"),
            "licenses": obj.get("licenses"),
            "mail_type": obj.get("mail_type"),
            "mail_user": obj.get("mail_user"),
            "max_cpus": V0039Uint32NoVal.from_dict(obj["max_cpus"]) if obj.get("max_cpus") is not None else None,
            "max_nodes": V0039Uint32NoVal.from_dict(obj["max_nodes"]) if obj.get("max_nodes") is not None else None,
            "mcs_label": obj.get("mcs_label"),
            "memory_per_tres": obj.get("memory_per_tres"),
            "name": obj.get("name"),
            "network": obj.get("network"),
            "nodes": obj.get("nodes"),
            "nice": obj.get("nice"),
            "tasks_per_core": V0039Uint16NoVal.from_dict(obj["tasks_per_core"]) if obj.get("tasks_per_core") is not None else None,
            "tasks_per_tres": V0039Uint16NoVal.from_dict(obj["tasks_per_tres"]) if obj.get("tasks_per_tres") is not None else None,
            "tasks_per_node": V0039Uint16NoVal.from_dict(obj["tasks_per_node"]) if obj.get("tasks_per_node") is not None else None,
            "tasks_per_socket": V0039Uint16NoVal.from_dict(obj["tasks_per_socket"]) if obj.get("tasks_per_socket") is not None else None,
            "tasks_per_board": V0039Uint16NoVal.from_dict(obj["tasks_per_board"]) if obj.get("tasks_per_board") is not None else None,
            "cpus": V0039Uint32NoVal.from_dict(obj["cpus"]) if obj.get("cpus") is not None else None,
            "node_count": V0039Uint32NoVal.from_dict(obj["node_count"]) if obj.get("node_count") is not None else None,
            "tasks": V0039Uint32NoVal.from_dict(obj["tasks"]) if obj.get("tasks") is not None else None,
            "partition": obj.get("partition"),
            "prefer": obj.get("prefer"),
            "memory_per_cpu": V0039Uint64NoVal.from_dict(obj["memory_per_cpu"]) if obj.get("memory_per_cpu") is not None else None,
            "memory_per_node": V0039Uint64NoVal.from_dict(obj["memory_per_node"]) if obj.get("memory_per_node") is not None else None,
            "minimum_cpus_per_node": V0039Uint16NoVal.from_dict(obj["minimum_cpus_per_node"]) if obj.get("minimum_cpus_per_node") is not None else None,
            "minimum_tmp_disk_per_node": V0039Uint32NoVal.from_dict(obj["minimum_tmp_disk_per_node"]) if obj.get("minimum_tmp_disk_per_node") is not None else None,
            "power": V0039JobInfoPower.from_dict(obj["power"]) if obj.get("power") is not None else None,
            "preempt_time": obj.get("preempt_time"),
            "preemptable_time": obj.get("preemptable_time"),
            "pre_sus_time": obj.get("pre_sus_time"),
            "hold": obj.get("hold"),
            "priority": V0039Uint32NoVal.from_dict(obj["priority"]) if obj.get("priority") is not None else None,
            "profile": obj.get("profile"),
            "qos": obj.get("qos"),
            "reboot": obj.get("reboot"),
            "required_nodes": obj.get("required_nodes"),
            "minimum_switches": obj.get("minimum_switches"),
            "requeue": obj.get("requeue"),
            "resize_time": obj.get("resize_time"),
            "restart_cnt": obj.get("restart_cnt"),
            "resv_name": obj.get("resv_name"),
            "scheduled_nodes": obj.get("scheduled_nodes"),
            "selinux_context": obj.get("selinux_context"),
            "shared": obj.get("shared"),
            "exclusive": obj.get("exclusive"),
            "oversubscribe": obj.get("oversubscribe"),
            "show_flags": obj.get("show_flags"),
            "sockets_per_board": obj.get("sockets_per_board"),
            "sockets_per_node": V0039Uint16NoVal.from_dict(obj["sockets_per_node"]) if obj.get("sockets_per_node") is not None else None,
            "start_time": obj.get("start_time"),
            "state_description": obj.get("state_description"),
            "state_reason": obj.get("state_reason"),
            "standard_error": obj.get("standard_error"),
            "standard_input": obj.get("standard_input"),
            "standard_output": obj.get("standard_output"),
            "submit_time": obj.get("submit_time"),
            "suspend_time": obj.get("suspend_time"),
            "system_comment": obj.get("system_comment"),
            "time_limit": V0039Uint32NoVal.from_dict(obj["time_limit"]) if obj.get("time_limit") is not None else None,
            "time_minimum": V0039Uint32NoVal.from_dict(obj["time_minimum"]) if obj.get("time_minimum") is not None else None,
            "threads_per_core": V0039Uint16NoVal.from_dict(obj["threads_per_core"]) if obj.get("threads_per_core") is not None else None,
            "tres_bind": obj.get("tres_bind"),
            "tres_freq": obj.get("tres_freq"),
            "tres_per_job": obj.get("tres_per_job"),
            "tres_per_node": obj.get("tres_per_node"),
            "tres_per_socket": obj.get("tres_per_socket"),
            "tres_per_task": obj.get("tres_per_task"),
            "tres_req_str": obj.get("tres_req_str"),
            "tres_alloc_str": obj.get("tres_alloc_str"),
            "user_id": obj.get("user_id"),
            "user_name": obj.get("user_name"),
            "maximum_switch_wait_time": obj.get("maximum_switch_wait_time"),
            "wckey": obj.get("wckey"),
            "current_working_directory": obj.get("current_working_directory")
        })
        return _obj

