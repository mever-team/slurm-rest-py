# V0041OpenapiSlurmdbdJobsRespJobsInnerHet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** |  | [optional] 
**job_offset** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId**](V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId.md) |  | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_het import V0041OpenapiSlurmdbdJobsRespJobsInnerHet

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerHet from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_het_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerHet.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerHet.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_het_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_het_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerHet from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_het_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerHet.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_het_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


