# V0039AssocMaxJobs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per** | [**V0039AssocMaxJobsPer**](V0039AssocMaxJobsPer.md) |  | [optional] 
**active** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**accruing** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 
**total** | [**V0039Uint32NoVal**](V0039Uint32NoVal.md) |  | [optional] 

## Example

```python
from slurm_rest.models.v0039_assoc_max_jobs import V0039AssocMaxJobs

# TODO update the JSON string below
json = "{}"
# create an instance of V0039AssocMaxJobs from a JSON string
v0039_assoc_max_jobs_instance = V0039AssocMaxJobs.from_json(json)
# print the JSON string representation of the object
print(V0039AssocMaxJobs.to_json())

# convert the object into a dict
v0039_assoc_max_jobs_dict = v0039_assoc_max_jobs_instance.to_dict()
# create an instance of V0039AssocMaxJobs from a dict
v0039_assoc_max_jobs_from_dict = V0039AssocMaxJobs.from_dict(v0039_assoc_max_jobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


