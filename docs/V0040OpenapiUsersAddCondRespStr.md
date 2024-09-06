# V0040OpenapiUsersAddCondRespStr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**added_users** | **str** | added_users | 
**meta** | [**V0040OpenapiMeta**](V0040OpenapiMeta.md) |  | [optional] 
**errors** | [**List[V0040OpenapiError]**](V0040OpenapiError.md) |  | [optional] 
**warnings** | [**List[V0040OpenapiWarning]**](V0040OpenapiWarning.md) |  | [optional] 

## Example

```python
from slurm_rest.models.v0040_openapi_users_add_cond_resp_str import V0040OpenapiUsersAddCondRespStr

# TODO update the JSON string below
json = "{}"
# create an instance of V0040OpenapiUsersAddCondRespStr from a JSON string
v0040_openapi_users_add_cond_resp_str_instance = V0040OpenapiUsersAddCondRespStr.from_json(json)
# print the JSON string representation of the object
print(V0040OpenapiUsersAddCondRespStr.to_json())

# convert the object into a dict
v0040_openapi_users_add_cond_resp_str_dict = v0040_openapi_users_add_cond_resp_str_instance.to_dict()
# create an instance of V0040OpenapiUsersAddCondRespStr from a dict
v0040_openapi_users_add_cond_resp_str_from_dict = V0040OpenapiUsersAddCondRespStr.from_dict(v0040_openapi_users_add_cond_resp_str_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


