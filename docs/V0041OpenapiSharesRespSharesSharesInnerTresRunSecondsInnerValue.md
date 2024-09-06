# V0041OpenapiSharesRespSharesSharesInnerTresRunSecondsInnerValue

TRES value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set. False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite. \&quot;set\&quot; and \&quot;number\&quot; will be ignored. | [optional] 
**number** | **int** | If set is True the number will be set with value. Otherwise ignore number contents. | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner_value import V0041OpenapiSharesRespSharesSharesInnerTresRunSecondsInnerValue

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSharesRespSharesSharesInnerTresRunSecondsInnerValue from a JSON string
v0041_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner_value_instance = V0041OpenapiSharesRespSharesSharesInnerTresRunSecondsInnerValue.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSharesRespSharesSharesInnerTresRunSecondsInnerValue.to_json())

# convert the object into a dict
v0041_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner_value_dict = v0041_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner_value_instance.to_dict()
# create an instance of V0041OpenapiSharesRespSharesSharesInnerTresRunSecondsInnerValue from a dict
v0041_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner_value_from_dict = V0041OpenapiSharesRespSharesSharesInnerTresRunSecondsInnerValue.from_dict(v0041_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


