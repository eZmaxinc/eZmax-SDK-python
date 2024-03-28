# EzsigndocumentGetObjectV2ResponseMPayload

Payload for GET /2/object/ezsigndocument/{pkiEzsigndocumentID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigndocument** | [**EzsigndocumentResponseCompound**](EzsigndocumentResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_get_object_v2_response_m_payload import EzsigndocumentGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentGetObjectV2ResponseMPayload from a JSON string
ezsigndocument_get_object_v2_response_m_payload_instance = EzsigndocumentGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
ezsigndocument_get_object_v2_response_m_payload_dict = ezsigndocument_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of EzsigndocumentGetObjectV2ResponseMPayload from a dict
ezsigndocument_get_object_v2_response_m_payload_form_dict = ezsigndocument_get_object_v2_response_m_payload.from_dict(ezsigndocument_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


