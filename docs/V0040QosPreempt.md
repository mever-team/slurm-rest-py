# V0040QosPreempt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | **List[str]** |  | [optional] 
**mode** | **List[str]** |  | [optional] 
**exempt_time** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 

## Example

```python
from slurm_rest.models.v0040_qos_preempt import V0040QosPreempt

# TODO update the JSON string below
json = "{}"
# create an instance of V0040QosPreempt from a JSON string
v0040_qos_preempt_instance = V0040QosPreempt.from_json(json)
# print the JSON string representation of the object
print(V0040QosPreempt.to_json())

# convert the object into a dict
v0040_qos_preempt_dict = v0040_qos_preempt_instance.to_dict()
# create an instance of V0040QosPreempt from a dict
v0040_qos_preempt_from_dict = V0040QosPreempt.from_dict(v0040_qos_preempt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


