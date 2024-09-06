# V0041OpenapiSlurmdbdConfigRespUsersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrator_level** | **List[str]** |  | [optional] 
**associations** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation]**](V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation.md) |  | [optional] 
**coordinators** | [**List[V0041OpenapiSlurmdbdConfigRespAccountsInnerCoordinatorsInner]**](V0041OpenapiSlurmdbdConfigRespAccountsInnerCoordinatorsInner.md) |  | [optional] 
**default** | [**V0040UserDefault**](V0040UserDefault.md) |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**name** | **str** |  | 
**old_name** | **str** |  | [optional] 
**wckeys** | [**List[V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner]**](V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner.md) |  | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_slurmdbd_config_resp_users_inner import V0041OpenapiSlurmdbdConfigRespUsersInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespUsersInner from a JSON string
v0041_openapi_slurmdbd_config_resp_users_inner_instance = V0041OpenapiSlurmdbdConfigRespUsersInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespUsersInner.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_users_inner_dict = v0041_openapi_slurmdbd_config_resp_users_inner_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespUsersInner from a dict
v0041_openapi_slurmdbd_config_resp_users_inner_from_dict = V0041OpenapiSlurmdbdConfigRespUsersInner.from_dict(v0041_openapi_slurmdbd_config_resp_users_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


