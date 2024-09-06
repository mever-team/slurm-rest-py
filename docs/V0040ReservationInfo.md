# V0040ReservationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **str** |  | [optional] 
**burst_buffer** | **str** |  | [optional] 
**core_count** | **int** |  | [optional] 
**core_specializations** | [**List[V0040ReservationCoreSpec]**](V0040ReservationCoreSpec.md) |  | [optional] 
**end_time** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**features** | **str** |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**groups** | **str** |  | [optional] 
**licenses** | **str** |  | [optional] 
**max_start_delay** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**node_count** | **int** |  | [optional] 
**node_list** | **str** |  | [optional] 
**partition** | **str** |  | [optional] 
**purge_completed** | [**V0040ReservationInfoPurgeCompleted**](V0040ReservationInfoPurgeCompleted.md) |  | [optional] 
**start_time** | [**V0040Uint64NoVal**](V0040Uint64NoVal.md) |  | [optional] 
**watts** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**tres** | **str** |  | [optional] 
**users** | **str** |  | [optional] 

## Example

```python
from slurm_rest.models.v0040_reservation_info import V0040ReservationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V0040ReservationInfo from a JSON string
v0040_reservation_info_instance = V0040ReservationInfo.from_json(json)
# print the JSON string representation of the object
print(V0040ReservationInfo.to_json())

# convert the object into a dict
v0040_reservation_info_dict = v0040_reservation_info_instance.to_dict()
# create an instance of V0040ReservationInfo from a dict
v0040_reservation_info_from_dict = V0040ReservationInfo.from_dict(v0040_reservation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


