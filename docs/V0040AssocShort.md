# V0040AssocShort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Association account (if assigned) | [optional] 
**cluster** | **str** | Association cluster (if assigned) | [optional] 
**partition** | **str** | Association partition (if assigned) | [optional] 
**user** | **str** | Assocation user (if assigned) | 
**id** | **int** | Numeric Association ID (if known) | [optional] 

## Example

```python
from slurm_rest.models.v0040_assoc_short import V0040AssocShort

# TODO update the JSON string below
json = "{}"
# create an instance of V0040AssocShort from a JSON string
v0040_assoc_short_instance = V0040AssocShort.from_json(json)
# print the JSON string representation of the object
print(V0040AssocShort.to_json())

# convert the object into a dict
v0040_assoc_short_dict = v0040_assoc_short_instance.to_dict()
# create an instance of V0040AssocShort from a dict
v0040_assoc_short_from_dict = V0040AssocShort.from_dict(v0040_assoc_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


