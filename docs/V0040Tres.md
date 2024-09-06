# V0040Tres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from slurm_rest.models.v0040_tres import V0040Tres

# TODO update the JSON string below
json = "{}"
# create an instance of V0040Tres from a JSON string
v0040_tres_instance = V0040Tres.from_json(json)
# print the JSON string representation of the object
print(V0040Tres.to_json())

# convert the object into a dict
v0040_tres_dict = v0040_tres_instance.to_dict()
# create an instance of V0040Tres from a dict
v0040_tres_from_dict = V0040Tres.from_dict(v0040_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


