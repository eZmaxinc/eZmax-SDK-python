# SignatureEditObjectV1Response

Response for PUT /1/object/signature/{pkiSignatureID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.signature_edit_object_v1_response import SignatureEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of SignatureEditObjectV1Response from a JSON string
signature_edit_object_v1_response_instance = SignatureEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(SignatureEditObjectV1Response.to_json())

# convert the object into a dict
signature_edit_object_v1_response_dict = signature_edit_object_v1_response_instance.to_dict()
# create an instance of SignatureEditObjectV1Response from a dict
signature_edit_object_v1_response_form_dict = signature_edit_object_v1_response.from_dict(signature_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


