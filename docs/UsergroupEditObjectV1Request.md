# UsergroupEditObjectV1Request

Request for PUT /1/object/usergroup/{pkiUsergroupID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_usergroup** | [**UsergroupRequestCompound**](UsergroupRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.usergroup_edit_object_v1_request import UsergroupEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupEditObjectV1Request from a JSON string
usergroup_edit_object_v1_request_instance = UsergroupEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print UsergroupEditObjectV1Request.to_json()

# convert the object into a dict
usergroup_edit_object_v1_request_dict = usergroup_edit_object_v1_request_instance.to_dict()
# create an instance of UsergroupEditObjectV1Request from a dict
usergroup_edit_object_v1_request_form_dict = usergroup_edit_object_v1_request.from_dict(usergroup_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


