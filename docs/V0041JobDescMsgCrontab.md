# V0041JobDescMsgCrontab

crontab entry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flags** | **List[str]** |  | [optional] 
**minute** | **str** |  | [optional] 
**hour** | **str** |  | [optional] 
**day_of_month** | **str** |  | [optional] 
**month** | **str** |  | [optional] 
**day_of_week** | **str** |  | [optional] 
**specification** | **str** |  | [optional] 
**command** | **str** |  | [optional] 
**line** | [**V0040CronEntryLine**](V0040CronEntryLine.md) |  | [optional] 

## Example

```python
from slurm_rest.models.v0041_job_desc_msg_crontab import V0041JobDescMsgCrontab

# TODO update the JSON string below
json = "{}"
# create an instance of V0041JobDescMsgCrontab from a JSON string
v0041_job_desc_msg_crontab_instance = V0041JobDescMsgCrontab.from_json(json)
# print the JSON string representation of the object
print(V0041JobDescMsgCrontab.to_json())

# convert the object into a dict
v0041_job_desc_msg_crontab_dict = v0041_job_desc_msg_crontab_instance.to_dict()
# create an instance of V0041JobDescMsgCrontab from a dict
v0041_job_desc_msg_crontab_from_dict = V0041JobDescMsgCrontab.from_dict(v0041_job_desc_msg_crontab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


