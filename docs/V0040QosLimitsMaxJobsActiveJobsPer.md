# V0040QosLimitsMaxJobsActiveJobsPer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**user** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 

## Example

```python
from slurm_rest.models.v0040_qos_limits_max_jobs_active_jobs_per import V0040QosLimitsMaxJobsActiveJobsPer

# TODO update the JSON string below
json = "{}"
# create an instance of V0040QosLimitsMaxJobsActiveJobsPer from a JSON string
v0040_qos_limits_max_jobs_active_jobs_per_instance = V0040QosLimitsMaxJobsActiveJobsPer.from_json(json)
# print the JSON string representation of the object
print(V0040QosLimitsMaxJobsActiveJobsPer.to_json())

# convert the object into a dict
v0040_qos_limits_max_jobs_active_jobs_per_dict = v0040_qos_limits_max_jobs_active_jobs_per_instance.to_dict()
# create an instance of V0040QosLimitsMaxJobsActiveJobsPer from a dict
v0040_qos_limits_max_jobs_active_jobs_per_from_dict = V0040QosLimitsMaxJobsActiveJobsPer.from_dict(v0040_qos_limits_max_jobs_active_jobs_per_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


