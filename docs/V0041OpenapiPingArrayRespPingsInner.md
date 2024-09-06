# V0041OpenapiPingArrayRespPingsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** |  | [optional] 
**pinged** | **str** |  | [optional] 
**latency** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_ping_array_resp_pings_inner import V0041OpenapiPingArrayRespPingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiPingArrayRespPingsInner from a JSON string
v0041_openapi_ping_array_resp_pings_inner_instance = V0041OpenapiPingArrayRespPingsInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiPingArrayRespPingsInner.to_json())

# convert the object into a dict
v0041_openapi_ping_array_resp_pings_inner_dict = v0041_openapi_ping_array_resp_pings_inner_instance.to_dict()
# create an instance of V0041OpenapiPingArrayRespPingsInner from a dict
v0041_openapi_ping_array_resp_pings_inner_from_dict = V0041OpenapiPingArrayRespPingsInner.from_dict(v0041_openapi_ping_array_resp_pings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


