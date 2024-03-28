# UsergroupdelegationCreateObjectV1Request

Request for POST /1/object/usergroupdelegation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_usergroupdelegation** | [**List[UsergroupdelegationRequestCompound]**](UsergroupdelegationRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.usergroupdelegation_create_object_v1_request import UsergroupdelegationCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupdelegationCreateObjectV1Request from a JSON string
usergroupdelegation_create_object_v1_request_instance = UsergroupdelegationCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(UsergroupdelegationCreateObjectV1Request.to_json())

# convert the object into a dict
usergroupdelegation_create_object_v1_request_dict = usergroupdelegation_create_object_v1_request_instance.to_dict()
# create an instance of UsergroupdelegationCreateObjectV1Request from a dict
usergroupdelegation_create_object_v1_request_form_dict = usergroupdelegation_create_object_v1_request.from_dict(usergroupdelegation_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


