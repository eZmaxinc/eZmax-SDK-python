# UsergroupmembershipCreateObjectV1Request

Request for POST /1/object/usergroupmembership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_usergroupmembership** | [**List[UsergroupmembershipRequestCompound]**](UsergroupmembershipRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.usergroupmembership_create_object_v1_request import UsergroupmembershipCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupmembershipCreateObjectV1Request from a JSON string
usergroupmembership_create_object_v1_request_instance = UsergroupmembershipCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print UsergroupmembershipCreateObjectV1Request.to_json()

# convert the object into a dict
usergroupmembership_create_object_v1_request_dict = usergroupmembership_create_object_v1_request_instance.to_dict()
# create an instance of UsergroupmembershipCreateObjectV1Request from a dict
usergroupmembership_create_object_v1_request_form_dict = usergroupmembership_create_object_v1_request.from_dict(usergroupmembership_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


