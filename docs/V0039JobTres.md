# V0039JobTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated** | [**List[V0039Tres]**](V0039Tres.md) |  | [optional] 
**requested** | [**List[V0039Tres]**](V0039Tres.md) |  | [optional] 

## Example

```python
from slurm_rest.models.v0039_job_tres import V0039JobTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0039JobTres from a JSON string
v0039_job_tres_instance = V0039JobTres.from_json(json)
# print the JSON string representation of the object
print(V0039JobTres.to_json())

# convert the object into a dict
v0039_job_tres_dict = v0039_job_tres_instance.to_dict()
# create an instance of V0039JobTres from a dict
v0039_job_tres_from_dict = V0039JobTres.from_dict(v0039_job_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

