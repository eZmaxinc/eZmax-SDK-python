# SignatureCreateObjectV1Response

Response for POST /1/object/signature

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**SignatureCreateObjectV1ResponseMPayload**](SignatureCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.signature_create_object_v1_response import SignatureCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureCreateObjectV1Response from a JSON string
signature_create_object_v1_response_instance = SignatureCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print SignatureCreateObjectV1Response.to_json()

# convert the object into a dict
signature_create_object_v1_response_dict = signature_create_object_v1_response_instance.to_dict()
# create an instance of SignatureCreateObjectV1Response from a dict
signature_create_object_v1_response_form_dict = signature_create_object_v1_response.from_dict(signature_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


