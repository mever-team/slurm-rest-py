# V0041OpenapiDiagRespStatisticsScheduleExit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_job_queue** | **int** |  | [optional] 
**default_queue_depth** | **int** |  | [optional] 
**max_job_start** | **int** |  | [optional] 
**max_rpc_cnt** | **int** |  | [optional] 
**max_sched_time** | **int** |  | [optional] 
**licenses** | **int** |  | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_diag_resp_statistics_schedule_exit import V0041OpenapiDiagRespStatisticsScheduleExit

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiDiagRespStatisticsScheduleExit from a JSON string
v0041_openapi_diag_resp_statistics_schedule_exit_instance = V0041OpenapiDiagRespStatisticsScheduleExit.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiDiagRespStatisticsScheduleExit.to_json())

# convert the object into a dict
v0041_openapi_diag_resp_statistics_schedule_exit_dict = v0041_openapi_diag_resp_statistics_schedule_exit_instance.to_dict()
# create an instance of V0041OpenapiDiagRespStatisticsScheduleExit from a dict
v0041_openapi_diag_resp_statistics_schedule_exit_from_dict = V0041OpenapiDiagRespStatisticsScheduleExit.from_dict(v0041_openapi_diag_resp_statistics_schedule_exit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


