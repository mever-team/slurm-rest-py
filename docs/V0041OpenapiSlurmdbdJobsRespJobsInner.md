# V0041OpenapiSlurmdbdJobsRespJobsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** |  | [optional] 
**comment** | [**V0040JobComment**](V0040JobComment.md) |  | [optional] 
**allocation_nodes** | **int** |  | [optional] 
**array** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerArray**](V0041OpenapiSlurmdbdJobsRespJobsInnerArray.md) |  | [optional] 
**association** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation**](V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation.md) |  | [optional] 
**block** | **str** |  | [optional] 
**cluster** | **str** |  | [optional] 
**constraints** | **str** |  | [optional] 
**container** | **str** |  | [optional] 
**derived_exit_code** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerDerivedExitCode**](V0041OpenapiSlurmdbdJobsRespJobsInnerDerivedExitCode.md) |  | [optional] 
**time** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerTime**](V0041OpenapiSlurmdbdJobsRespJobsInnerTime.md) |  | [optional] 
**exit_code** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerDerivedExitCode**](V0041OpenapiSlurmdbdJobsRespJobsInnerDerivedExitCode.md) |  | [optional] 
**extra** | **str** |  | [optional] 
**failed_node** | **str** |  | [optional] 
**flags** | **List[str]** |  | [optional] 
**group** | **str** |  | [optional] 
**het** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerHet**](V0041OpenapiSlurmdbdJobsRespJobsInnerHet.md) |  | [optional] 
**job_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**licenses** | **str** |  | [optional] 
**mcs** | [**V0040JobMcs**](V0040JobMcs.md) |  | [optional] 
**nodes** | **str** |  | [optional] 
**partition** | **str** |  | [optional] 
**hold** | **bool** | Hold (true) or release (false) job | [optional] 
**priority** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerPriority**](V0041OpenapiSlurmdbdJobsRespJobsInnerPriority.md) |  | [optional] 
**qos** | **str** |  | [optional] 
**required** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerRequired**](V0041OpenapiSlurmdbdJobsRespJobsInnerRequired.md) |  | [optional] 
**kill_request_user** | **str** |  | [optional] 
**reservation** | [**V0040JobReservation**](V0040JobReservation.md) |  | [optional] 
**script** | **str** |  | [optional] 
**stdin_expanded** | **str** | Job stdin with expanded fields | [optional] 
**stdout_expanded** | **str** | Job stdout with expanded fields | [optional] 
**stderr_expanded** | **str** | Job stderr with expanded fields | [optional] 
**stdout** | **str** |  | [optional] 
**stderr** | **str** |  | [optional] 
**stdin** | **str** |  | [optional] 
**state** | [**V0040JobState**](V0040JobState.md) |  | [optional] 
**steps** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInner.md) |  | [optional] 
**submit_line** | **str** |  | [optional] 
**tres** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerTres**](V0041OpenapiSlurmdbdJobsRespJobsInnerTres.md) |  | [optional] 
**used_gres** | **str** |  | [optional] 
**user** | **str** |  | [optional] 
**wckey** | [**V0041OpenapiSlurmdbdJobsRespJobsInnerWckey**](V0041OpenapiSlurmdbdJobsRespJobsInnerWckey.md) |  | [optional] 
**working_directory** | **str** |  | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner import V0041OpenapiSlurmdbdJobsRespJobsInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInner from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_instance = V0041OpenapiSlurmdbdJobsRespJobsInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInner.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInner from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInner.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


