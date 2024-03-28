# UsergroupexternalCreateObjectV1Request

Request for POST /1/object/usergroupexternal

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_usergroupexternal** | [**List[UsergroupexternalRequestCompound]**](UsergroupexternalRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.usergroupexternal_create_object_v1_request import UsergroupexternalCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupexternalCreateObjectV1Request from a JSON string
usergroupexternal_create_object_v1_request_instance = UsergroupexternalCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(UsergroupexternalCreateObjectV1Request.to_json())

# convert the object into a dict
usergroupexternal_create_object_v1_request_dict = usergroupexternal_create_object_v1_request_instance.to_dict()
# create an instance of UsergroupexternalCreateObjectV1Request from a dict
usergroupexternal_create_object_v1_request_form_dict = usergroupexternal_create_object_v1_request.from_dict(usergroupexternal_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


