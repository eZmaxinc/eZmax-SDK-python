# UsergroupmembershipEditObjectV1Request

Request for PUT /1/object/usergroupmembership/{pkiUsergroupmembershipID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_usergroupmembership** | [**UsergroupmembershipRequestCompound**](UsergroupmembershipRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.usergroupmembership_edit_object_v1_request import UsergroupmembershipEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupmembershipEditObjectV1Request from a JSON string
usergroupmembership_edit_object_v1_request_instance = UsergroupmembershipEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(UsergroupmembershipEditObjectV1Request.to_json())

# convert the object into a dict
usergroupmembership_edit_object_v1_request_dict = usergroupmembership_edit_object_v1_request_instance.to_dict()
# create an instance of UsergroupmembershipEditObjectV1Request from a dict
usergroupmembership_edit_object_v1_request_form_dict = usergroupmembership_edit_object_v1_request.from_dict(usergroupmembership_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


