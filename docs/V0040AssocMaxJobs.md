# V0040AssocMaxJobs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per** | [**V0040AssocMaxJobsPer**](V0040AssocMaxJobsPer.md) |  | [optional] 
**active** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**accruing** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 
**total** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 

## Example

```python
from slurm_rest.models.v0040_assoc_max_jobs import V0040AssocMaxJobs

# TODO update the JSON string below
json = "{}"
# create an instance of V0040AssocMaxJobs from a JSON string
v0040_assoc_max_jobs_instance = V0040AssocMaxJobs.from_json(json)
# print the JSON string representation of the object
print(V0040AssocMaxJobs.to_json())

# convert the object into a dict
v0040_assoc_max_jobs_dict = v0040_assoc_max_jobs_instance.to_dict()
# create an instance of V0040AssocMaxJobs from a dict
v0040_assoc_max_jobs_from_dict = V0040AssocMaxJobs.from_dict(v0040_assoc_max_jobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


