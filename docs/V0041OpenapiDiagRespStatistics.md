# V0041OpenapiDiagRespStatistics

statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parts_packed** | **int** |  | [optional] 
**req_time** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu**](V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu.md) |  | [optional] 
**req_time_start** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu**](V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu.md) |  | [optional] 
**server_thread_count** | **int** |  | [optional] 
**agent_queue_size** | **int** |  | [optional] 
**agent_count** | **int** |  | [optional] 
**agent_thread_count** | **int** |  | [optional] 
**dbd_agent_queue_size** | **int** |  | [optional] 
**gettimeofday_latency** | **int** |  | [optional] 
**schedule_cycle_max** | **int** |  | [optional] 
**schedule_cycle_last** | **int** |  | [optional] 
**schedule_cycle_sum** | **int** |  | [optional] 
**schedule_cycle_total** | **int** |  | [optional] 
**schedule_cycle_mean** | **int** |  | [optional] 
**schedule_cycle_mean_depth** | **int** |  | [optional] 
**schedule_cycle_per_minute** | **int** |  | [optional] 
**schedule_cycle_depth** | **int** |  | [optional] 
**schedule_exit** | [**V0041OpenapiDiagRespStatisticsScheduleExit**](V0041OpenapiDiagRespStatisticsScheduleExit.md) |  | [optional] 
**schedule_queue_length** | **int** |  | [optional] 
**jobs_submitted** | **int** |  | [optional] 
**jobs_started** | **int** |  | [optional] 
**jobs_completed** | **int** |  | [optional] 
**jobs_canceled** | **int** |  | [optional] 
**jobs_failed** | **int** |  | [optional] 
**jobs_pending** | **int** |  | [optional] 
**jobs_running** | **int** |  | [optional] 
**job_states_ts** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu**](V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu.md) |  | [optional] 
**bf_backfilled_jobs** | **int** |  | [optional] 
**bf_last_backfilled_jobs** | **int** |  | [optional] 
**bf_backfilled_het_jobs** | **int** |  | [optional] 
**bf_cycle_counter** | **int** |  | [optional] 
**bf_cycle_mean** | **int** |  | [optional] 
**bf_depth_mean** | **int** |  | [optional] 
**bf_depth_mean_try** | **int** |  | [optional] 
**bf_cycle_sum** | **int** |  | [optional] 
**bf_cycle_last** | **int** |  | [optional] 
**bf_cycle_max** | **int** |  | [optional] 
**bf_exit** | [**V0041OpenapiDiagRespStatisticsBfExit**](V0041OpenapiDiagRespStatisticsBfExit.md) |  | [optional] 
**bf_last_depth** | **int** |  | [optional] 
**bf_last_depth_try** | **int** |  | [optional] 
**bf_depth_sum** | **int** |  | [optional] 
**bf_depth_try_sum** | **int** |  | [optional] 
**bf_queue_len** | **int** |  | [optional] 
**bf_queue_len_mean** | **int** |  | [optional] 
**bf_queue_len_sum** | **int** |  | [optional] 
**bf_table_size** | **int** |  | [optional] 
**bf_table_size_sum** | **int** |  | [optional] 
**bf_table_size_mean** | **int** |  | [optional] 
**bf_when_last_cycle** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu**](V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu.md) |  | [optional] 
**bf_active** | **bool** |  | [optional] 
**rpcs_by_message_type** | [**List[V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner]**](V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner.md) | RPCs by type | [optional] 
**rpcs_by_user** | [**List[V0041OpenapiDiagRespStatisticsRpcsByUserInner]**](V0041OpenapiDiagRespStatisticsRpcsByUserInner.md) | RPCs by user | [optional] 
**pending_rpcs** | [**List[V0041OpenapiDiagRespStatisticsPendingRpcsInner]**](V0041OpenapiDiagRespStatisticsPendingRpcsInner.md) | Pending RPC statistics | [optional] 
**pending_rpcs_by_hostlist** | [**List[V0041OpenapiDiagRespStatisticsPendingRpcsByHostlistInner]**](V0041OpenapiDiagRespStatisticsPendingRpcsByHostlistInner.md) | Pending RPCs hostlists | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_diag_resp_statistics import V0041OpenapiDiagRespStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiDiagRespStatistics from a JSON string
v0041_openapi_diag_resp_statistics_instance = V0041OpenapiDiagRespStatistics.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiDiagRespStatistics.to_json())

# convert the object into a dict
v0041_openapi_diag_resp_statistics_dict = v0041_openapi_diag_resp_statistics_instance.to_dict()
# create an instance of V0041OpenapiDiagRespStatistics from a dict
v0041_openapi_diag_resp_statistics_from_dict = V0041OpenapiDiagRespStatistics.from_dict(v0041_openapi_diag_resp_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


