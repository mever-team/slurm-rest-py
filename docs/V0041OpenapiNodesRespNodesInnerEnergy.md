# V0041OpenapiNodesRespNodesInnerEnergy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_watts** | **int** |  | [optional] 
**base_consumed_energy** | **int** |  | [optional] 
**consumed_energy** | **int** |  | [optional] 
**current_watts** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId**](V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId.md) |  | [optional] 
**previous_consumed_energy** | **int** |  | [optional] 
**last_collected** | **int** |  | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_nodes_resp_nodes_inner_energy import V0041OpenapiNodesRespNodesInnerEnergy

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiNodesRespNodesInnerEnergy from a JSON string
v0041_openapi_nodes_resp_nodes_inner_energy_instance = V0041OpenapiNodesRespNodesInnerEnergy.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiNodesRespNodesInnerEnergy.to_json())

# convert the object into a dict
v0041_openapi_nodes_resp_nodes_inner_energy_dict = v0041_openapi_nodes_resp_nodes_inner_energy_instance.to_dict()
# create an instance of V0041OpenapiNodesRespNodesInnerEnergy from a dict
v0041_openapi_nodes_resp_nodes_inner_energy_from_dict = V0041OpenapiNodesRespNodesInnerEnergy.from_dict(v0041_openapi_nodes_resp_nodes_inner_energy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


