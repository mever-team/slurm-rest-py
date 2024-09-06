# V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elapsed** | **int** |  | [optional] 
**end** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu**](V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu.md) |  | [optional] 
**start** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu**](V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu.md) |  | [optional] 
**suspended** | **int** |  | [optional] 
**system** | [**V0040StepTimeSystem**](V0040StepTimeSystem.md) |  | [optional] 
**total** | [**V0040StepTimeSystem**](V0040StepTimeSystem.md) |  | [optional] 
**user** | [**V0040StepTimeSystem**](V0040StepTimeSystem.md) |  | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time import V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTime.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


