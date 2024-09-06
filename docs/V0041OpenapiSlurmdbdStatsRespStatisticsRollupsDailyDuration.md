# V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDailyDuration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last** | **int** | total time spent doing daily daily rollup (seconds) | [optional] 
**max** | **int** | longest daily rollup time (seconds) | [optional] 
**time** | **int** | total time spent doing daily rollups (seconds) | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_slurmdbd_stats_resp_statistics_rollups_daily_duration import V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDailyDuration

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDailyDuration from a JSON string
v0041_openapi_slurmdbd_stats_resp_statistics_rollups_daily_duration_instance = V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDailyDuration.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDailyDuration.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_stats_resp_statistics_rollups_daily_duration_dict = v0041_openapi_slurmdbd_stats_resp_statistics_rollups_daily_duration_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDailyDuration from a dict
v0041_openapi_slurmdbd_stats_resp_statistics_rollups_daily_duration_from_dict = V0041OpenapiSlurmdbdStatsRespStatisticsRollupsDailyDuration.from_dict(v0041_openapi_slurmdbd_stats_resp_statistics_rollups_daily_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


