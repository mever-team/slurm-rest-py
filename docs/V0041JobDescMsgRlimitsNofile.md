# V0041JobDescMsgRlimitsNofile

Number of open files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set. False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite. \&quot;set\&quot; and \&quot;number\&quot; will be ignored. | [optional] 
**number** | **int** | If set is True the number will be set with value. Otherwise ignore number contents. | [optional] 

## Example

```python
from slurm_rest.models.v0041_job_desc_msg_rlimits_nofile import V0041JobDescMsgRlimitsNofile

# TODO update the JSON string below
json = "{}"
# create an instance of V0041JobDescMsgRlimitsNofile from a JSON string
v0041_job_desc_msg_rlimits_nofile_instance = V0041JobDescMsgRlimitsNofile.from_json(json)
# print the JSON string representation of the object
print(V0041JobDescMsgRlimitsNofile.to_json())

# convert the object into a dict
v0041_job_desc_msg_rlimits_nofile_dict = v0041_job_desc_msg_rlimits_nofile_instance.to_dict()
# create an instance of V0041JobDescMsgRlimitsNofile from a dict
v0041_job_desc_msg_rlimits_nofile_from_dict = V0041JobDescMsgRlimitsNofile.from_dict(v0041_job_desc_msg_rlimits_nofile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

