# V0041OpenapiSlurmdbdJobsRespJobsInnerTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsed** | **int** |  | [optional] 
**eligible** | **int** |  | [optional] 
**end** | **int** |  | [optional] 
**planned** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerTimePlanned**](V0041OpenapiSlurmdbdJobsRespJobsInnerTimePlanned.md) |  | [optional] 
**start** | **int** |  | [optional] 
**submission** | **int** |  | [optional] 
**suspended** | **int** |  | [optional] 
**system** | [**V0040JobTimeSystem**](V0040JobTimeSystem.md) |  | [optional] 
**limit** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId**](V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId.md) |  | [optional] 
**total** | [**V0040JobTimeSystem**](V0040JobTimeSystem.md) |  | [optional] 
**user** | [**V0040JobTimeSystem**](V0040JobTimeSystem.md) |  | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time import V0041OpenapiSlurmdbdJobsRespJobsInnerTime

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerTime from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerTime.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerTime.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerTime from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerTime.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


