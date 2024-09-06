# V0041OpenapiJobSubmitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**V0041OpenapiJobSubmitResponseResult**](V0041OpenapiJobSubmitResponseResult.md) |  | [optional] 
**job_id** | **int** | submited JobId | [optional] 
**step_id** | **str** | submited StepID | [optional] 
**job_submit_user_msg** | **str** | job submision user message | [optional] 
**meta** | [**V0041OpenapiSlurmdbdJobsRespMeta**](V0041OpenapiSlurmdbdJobsRespMeta.md) |  | [optional] 
**errors** | [**List[V0041OpenapiSlurmdbdJobsRespErrorsInner]**](V0041OpenapiSlurmdbdJobsRespErrorsInner.md) | Query errors | [optional] 
**warnings** | [**List[V0041OpenapiSlurmdbdJobsRespWarningsInner]**](V0041OpenapiSlurmdbdJobsRespWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_job_submit_response import V0041OpenapiJobSubmitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiJobSubmitResponse from a JSON string
v0041_openapi_job_submit_response_instance = V0041OpenapiJobSubmitResponse.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiJobSubmitResponse.to_json())

# convert the object into a dict
v0041_openapi_job_submit_response_dict = v0041_openapi_job_submit_response_instance.to_dict()
# create an instance of V0041OpenapiJobSubmitResponse from a dict
v0041_openapi_job_submit_response_from_dict = V0041OpenapiJobSubmitResponse.from_dict(v0041_openapi_job_submit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


