# ScimGroupMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**display** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**ref** | **str** |  | [optional] 

## Example

```python
from eZmaxApi.models.scim_group_member import ScimGroupMember

# TODO update the JSON string below
json = "{}"
# create an instance of ScimGroupMember from a JSON string
scim_group_member_instance = ScimGroupMember.from_json(json)
# print the JSON string representation of the object
print(ScimGroupMember.to_json())

# convert the object into a dict
scim_group_member_dict = scim_group_member_instance.to_dict()
# create an instance of ScimGroupMember from a dict
scim_group_member_from_dict = ScimGroupMember.from_dict(scim_group_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


