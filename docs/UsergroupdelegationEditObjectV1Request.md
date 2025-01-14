# UsergroupdelegationEditObjectV1Request

Request for PUT /1/object/usergroupdelegation/{pkiUsergroupdelegationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_usergroupdelegation** | [**UsergroupdelegationRequestCompound**](UsergroupdelegationRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.usergroupdelegation_edit_object_v1_request import UsergroupdelegationEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupdelegationEditObjectV1Request from a JSON string
usergroupdelegation_edit_object_v1_request_instance = UsergroupdelegationEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(UsergroupdelegationEditObjectV1Request.to_json())

# convert the object into a dict
usergroupdelegation_edit_object_v1_request_dict = usergroupdelegation_edit_object_v1_request_instance.to_dict()
# create an instance of UsergroupdelegationEditObjectV1Request from a dict
usergroupdelegation_edit_object_v1_request_from_dict = UsergroupdelegationEditObjectV1Request.from_dict(usergroupdelegation_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


