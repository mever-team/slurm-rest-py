# V0041OpenapiPartitionRespPartitionsInnerMaximums


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpus_per_node** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId**](V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId.md) |  | [optional] 
**cpus_per_socket** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId**](V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId.md) |  | [optional] 
**memory_per_cpu** | **int** |  | [optional] 
**partition_memory_per_cpu** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu**](V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu.md) |  | [optional] 
**partition_memory_per_node** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu**](V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu.md) |  | [optional] 
**nodes** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId**](V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId.md) |  | [optional] 
**shares** | **int** |  | [optional] 
**oversubscribe** | [**V0040PartitionInfoMaximumsOversubscribe**](V0040PartitionInfoMaximumsOversubscribe.md) |  | [optional] 
**time** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId**](V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId.md) |  | [optional] 
**over_time_limit** | [**V0041JobDescMsgDistributionPlaneSize**](V0041JobDescMsgDistributionPlaneSize.md) |  | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_partition_resp_partitions_inner_maximums import V0041OpenapiPartitionRespPartitionsInnerMaximums

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiPartitionRespPartitionsInnerMaximums from a JSON string
v0041_openapi_partition_resp_partitions_inner_maximums_instance = V0041OpenapiPartitionRespPartitionsInnerMaximums.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiPartitionRespPartitionsInnerMaximums.to_json())

# convert the object into a dict
v0041_openapi_partition_resp_partitions_inner_maximums_dict = v0041_openapi_partition_resp_partitions_inner_maximums_instance.to_dict()
# create an instance of V0041OpenapiPartitionRespPartitionsInnerMaximums from a dict
v0041_openapi_partition_resp_partitions_inner_maximums_from_dict = V0041OpenapiPartitionRespPartitionsInnerMaximums.from_dict(v0041_openapi_partition_resp_partitions_inner_maximums_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


