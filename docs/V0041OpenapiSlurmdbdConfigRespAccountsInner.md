# V0041OpenapiSlurmdbdConfigRespAccountsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associations** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation]**](V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation.md) |  | [optional] 
**coordinators** | [**List[V0041OpenapiSlurmdbdConfigRespAccountsInnerCoordinatorsInner]**](V0041OpenapiSlurmdbdConfigRespAccountsInnerCoordinatorsInner.md) |  | [optional] 
**description** | **str** |  | 
**name** | **str** |  | 
**organization** | **str** |  | 
**flags** | **List[str]** |  | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_slurmdbd_config_resp_accounts_inner import V0041OpenapiSlurmdbdConfigRespAccountsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespAccountsInner from a JSON string
v0041_openapi_slurmdbd_config_resp_accounts_inner_instance = V0041OpenapiSlurmdbdConfigRespAccountsInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespAccountsInner.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_accounts_inner_dict = v0041_openapi_slurmdbd_config_resp_accounts_inner_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespAccountsInner from a dict
v0041_openapi_slurmdbd_config_resp_accounts_inner_from_dict = V0041OpenapiSlurmdbdConfigRespAccountsInner.from_dict(v0041_openapi_slurmdbd_config_resp_accounts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


