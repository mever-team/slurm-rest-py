# V0041OpenapiSlurmdbdJobsRespJobsInnerArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** |  | [optional] 
**limits** | [**V0040JobArrayLimits**](V0040JobArrayLimits.md) |  | [optional] 
**task_id** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId**](V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId.md) |  | [optional] 
**task** | **str** |  | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_array import V0041OpenapiSlurmdbdJobsRespJobsInnerArray

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerArray from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_array_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerArray.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerArray.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_array_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_array_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerArray from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_array_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerArray.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


