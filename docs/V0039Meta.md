# V0039Meta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugin** | [**V0039MetaPlugin**](V0039MetaPlugin.md) |  | [optional] 
**slurm** | [**V0039MetaSlurm**](V0039MetaSlurm.md) |  | [optional] 

## Example

```python
from slurm_rest.models.v0039_meta import V0039Meta

# TODO update the JSON string below
json = "{}"
# create an instance of V0039Meta from a JSON string
v0039_meta_instance = V0039Meta.from_json(json)
# print the JSON string representation of the object
print(V0039Meta.to_json())

# convert the object into a dict
v0039_meta_dict = v0039_meta_instance.to_dict()
# create an instance of V0039Meta from a dict
v0039_meta_from_dict = V0039Meta.from_dict(v0039_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


