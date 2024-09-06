# V0041OpenapiReservationRespReservationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **str** |  | [optional] 
**burst_buffer** | **str** |  | [optional] 
**core_count** | **int** |  | [optional] 
**core_specializations** | [**List[V0041OpenapiReservationRespReservationsInnerCoreSpecializationsInner]**](V0041OpenapiReservationRespReservationsInnerCoreSpecializationsInner.md) |  | [optional] 
**end_time** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu**](V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu.md) |  | [optional] 
**features** | **str** |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**groups** | **str** |  | [optional] 
**licenses** | **str** |  | [optional] 
**max_start_delay** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**node_count** | **int** |  | [optional] 
**node_list** | **str** |  | [optional] 
**partition** | **str** |  | [optional] 
**purge_completed** | [**V0041OpenapiReservationRespReservationsInnerPurgeCompleted**](V0041OpenapiReservationRespReservationsInnerPurgeCompleted.md) |  | [optional] 
**start_time** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu**](V0041OpenapiSlurmdbdJobsRespJobsInnerRequiredMemoryPerCpu.md) |  | [optional] 
**watts** | [**V0041OpenapiReservationRespReservationsInnerWatts**](V0041OpenapiReservationRespReservationsInnerWatts.md) |  | [optional] 
**tres** | **str** |  | [optional] 
**users** | **str** |  | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_reservation_resp_reservations_inner import V0041OpenapiReservationRespReservationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiReservationRespReservationsInner from a JSON string
v0041_openapi_reservation_resp_reservations_inner_instance = V0041OpenapiReservationRespReservationsInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiReservationRespReservationsInner.to_json())

# convert the object into a dict
v0041_openapi_reservation_resp_reservations_inner_dict = v0041_openapi_reservation_resp_reservations_inner_instance.to_dict()
# create an instance of V0041OpenapiReservationRespReservationsInner from a dict
v0041_openapi_reservation_resp_reservations_inner_from_dict = V0041OpenapiReservationRespReservationsInner.from_dict(v0041_openapi_reservation_resp_reservations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


