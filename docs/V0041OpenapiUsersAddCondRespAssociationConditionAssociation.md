# V0041OpenapiUsersAddCondRespAssociationConditionAssociation

Association limits and options

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment for the association | [optional] 
**defaultqos** | **str** | Which QOS id is this association default | [optional] 
**grpjobs** | [**V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpjobs**](V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpjobs.md) |  | [optional] 
**grpjobsaccrue** | [**V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpjobsaccrue**](V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpjobsaccrue.md) |  | [optional] 
**grpsubmitjobs** | [**V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpsubmitjobs**](V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpsubmitjobs.md) |  | [optional] 
**grptres** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) |  | [optional] 
**grptresmins** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | Max number of cpu minutes the underlying group of associations can run for | [optional] 
**grptresrunmins** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | Max number of cpu minutes the underlying group of associations can having running at one time | [optional] 
**grpwall** | [**V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpwall**](V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpwall.md) |  | [optional] 
**maxjobs** | [**V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxjobs**](V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxjobs.md) |  | [optional] 
**maxjobsaccrue** | [**V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxjobsaccrue**](V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxjobsaccrue.md) |  | [optional] 
**maxsubmitjobs** | [**V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxsubmitjobs**](V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxsubmitjobs.md) |  | [optional] 
**maxtresminsperjob** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | Max number of cpu minutes this association can have per job | [optional] 
**maxtresrunmins** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | Max number of cpu minutes this association can having running at one time | [optional] 
**maxtresperjob** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | Max number of cpus this association can allocate per job | [optional] 
**maxtrespernode** | [**List[V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner]**](V0041OpenapiSlurmdbdJobsRespJobsInnerStepsInnerTresRequestedMaxInner.md) | Max number of TRES this association can allocate per node | [optional] 
**maxwalldurationperjob** | [**V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxwalldurationperjob**](V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxwalldurationperjob.md) |  | [optional] 
**minpriothresh** | [**V0041OpenapiUsersAddCondRespAssociationConditionAssociationMinpriothresh**](V0041OpenapiUsersAddCondRespAssociationConditionAssociationMinpriothresh.md) |  | [optional] 
**parent** | **str** | Name of parent account | [optional] 
**priority** | [**V0041OpenapiUsersAddCondRespAssociationConditionAssociationPriority**](V0041OpenapiUsersAddCondRespAssociationConditionAssociationPriority.md) |  | [optional] 
**qoslevel** | **List[str]** | Default QoS&#39; that jobs are able to run at for this association | [optional] 
**fairshare** | **int** | Number of shares allocated to this association | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_users_add_cond_resp_association_condition_association import V0041OpenapiUsersAddCondRespAssociationConditionAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiUsersAddCondRespAssociationConditionAssociation from a JSON string
v0041_openapi_users_add_cond_resp_association_condition_association_instance = V0041OpenapiUsersAddCondRespAssociationConditionAssociation.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiUsersAddCondRespAssociationConditionAssociation.to_json())

# convert the object into a dict
v0041_openapi_users_add_cond_resp_association_condition_association_dict = v0041_openapi_users_add_cond_resp_association_condition_association_instance.to_dict()
# create an instance of V0041OpenapiUsersAddCondRespAssociationConditionAssociation from a dict
v0041_openapi_users_add_cond_resp_association_condition_association_from_dict = V0041OpenapiUsersAddCondRespAssociationConditionAssociation.from_dict(v0041_openapi_users_add_cond_resp_association_condition_association_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


