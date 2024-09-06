# V0041OpenapiWckeyRemovedResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_wckeys** | **List[str]** | deleted wckeys | 
**meta** | [**V0041OpenapiSlurmdbdJobsRespMeta**](V0041OpenapiSlurmdbdJobsRespMeta.md) |  | [optional] 
**errors** | [**List[V0041OpenapiSlurmdbdJobsRespErrorsInner]**](V0041OpenapiSlurmdbdJobsRespErrorsInner.md) | Query errors | [optional] 
**warnings** | [**List[V0041OpenapiSlurmdbdJobsRespWarningsInner]**](V0041OpenapiSlurmdbdJobsRespWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_wckey_removed_resp import V0041OpenapiWckeyRemovedResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiWckeyRemovedResp from a JSON string
v0041_openapi_wckey_removed_resp_instance = V0041OpenapiWckeyRemovedResp.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiWckeyRemovedResp.to_json())

# convert the object into a dict
v0041_openapi_wckey_removed_resp_dict = v0041_openapi_wckey_removed_resp_instance.to_dict()
# create an instance of V0041OpenapiWckeyRemovedResp from a dict
v0041_openapi_wckey_removed_resp_from_dict = V0041OpenapiWckeyRemovedResp.from_dict(v0041_openapi_wckey_removed_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


