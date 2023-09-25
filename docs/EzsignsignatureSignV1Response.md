# EzsignsignatureSignV1Response

Response for POST /1/object/ezsignsignature/{pkiEzsignsignatureID}/sign

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignsignature_sign_v1_response import EzsignsignatureSignV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureSignV1Response from a JSON string
ezsignsignature_sign_v1_response_instance = EzsignsignatureSignV1Response.from_json(json)
# print the JSON string representation of the object
print EzsignsignatureSignV1Response.to_json()

# convert the object into a dict
ezsignsignature_sign_v1_response_dict = ezsignsignature_sign_v1_response_instance.to_dict()
# create an instance of EzsignsignatureSignV1Response from a dict
ezsignsignature_sign_v1_response_form_dict = ezsignsignature_sign_v1_response.from_dict(ezsignsignature_sign_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


