# V0041OpenapiUsersAddCondRespUser

Admin level of user, DefaultAccount, DefaultWCKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adminlevel** | **List[str]** | Admin level of user.  Valid levels are None, Operator, and Admin. | [optional] 
**defaultaccount** | **str** | Identify the default bank account name to be used for a job if none is specified at submission time. | [optional] 
**defaultwckey** | **str** | Identify the default Workload Characterization Key. | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_users_add_cond_resp_user import V0041OpenapiUsersAddCondRespUser

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiUsersAddCondRespUser from a JSON string
v0041_openapi_users_add_cond_resp_user_instance = V0041OpenapiUsersAddCondRespUser.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiUsersAddCondRespUser.to_json())

# convert the object into a dict
v0041_openapi_users_add_cond_resp_user_dict = v0041_openapi_users_add_cond_resp_user_instance.to_dict()
# create an instance of V0041OpenapiUsersAddCondRespUser from a dict
v0041_openapi_users_add_cond_resp_user_from_dict = V0041OpenapiUsersAddCondRespUser.from_dict(v0041_openapi_users_add_cond_resp_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


