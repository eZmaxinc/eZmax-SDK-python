# UsergroupmembershipCreateObjectV1Response

Response for POST /1/object/usergroupmembership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**UsergroupmembershipCreateObjectV1ResponseMPayload**](UsergroupmembershipCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.usergroupmembership_create_object_v1_response import UsergroupmembershipCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupmembershipCreateObjectV1Response from a JSON string
usergroupmembership_create_object_v1_response_instance = UsergroupmembershipCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(UsergroupmembershipCreateObjectV1Response.to_json())

# convert the object into a dict
usergroupmembership_create_object_v1_response_dict = usergroupmembership_create_object_v1_response_instance.to_dict()
# create an instance of UsergroupmembershipCreateObjectV1Response from a dict
usergroupmembership_create_object_v1_response_from_dict = UsergroupmembershipCreateObjectV1Response.from_dict(usergroupmembership_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


