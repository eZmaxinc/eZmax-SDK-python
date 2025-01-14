# UsergroupexternalEditObjectV1Request

Request for PUT /1/object/usergroupexternal/{pkiUsergroupexternalID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_usergroupexternal** | [**UsergroupexternalRequestCompound**](UsergroupexternalRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.usergroupexternal_edit_object_v1_request import UsergroupexternalEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupexternalEditObjectV1Request from a JSON string
usergroupexternal_edit_object_v1_request_instance = UsergroupexternalEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(UsergroupexternalEditObjectV1Request.to_json())

# convert the object into a dict
usergroupexternal_edit_object_v1_request_dict = usergroupexternal_edit_object_v1_request_instance.to_dict()
# create an instance of UsergroupexternalEditObjectV1Request from a dict
usergroupexternal_edit_object_v1_request_from_dict = UsergroupexternalEditObjectV1Request.from_dict(usergroupexternal_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


