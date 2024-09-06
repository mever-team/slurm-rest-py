# V0041OpenapiSharesRespSharesSharesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | assocation id | [optional] 
**cluster** | **str** | cluster name | [optional] 
**name** | **str** | share name | [optional] 
**parent** | **str** | parent name | [optional] 
**partition** | **str** | partition name | [optional] 
**shares_normalized** | [**V0041OpenapiSharesRespSharesSharesInnerSharesNormalized**](V0041OpenapiSharesRespSharesSharesInnerSharesNormalized.md) |  | [optional] 
**shares** | [**V0041OpenapiSharesRespSharesSharesInnerShares**](V0041OpenapiSharesRespSharesSharesInnerShares.md) |  | [optional] 
**tres** | [**V0041OpenapiSharesRespSharesSharesInnerTres**](V0041OpenapiSharesRespSharesSharesInnerTres.md) |  | [optional] 
**effective_usage** | **float** | effective, normalized usage | [optional] 
**usage_normalized** | [**V0041OpenapiSharesRespSharesSharesInnerUsageNormalized**](V0041OpenapiSharesRespSharesSharesInnerUsageNormalized.md) |  | [optional] 
**usage** | **int** | measure of tresbillableunits usage | [optional] 
**fairshare** | [**V0040AssocSharesObjWrapFairshare**](V0040AssocSharesObjWrapFairshare.md) |  | [optional] 
**type** | **List[str]** | user or account association | [optional] 

## Example

```python
from slurm_rest.models.v0041_openapi_shares_resp_shares_shares_inner import V0041OpenapiSharesRespSharesSharesInner

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSharesRespSharesSharesInner from a JSON string
v0041_openapi_shares_resp_shares_shares_inner_instance = V0041OpenapiSharesRespSharesSharesInner.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSharesRespSharesSharesInner.to_json())

# convert the object into a dict
v0041_openapi_shares_resp_shares_shares_inner_dict = v0041_openapi_shares_resp_shares_shares_inner_instance.to_dict()
# create an instance of V0041OpenapiSharesRespSharesSharesInner from a dict
v0041_openapi_shares_resp_shares_shares_inner_from_dict = V0041OpenapiSharesRespSharesSharesInner.from_dict(v0041_openapi_shares_resp_shares_shares_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


