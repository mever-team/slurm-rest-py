# V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per** | [**V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsPer**](V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsPer.md) |  | [optional] 
**active** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId**](V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId.md) |  | [optional] 
**accruing** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId**](V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId.md) |  | [optional] 
**total** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId**](V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId.md) |  | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_slurmdbd_config_resp_associations_inner_max_jobs import V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobs

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobs from a JSON string
v0041_openapi_slurmdbd_config_resp_associations_inner_max_jobs_instance = V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobs.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobs.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_associations_inner_max_jobs_dict = v0041_openapi_slurmdbd_config_resp_associations_inner_max_jobs_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobs from a dict
v0041_openapi_slurmdbd_config_resp_associations_inner_max_jobs_from_dict = V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobs.from_dict(v0041_openapi_slurmdbd_config_resp_associations_inner_max_jobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


