# EzsigndocumentGetObjectV3ResponseMPayload

Payload for GET /3/object/ezsigndocument/{pkiEzsigndocumentID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigndocument** | [**EzsigndocumentResponseCompoundV3**](EzsigndocumentResponseCompoundV3.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_get_object_v3_response_m_payload import EzsigndocumentGetObjectV3ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentGetObjectV3ResponseMPayload from a JSON string
ezsigndocument_get_object_v3_response_m_payload_instance = EzsigndocumentGetObjectV3ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentGetObjectV3ResponseMPayload.to_json())

# convert the object into a dict
ezsigndocument_get_object_v3_response_m_payload_dict = ezsigndocument_get_object_v3_response_m_payload_instance.to_dict()
# create an instance of EzsigndocumentGetObjectV3ResponseMPayload from a dict
ezsigndocument_get_object_v3_response_m_payload_from_dict = EzsigndocumentGetObjectV3ResponseMPayload.from_dict(ezsigndocument_get_object_v3_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


