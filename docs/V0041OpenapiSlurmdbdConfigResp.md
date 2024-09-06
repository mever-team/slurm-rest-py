# V0041OpenapiSlurmdbdConfigResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**List[V0041OpenapiSlurmdbdConfigRespClustersInner]**](V0041OpenapiSlurmdbdConfigRespClustersInner.md) | clusters | [optional] 
**tres** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | tres | [optional] 
**accounts** | [**List[V0041OpenapiSlurmdbdConfigRespAccountsInner]**](V0041OpenapiSlurmdbdConfigRespAccountsInner.md) | accounts | [optional] 
**users** | [**List[V0041OpenapiSlurmdbdConfigRespUsersInner]**](V0041OpenapiSlurmdbdConfigRespUsersInner.md) | users | [optional] 
**qos** | [**List[V0041OpenapiSlurmdbdConfigRespQosInner]**](V0041OpenapiSlurmdbdConfigRespQosInner.md) | qos | [optional] 
**wckeys** | [**List[V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner]**](V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner.md) | wckeys | [optional] 
**associations** | [**List[V0041OpenapiSlurmdbdConfigRespAssociationsInner]**](V0041OpenapiSlurmdbdConfigRespAssociationsInner.md) | associations | [optional] 
**instances** | [**List[V0041OpenapiSlurmdbdConfigRespInstancesInner]**](V0041OpenapiSlurmdbdConfigRespInstancesInner.md) | instances | [optional] 
**meta** | [**V0041OpenapiSlurmdbdJobsRespMeta**](V0041OpenapiSlurmdbdJobsRespMeta.md) |  | [optional] 
**errors** | [**List[V0041OpenapiSlurmdbdJobsRespErrorsInner]**](V0041OpenapiSlurmdbdJobsRespErrorsInner.md) | Query errors | [optional] 
**warnings** | [**List[V0041OpenapiSlurmdbdJobsRespWarningsInner]**](V0041OpenapiSlurmdbdJobsRespWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_slurmdbd_config_resp import V0041OpenapiSlurmdbdConfigResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigResp from a JSON string
v0041_openapi_slurmdbd_config_resp_instance = V0041OpenapiSlurmdbdConfigResp.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigResp.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_dict = v0041_openapi_slurmdbd_config_resp_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigResp from a dict
v0041_openapi_slurmdbd_config_resp_from_dict = V0041OpenapiSlurmdbdConfigResp.from_dict(v0041_openapi_slurmdbd_config_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


