# SignatureGetObjectV2ResponseMPayload

Payload for GET /2/object/signature/{pkiSignatureID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_signature** | [**SignatureResponseCompound**](SignatureResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.signature_get_object_v2_response_m_payload import SignatureGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureGetObjectV2ResponseMPayload from a JSON string
signature_get_object_v2_response_m_payload_instance = SignatureGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(SignatureGetObjectV2ResponseMPayload.to_json())

# convert the object into a dict
signature_get_object_v2_response_m_payload_dict = signature_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of SignatureGetObjectV2ResponseMPayload from a dict
signature_get_object_v2_response_m_payload_from_dict = SignatureGetObjectV2ResponseMPayload.from_dict(signature_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


