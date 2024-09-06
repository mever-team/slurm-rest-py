# V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxjobsaccrue

Max number of jobs this association can have accruing priority time

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set. False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite. \&quot;set\&quot; and \&quot;number\&quot; will be ignored. | [optional] 
**number** | **int** | If set is True the number will be set with value. Otherwise ignore number contents. | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_users_add_cond_resp_association_condition_association_maxjobsaccrue import V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxjobsaccrue

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxjobsaccrue from a JSON string
v0041_openapi_users_add_cond_resp_association_condition_association_maxjobsaccrue_instance = V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxjobsaccrue.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxjobsaccrue.to_json())

# convert the object into a dict
v0041_openapi_users_add_cond_resp_association_condition_association_maxjobsaccrue_dict = v0041_openapi_users_add_cond_resp_association_condition_association_maxjobsaccrue_instance.to_dict()
# create an instance of V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxjobsaccrue from a dict
v0041_openapi_users_add_cond_resp_association_condition_association_maxjobsaccrue_from_dict = V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxjobsaccrue.from_dict(v0041_openapi_users_add_cond_resp_association_condition_association_maxjobsaccrue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


