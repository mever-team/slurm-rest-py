# V0041OpenapiNodesRespNodesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** |  | [optional] 
**burstbuffer_network_address** | **str** |  | [optional] 
**boards** | **int** |  | [optional] 
**boot_time** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu**](V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu.md) |  | [optional] 
**cluster_name** | **str** |  | [optional] 
**cores** | **int** |  | [optional] 
**specialized_cores** | **int** |  | [optional] 
**cpu_binding** | **int** |  | [optional] 
**cpu_load** | **int** |  | [optional] 
**free_mem** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu**](V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu.md) |  | [optional] 
**cpus** | **int** |  | [optional] 
**effective_cpus** | **int** |  | [optional] 
**specialized_cpus** | **str** |  | [optional] 
**energy** | [**V0041OpenapiNodesRespNodesInnerEnergy**](V0041OpenapiNodesRespNodesInnerEnergy.md) |  | [optional] 
**external_sensors** | **object** |  | [optional] 
**extra** | **str** |  | [optional] 
**power** | **object** |  | [optional] 
**features** | **List[str]** |  | [optional] 
**active_features** | **List[str]** |  | [optional] 
**gpu_spec** | **str** |  | [optional] 
**gres** | **str** |  | [optional] 
**gres_drained** | **str** |  | [optional] 
**gres_used** | **str** |  | [optional] 
**instance_id** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 
**last_busy** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu**](V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu.md) |  | [optional] 
**mcs_label** | **str** |  | [optional] 
**specialized_memory** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**next_state_after_reboot** | **List[str]** |  | [optional] 
**address** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**state** | **List[str]** |  | [optional] 
**operating_system** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**partitions** | **List[str]** |  | [optional] 
**port** | **int** |  | [optional] 
**real_memory** | **int** |  | [optional] 
**res_cores_per_gpu** | **int** |  | [optional] 
**comment** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**reason_changed_at** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu**](V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu.md) |  | [optional] 
**reason_set_by_user** | **str** |  | [optional] 
**resume_after** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu**](V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu.md) |  | [optional] 
**reservation** | **str** |  | [optional] 
**alloc_memory** | **int** |  | [optional] 
**alloc_cpus** | **int** |  | [optional] 
**alloc_idle_cpus** | **int** |  | [optional] 
**tres_used** | **str** |  | [optional] 
**tres_weighted** | **float** |  | [optional] 
**slurmd_start_time** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu**](V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu.md) |  | [optional] 
**sockets** | **int** |  | [optional] 
**threads** | **int** |  | [optional] 
**temporary_disk** | **int** |  | [optional] 
**weight** | **int** |  | [optional] 
**tres** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_nodes_resp_nodes_inner import V0041OpenapiNodesRespNodesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiNodesRespNodesInner from a JSON string
v0041_openapi_nodes_resp_nodes_inner_instance = V0041OpenapiNodesRespNodesInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiNodesRespNodesInner.to_json())

# convert the object into a dict
v0041_openapi_nodes_resp_nodes_inner_dict = v0041_openapi_nodes_resp_nodes_inner_instance.to_dict()
# create an instance of V0041OpenapiNodesRespNodesInner from a dict
v0041_openapi_nodes_resp_nodes_inner_from_dict = V0041OpenapiNodesRespNodesInner.from_dict(v0041_openapi_nodes_resp_nodes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


