# V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation


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
from slurm_rest.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_association import V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_association_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_association_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_association_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_association_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerAssociation.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


