# V0041UpdateNodeMsg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | arbitrary comment | [optional] 
**cpu_bind** | **int** | default CPU binding type | [optional] 
**extra** | **str** | arbitrary string | [optional] 
**features** | **List[str]** | new available feature for node | [optional] 
**features_act** | **List[str]** | new active feature for node | [optional] 
**gres** | **str** | new generic resources for node | [optional] 
**address** | **List[str]** | communication name | [optional] 
**hostname** | **List[str]** | node&#39;s hostname | [optional] 
**name** | **List[str]** | node to update | [optional] 
**state** | **List[str]** | assign new node state | [optional] 
**reason** | **str** | reason for node being DOWN or DRAINING | [optional] 
**reason_uid** | **str** | user ID of sending (needed if user root is sending message) | [optional] 
**resume_after** | [**V0041UpdateNodeMsgResumeAfter**](V0041UpdateNodeMsgResumeAfter.md) |  | [optional] 
**weight** | [**V0041UpdateNodeMsgWeight**](V0041UpdateNodeMsgWeight.md) |  | [optional] 

## Example

```python
from slurm_rest.models.v0041_update_node_msg import V0041UpdateNodeMsg

# TODO update the JSON string below
json = "{}"
# create an instance of V0041UpdateNodeMsg from a JSON string
v0041_update_node_msg_instance = V0041UpdateNodeMsg.from_json(json)
# print the JSON string representation of the object
print(V0041UpdateNodeMsg.to_json())

# convert the object into a dict
v0041_update_node_msg_dict = v0041_update_node_msg_instance.to_dict()
# create an instance of V0041UpdateNodeMsg from a dict
v0041_update_node_msg_from_dict = V0041UpdateNodeMsg.from_dict(v0041_update_node_msg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


