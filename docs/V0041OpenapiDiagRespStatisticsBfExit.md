# V0041OpenapiDiagRespStatisticsBfExit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_job_queue** | **int** |  | [optional] 
**bf_max_job_start** | **int** |  | [optional] 
**bf_max_job_test** | **int** |  | [optional] 
**bf_max_time** | **int** |  | [optional] 
**bf_node_space_size** | **int** |  | [optional] 
**state_changed** | **int** |  | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_diag_resp_statistics_bf_exit import V0041OpenapiDiagRespStatisticsBfExit

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiDiagRespStatisticsBfExit from a JSON string
v0041_openapi_diag_resp_statistics_bf_exit_instance = V0041OpenapiDiagRespStatisticsBfExit.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiDiagRespStatisticsBfExit.to_json())

# convert the object into a dict
v0041_openapi_diag_resp_statistics_bf_exit_dict = v0041_openapi_diag_resp_statistics_bf_exit_instance.to_dict()
# create an instance of V0041OpenapiDiagRespStatisticsBfExit from a dict
v0041_openapi_diag_resp_statistics_bf_exit_from_dict = V0041OpenapiDiagRespStatisticsBfExit.from_dict(v0041_openapi_diag_resp_statistics_bf_exit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


