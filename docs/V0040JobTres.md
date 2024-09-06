# V0040JobTres


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated** | [**List[V0040Tres]**](V0040Tres.md) |  | [optional] 
**requested** | [**List[V0040Tres]**](V0040Tres.md) |  | [optional] 

## Example

```python
from slurm_rest.models.v0040_job_tres import V0040JobTres

# TODO update the JSON string below
json = "{}"
# create an instance of V0040JobTres from a JSON string
v0040_job_tres_instance = V0040JobTres.from_json(json)
# print the JSON string representation of the object
print(V0040JobTres.to_json())

# convert the object into a dict
v0040_job_tres_dict = v0040_job_tres_instance.to_dict()
# create an instance of V0040JobTres from a dict
v0040_job_tres_from_dict = V0040JobTres.from_dict(v0040_job_tres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


