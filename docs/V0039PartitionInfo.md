# V0039PartitionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**V0040PartitionInfoNodes**](V0040PartitionInfoNodes.md) |  | [optional] 
**accounts** | [**V0040PartitionInfoAccounts**](V0040PartitionInfoAccounts.md) |  | [optional] 
**groups** | [**V0040PartitionInfoGroups**](V0040PartitionInfoGroups.md) |  | [optional] 
**qos** | [**V0040PartitionInfoQos**](V0040PartitionInfoQos.md) |  | [optional] 
**alternate** | **str** |  | [optional] 
**tres** | [**V0040PartitionInfoTres**](V0040PartitionInfoTres.md) |  | [optional] 
**cluster** | **str** |  | [optional] 
**cpus** | [**V0040PartitionInfoCpus**](V0040PartitionInfoCpus.md) |  | [optional] 
**defaults** | [**V0039PartitionInfoDefaults**](V0039PartitionInfoDefaults.md) |  | [optional] 
**grace_time** | **int** |  | [optional] 
**maximums** | [**V0039PartitionInfoMaximums**](V0039PartitionInfoMaximums.md) |  | [optional] 
**minimums** | [**V0040PartitionInfoMinimums**](V0040PartitionInfoMinimums.md) |  | [optional] 
**name** | **str** |  | [optional] 
**node_sets** | **str** |  | [optional] 
**priority** | [**V0040PartitionInfoPriority**](V0040PartitionInfoPriority.md) |  | [optional] 
**timeouts** | [**V0039PartitionInfoTimeouts**](V0039PartitionInfoTimeouts.md) |  | [optional] 
**suspend_time** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 

## Example

```python
from slurm_rest.models.v0039_partition_info import V0039PartitionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V0039PartitionInfo from a JSON string
v0039_partition_info_instance = V0039PartitionInfo.from_json(json)
# print the JSON string representation of the object
print(V0039PartitionInfo.to_json())

# convert the object into a dict
v0039_partition_info_dict = v0039_partition_info_instance.to_dict()
# create an instance of V0039PartitionInfo from a dict
v0039_partition_info_from_dict = V0039PartitionInfo.from_dict(v0039_partition_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


