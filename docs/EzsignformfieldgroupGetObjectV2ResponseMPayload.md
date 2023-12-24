# EzsignformfieldgroupGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsignformfieldgroup/{pkiEzsignformfieldgroupID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsignformfieldgroup** | [**EzsignformfieldgroupResponseCompound**](EzsignformfieldgroupResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignformfieldgroup_get_object_v2_response_m_payload import EzsignformfieldgroupGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignformfieldgroupGetObjectV2ResponseMPayload from a JSON string
ezsignformfieldgroup_get_object_v2_response_m_payload_instance = EzsignformfieldgroupGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsignformfieldgroupGetObjectV2ResponseMPayload.to_json()

# convert the object into a dict
ezsignformfieldgroup_get_object_v2_response_m_payload_dict = ezsignformfieldgroup_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsignformfieldgroupGetObjectV2ResponseMPayload from a dict
ezsignformfieldgroup_get_object_v2_response_m_payload_form_dict = ezsignformfieldgroup_get_object_v2_response_m_payload.from_dict(ezsignformfieldgroup_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


