# V0041OpenapiNodesRespLastUpdate

time of last node change (UNIX timestamp)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set. False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite. \&quot;set\&quot; and \&quot;number\&quot; will be ignored. | [optional] 
**number** | **int** | If set is True the number will be set with value. Otherwise ignore number contents. | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_nodes_resp_last_update import V0041OpenapiNodesRespLastUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiNodesRespLastUpdate from a JSON string
v0041_openapi_nodes_resp_last_update_instance = V0041OpenapiNodesRespLastUpdate.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiNodesRespLastUpdate.to_json())

# convert the object into a dict
v0041_openapi_nodes_resp_last_update_dict = v0041_openapi_nodes_resp_last_update_instance.to_dict()
# create an instance of V0041OpenapiNodesRespLastUpdate from a dict
v0041_openapi_nodes_resp_last_update_from_dict = V0041OpenapiNodesRespLastUpdate.from_dict(v0041_openapi_nodes_resp_last_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


