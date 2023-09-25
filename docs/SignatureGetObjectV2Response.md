# SignatureGetObjectV2Response

Response for GET /2/object/signature/{pkiSignatureID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**SignatureGetObjectV2ResponseMPayload**](SignatureGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.signature_get_object_v2_response import SignatureGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureGetObjectV2Response from a JSON string
signature_get_object_v2_response_instance = SignatureGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print SignatureGetObjectV2Response.to_json()

# convert the object into a dict
signature_get_object_v2_response_dict = signature_get_object_v2_response_instance.to_dict()
# create an instance of SignatureGetObjectV2Response from a dict
signature_get_object_v2_response_form_dict = signature_get_object_v2_response.from_dict(signature_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


