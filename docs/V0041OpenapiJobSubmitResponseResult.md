# V0041OpenapiJobSubmitResponseResult

Job submission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** |  | [optional] 
**step_id** | **str** |  | [optional] 
**error_code** | **int** |  | [optional] 
**error** | **str** |  | [optional] 
**job_submit_user_msg** | **str** |  | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_job_submit_response_result import V0041OpenapiJobSubmitResponseResult

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiJobSubmitResponseResult from a JSON string
v0041_openapi_job_submit_response_result_instance = V0041OpenapiJobSubmitResponseResult.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiJobSubmitResponseResult.to_json())

# convert the object into a dict
v0041_openapi_job_submit_response_result_dict = v0041_openapi_job_submit_response_result_instance.to_dict()
# create an instance of V0041OpenapiJobSubmitResponseResult from a dict
v0041_openapi_job_submit_response_result_from_dict = V0041OpenapiJobSubmitResponseResult.from_dict(v0041_openapi_job_submit_response_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


