# EzsignsignergroupmembershipGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsignsignergroupmembership/{pkiEzsignsignergroupmembershipID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignsignergroupmembership** | [**EzsignsignergroupmembershipResponseCompound**](EzsignsignergroupmembershipResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignergroupmembership_get_object_v2_response_m_payload import EzsignsignergroupmembershipGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignergroupmembershipGetObjectV2ResponseMPayload from a JSON string
ezsignsignergroupmembership_get_object_v2_response_m_payload_instance = EzsignsignergroupmembershipGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsignsignergroupmembershipGetObjectV2ResponseMPayload.to_json()

# convert the object into a dict
ezsignsignergroupmembership_get_object_v2_response_m_payload_dict = ezsignsignergroupmembership_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsignsignergroupmembershipGetObjectV2ResponseMPayload from a dict
ezsignsignergroupmembership_get_object_v2_response_m_payload_form_dict = ezsignsignergroupmembership_get_object_v2_response_m_payload.from_dict(ezsignsignergroupmembership_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


