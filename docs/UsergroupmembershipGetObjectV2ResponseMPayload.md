# UsergroupmembershipGetObjectV2ResponseMPayload

Payload for GET /2/object/usergroupmembership/{pkiUsergroupmembershipID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_usergroupmembership** | [**UsergroupmembershipResponseCompound**](UsergroupmembershipResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.usergroupmembership_get_object_v2_response_m_payload import UsergroupmembershipGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UsergroupmembershipGetObjectV2ResponseMPayload from a JSON string
usergroupmembership_get_object_v2_response_m_payload_instance = UsergroupmembershipGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print UsergroupmembershipGetObjectV2ResponseMPayload.to_json()

# convert the object into a dict
usergroupmembership_get_object_v2_response_m_payload_dict = usergroupmembership_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of UsergroupmembershipGetObjectV2ResponseMPayload from a dict
usergroupmembership_get_object_v2_response_m_payload_form_dict = usergroupmembership_get_object_v2_response_m_payload.from_dict(usergroupmembership_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


