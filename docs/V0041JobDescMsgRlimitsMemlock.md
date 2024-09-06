# V0041JobDescMsgRlimitsMemlock

Locked-in-memory address space

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set. False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite. \&quot;set\&quot; and \&quot;number\&quot; will be ignored. | [optional] 
**number** | **int** | If set is True the number will be set with value. Otherwise ignore number contents. | [optional] 

## Example

```python
from slurm_rest.models.v0041_job_desc_msg_rlimits_memlock import V0041JobDescMsgRlimitsMemlock

# TODO update the JSON string below
json = "{}"
# create an instance of V0041JobDescMsgRlimitsMemlock from a JSON string
v0041_job_desc_msg_rlimits_memlock_instance = V0041JobDescMsgRlimitsMemlock.from_json(json)
# print the JSON string representation of the object
print(V0041JobDescMsgRlimitsMemlock.to_json())

# convert the object into a dict
v0041_job_desc_msg_rlimits_memlock_dict = v0041_job_desc_msg_rlimits_memlock_instance.to_dict()
# create an instance of V0041JobDescMsgRlimitsMemlock from a dict
v0041_job_desc_msg_rlimits_memlock_from_dict = V0041JobDescMsgRlimitsMemlock.from_dict(v0041_job_desc_msg_rlimits_memlock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


