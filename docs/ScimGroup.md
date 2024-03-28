# ScimGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**display_name** | **str** | The Name of the Usergroup in the language of the requester | 
**members** | [**List[ScimGroupMember]**](ScimGroupMember.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.scim_group import ScimGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ScimGroup from a JSON string
scim_group_instance = ScimGroup.from_json(json)
# print the JSON string representation of the object
print(ScimGroup.to_json())

# convert the object into a dict
scim_group_dict = scim_group_instance.to_dict()
# create an instance of ScimGroup from a dict
scim_group_form_dict = scim_group.from_dict(scim_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


