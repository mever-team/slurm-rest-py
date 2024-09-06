# V0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore

Number of processor threads per CPU core

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set. False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite. \&quot;set\&quot; and \&quot;number\&quot; will be ignored. | [optional] 
**number** | **int** | If set is True the number will be set with value. Otherwise ignore number contents. | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_job_info_resp_jobs_inner_job_resources_threads_per_core import V0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore from a JSON string
v0041_openapi_job_info_resp_jobs_inner_job_resources_threads_per_core_instance = V0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore.to_json())

# convert the object into a dict
v0041_openapi_job_info_resp_jobs_inner_job_resources_threads_per_core_dict = v0041_openapi_job_info_resp_jobs_inner_job_resources_threads_per_core_instance.to_dict()
# create an instance of V0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore from a dict
v0041_openapi_job_info_resp_jobs_inner_job_resources_threads_per_core_from_dict = V0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore.from_dict(v0041_openapi_job_info_resp_jobs_inner_job_resources_threads_per_core_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


