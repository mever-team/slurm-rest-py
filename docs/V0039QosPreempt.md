# V0039QosPreempt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | **List[str]** |  | [optional] 
**mode** | **List[str]** |  | [optional] 
**exempt_time** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 

## Example

```python
from slurm_rest.models.v0039_qos_preempt import V0039QosPreempt

# TODO update the JSON string below
json = "{}"
# create an instance of V0039QosPreempt from a JSON string
v0039_qos_preempt_instance = V0039QosPreempt.from_json(json)
# print the JSON string representation of the object
print(V0039QosPreempt.to_json())

# convert the object into a dict
v0039_qos_preempt_dict = v0039_qos_preempt_instance.to_dict()
# create an instance of V0039QosPreempt from a dict
v0039_qos_preempt_from_dict = V0039QosPreempt.from_dict(v0039_qos_preempt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


