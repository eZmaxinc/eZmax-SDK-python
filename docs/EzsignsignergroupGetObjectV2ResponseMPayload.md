# EzsignsignergroupGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsignsignergroup/{pkiEzsignsignergroupID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignsignergroup** | [**EzsignsignergroupResponseCompound**](EzsignsignergroupResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignergroup_get_object_v2_response_m_payload import EzsignsignergroupGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignergroupGetObjectV2ResponseMPayload from a JSON string
ezsignsignergroup_get_object_v2_response_m_payload_instance = EzsignsignergroupGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsignsignergroupGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
ezsignsignergroup_get_object_v2_response_m_payload_dict = ezsignsignergroup_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsignsignergroupGetObjectV2ResponseMPayload from a dict
ezsignsignergroup_get_object_v2_response_m_payload_form_dict = ezsignsignergroup_get_object_v2_response_m_payload.from_dict(ezsignsignergroup_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


