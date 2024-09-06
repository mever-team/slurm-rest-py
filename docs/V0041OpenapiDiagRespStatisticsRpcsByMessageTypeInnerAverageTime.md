# V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInnerAverageTime

Average time spent processing RPC in seconds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set. False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite. \&quot;set\&quot; and \&quot;number\&quot; will be ignored. | [optional] 
**number** | **int** | If set is True the number will be set with value. Otherwise ignore number contents. | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_diag_resp_statistics_rpcs_by_message_type_inner_average_time import V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInnerAverageTime

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInnerAverageTime from a JSON string
v0041_openapi_diag_resp_statistics_rpcs_by_message_type_inner_average_time_instance = V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInnerAverageTime.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInnerAverageTime.to_json())

# convert the object into a dict
v0041_openapi_diag_resp_statistics_rpcs_by_message_type_inner_average_time_dict = v0041_openapi_diag_resp_statistics_rpcs_by_message_type_inner_average_time_instance.to_dict()
# create an instance of V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInnerAverageTime from a dict
v0041_openapi_diag_resp_statistics_rpcs_by_message_type_inner_average_time_from_dict = V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInnerAverageTime.from_dict(v0041_openapi_diag_resp_statistics_rpcs_by_message_type_inner_average_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


