# SignatureGetObjectV3Response

Response for GET /3/object/signature/{pkiSignatureID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**SignatureGetObjectV3ResponseMPayload**](SignatureGetObjectV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.signature_get_object_v3_response import SignatureGetObjectV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureGetObjectV3Response from a JSON string
signature_get_object_v3_response_instance = SignatureGetObjectV3Response.from_json(json)
# print the JSON string representation of the object
print(SignatureGetObjectV3Response.to_json())

# convert the object into a dict
signature_get_object_v3_response_dict = signature_get_object_v3_response_instance.to_dict()
# create an instance of SignatureGetObjectV3Response from a dict
signature_get_object_v3_response_from_dict = SignatureGetObjectV3Response.from_dict(signature_get_object_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


