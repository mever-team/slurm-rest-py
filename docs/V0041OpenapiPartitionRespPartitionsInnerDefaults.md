# V0041OpenapiPartitionRespPartitionsInnerDefaults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_per_cpu** | **int** |  | [optional] 
**partition_memory_per_cpu** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu**](V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu.md) |  | [optional] 
**partition_memory_per_node** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu**](V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu.md) |  | [optional] 
**time** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId**](V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId.md) |  | [optional] 
**job** | **str** |  | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_partition_resp_partitions_inner_defaults import V0041OpenapiPartitionRespPartitionsInnerDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiPartitionRespPartitionsInnerDefaults from a JSON string
v0041_openapi_partition_resp_partitions_inner_defaults_instance = V0041OpenapiPartitionRespPartitionsInnerDefaults.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiPartitionRespPartitionsInnerDefaults.to_json())

# convert the object into a dict
v0041_openapi_partition_resp_partitions_inner_defaults_dict = v0041_openapi_partition_resp_partitions_inner_defaults_instance.to_dict()
# create an instance of V0041OpenapiPartitionRespPartitionsInnerDefaults from a dict
v0041_openapi_partition_resp_partitions_inner_defaults_from_dict = V0041OpenapiPartitionRespPartitionsInnerDefaults.from_dict(v0041_openapi_partition_resp_partitions_inner_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


