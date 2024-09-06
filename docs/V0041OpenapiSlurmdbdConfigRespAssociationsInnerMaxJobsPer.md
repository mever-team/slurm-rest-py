# V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsPer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId**](V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId.md) |  | [optional] 
**accruing** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId**](V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId.md) |  | [optional] 
**submitted** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId**](V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId.md) |  | [optional] 
**wall_clock** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId**](V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId.md) |  | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_slurmdbd_config_resp_associations_inner_max_jobs_per import V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsPer

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsPer from a JSON string
v0041_openapi_slurmdbd_config_resp_associations_inner_max_jobs_per_instance = V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsPer.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsPer.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_associations_inner_max_jobs_per_dict = v0041_openapi_slurmdbd_config_resp_associations_inner_max_jobs_per_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsPer from a dict
v0041_openapi_slurmdbd_config_resp_associations_inner_max_jobs_per_from_dict = V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsPer.from_dict(v0041_openapi_slurmdbd_config_resp_associations_inner_max_jobs_per_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


