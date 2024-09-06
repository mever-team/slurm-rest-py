# V0040ReservationCoreSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node** | **str** |  | [optional] 
**core** | **str** |  | [optional] 

## Example

```python
from slurm_rest.models.v0040_reservation_core_spec import V0040ReservationCoreSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V0040ReservationCoreSpec from a JSON string
v0040_reservation_core_spec_instance = V0040ReservationCoreSpec.from_json(json)
# print the JSON string representation of the object
print(V0040ReservationCoreSpec.to_json())

# convert the object into a dict
v0040_reservation_core_spec_dict = v0040_reservation_core_spec_instance.to_dict()
# create an instance of V0040ReservationCoreSpec from a dict
v0040_reservation_core_spec_from_dict = V0040ReservationCoreSpec.from_dict(v0040_reservation_core_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


