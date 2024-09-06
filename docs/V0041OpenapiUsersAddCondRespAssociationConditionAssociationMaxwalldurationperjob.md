# V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxwalldurationperjob

Longest time this association can run a job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set. False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite. \&quot;set\&quot; and \&quot;number\&quot; will be ignored. | [optional] 
**number** | **int** | If set is True the number will be set with value. Otherwise ignore number contents. | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_users_add_cond_resp_association_condition_association_maxwalldurationperjob import V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxwalldurationperjob

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxwalldurationperjob from a JSON string
v0041_openapi_users_add_cond_resp_association_condition_association_maxwalldurationperjob_instance = V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxwalldurationperjob.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxwalldurationperjob.to_json())

# convert the object into a dict
v0041_openapi_users_add_cond_resp_association_condition_association_maxwalldurationperjob_dict = v0041_openapi_users_add_cond_resp_association_condition_association_maxwalldurationperjob_instance.to_dict()
# create an instance of V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxwalldurationperjob from a dict
v0041_openapi_users_add_cond_resp_association_condition_association_maxwalldurationperjob_from_dict = V0041OpenapiUsersAddCondRespAssociationConditionAssociationMaxwalldurationperjob.from_dict(v0041_openapi_users_add_cond_resp_association_condition_association_maxwalldurationperjob_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


