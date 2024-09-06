# V0041UpdateNodeMsgResumeAfter

automatically resume DOWN or DRAINED node after this amount of seconds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set. False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite. \&quot;set\&quot; and \&quot;number\&quot; will be ignored. | [optional] 
**number** | **int** | If set is True the number will be set with value. Otherwise ignore number contents. | [optional] 

## Example

```python
from slurm_rest.models.v0041_update_node_msg_resume_after import V0041UpdateNodeMsgResumeAfter

# TODO update the JSON string below
json = "{}"
# create an instance of V0041UpdateNodeMsgResumeAfter from a JSON string
v0041_update_node_msg_resume_after_instance = V0041UpdateNodeMsgResumeAfter.from_json(json)
# print the JSON string representation of the object
print(V0041UpdateNodeMsgResumeAfter.to_json())

# convert the object into a dict
v0041_update_node_msg_resume_after_dict = v0041_update_node_msg_resume_after_instance.to_dict()
# create an instance of V0041UpdateNodeMsgResumeAfter from a dict
v0041_update_node_msg_resume_after_from_dict = V0041UpdateNodeMsgResumeAfter.from_dict(v0041_update_node_msg_resume_after_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


