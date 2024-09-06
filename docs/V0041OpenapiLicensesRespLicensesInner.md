# V0041OpenapiLicensesRespLicensesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_name** | **str** |  | [optional] 
**total** | **int** |  | [optional] 
**used** | **int** |  | [optional] 
**free** | **int** |  | [optional] 
**remote** | **bool** |  | [optional] 
**reserved** | **int** |  | [optional] 
**last_consumed** | **int** |  | [optional] 
**last_deficit** | **int** |  | [optional] 
**last_update** | **int** |  | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_licenses_resp_licenses_inner import V0041OpenapiLicensesRespLicensesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiLicensesRespLicensesInner from a JSON string
v0041_openapi_licenses_resp_licenses_inner_instance = V0041OpenapiLicensesRespLicensesInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiLicensesRespLicensesInner.to_json())

# convert the object into a dict
v0041_openapi_licenses_resp_licenses_inner_dict = v0041_openapi_licenses_resp_licenses_inner_instance.to_dict()
# create an instance of V0041OpenapiLicensesRespLicensesInner from a dict
v0041_openapi_licenses_resp_licenses_inner_from_dict = V0041OpenapiLicensesRespLicensesInner.from_dict(v0041_openapi_licenses_resp_licenses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


