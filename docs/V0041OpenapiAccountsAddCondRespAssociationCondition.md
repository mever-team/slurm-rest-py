# V0041OpenapiAccountsAddCondRespAssociationCondition

CSV list of accounts, association limits and options, CSV list of clusters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **List[str]** | CSV accounts list | 
**association** | [**V0041OpenapiUsersAddCondRespAssociationConditionAssociation**](V0041OpenapiUsersAddCondRespAssociationConditionAssociation.md) |  | [optional] 
**clusters** | **List[str]** | CSV clusters list | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_accounts_add_cond_resp_association_condition import V0041OpenapiAccountsAddCondRespAssociationCondition

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiAccountsAddCondRespAssociationCondition from a JSON string
v0041_openapi_accounts_add_cond_resp_association_condition_instance = V0041OpenapiAccountsAddCondRespAssociationCondition.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiAccountsAddCondRespAssociationCondition.to_json())

# convert the object into a dict
v0041_openapi_accounts_add_cond_resp_association_condition_dict = v0041_openapi_accounts_add_cond_resp_association_condition_instance.to_dict()
# create an instance of V0041OpenapiAccountsAddCondRespAssociationCondition from a dict
v0041_openapi_accounts_add_cond_resp_association_condition_from_dict = V0041OpenapiAccountsAddCondRespAssociationCondition.from_dict(v0041_openapi_accounts_add_cond_resp_association_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


