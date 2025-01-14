# UsergroupmembershipCreateObjectV1ResponseMPayload

Payload for POST /1/object/usergroupmembership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_usergroupmembership_id** | **List[int]** | An array of unique IDs representing the object that were requested to be created.  They are returned in the same order as the array containing the objects to be created that was sent in the request. | 

## Example

```python
from eZmaxApi.models.usergroupmembership_create_object_v1_response_m_payload import UsergroupmembershipCreateObjectV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupmembershipCreateObjectV1ResponseMPayload from a JSON string
usergroupmembership_create_object_v1_response_m_payload_instance = UsergroupmembershipCreateObjectV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(UsergroupmembershipCreateObjectV1ResponseMPayload.to_json())

# convert the object into a dict
usergroupmembership_create_object_v1_response_m_payload_dict = usergroupmembership_create_object_v1_response_m_payload_instance.to_dict()
# create an instance of UsergroupmembershipCreateObjectV1ResponseMPayload from a dict
usergroupmembership_create_object_v1_response_m_payload_from_dict = UsergroupmembershipCreateObjectV1ResponseMPayload.from_dict(usergroupmembership_create_object_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


