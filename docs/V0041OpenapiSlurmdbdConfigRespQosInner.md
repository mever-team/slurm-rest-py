# V0041OpenapiSlurmdbdConfigRespQosInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**id** | **int** |  | [optional] 
**limits** | [**V0041OpenapiSlurmdbdConfigRespQosInnerLimits**](V0041OpenapiSlurmdbdConfigRespQosInnerLimits.md) |  | [optional] 
**name** | **str** |  | [optional] 
**preempt** | [**V0041OpenapiSlurmdbdConfigRespQosInnerPreempt**](V0041OpenapiSlurmdbdConfigRespQosInnerPreempt.md) |  | [optional] 
**priority** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId**](V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId.md) |  | [optional] 
**usage_factor** | [**V0041OpenapiSlurmdbdConfigRespQosInnerLimitsFactor**](V0041OpenapiSlurmdbdConfigRespQosInnerLimitsFactor.md) |  | [optional] 
**usage_threshold** | [**V0041OpenapiSlurmdbdConfigRespQosInnerLimitsFactor**](V0041OpenapiSlurmdbdConfigRespQosInnerLimitsFactor.md) |  | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_slurmdbd_config_resp_qos_inner import V0041OpenapiSlurmdbdConfigRespQosInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInner from a JSON string
v0041_openapi_slurmdbd_config_resp_qos_inner_instance = V0041OpenapiSlurmdbdConfigRespQosInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespQosInner.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_dict = v0041_openapi_slurmdbd_config_resp_qos_inner_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInner from a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_from_dict = V0041OpenapiSlurmdbdConfigRespQosInner.from_dict(v0041_openapi_slurmdbd_config_resp_qos_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


