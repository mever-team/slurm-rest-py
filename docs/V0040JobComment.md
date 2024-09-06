# V0040JobComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrator** | **str** |  | [optional] 
**job** | **str** |  | [optional] 
**system** | **str** |  | [optional] 

## Example

```python
from slurm_rest.models.v0040_job_comment import V0040JobComment

# TODO update the JSON string below
json = "{}"
# create an instance of V0040JobComment from a JSON string
v0040_job_comment_instance = V0040JobComment.from_json(json)
# print the JSON string representation of the object
print(V0040JobComment.to_json())

# convert the object into a dict
v0040_job_comment_dict = v0040_job_comment_instance.to_dict()
# create an instance of V0040JobComment from a dict
v0040_job_comment_from_dict = V0040JobComment.from_dict(v0040_job_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


