# EzsignsignatureGetObjectV2Response

Response for GET /2/object/ezsignsignature/{pkiEzsignsignatureID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignsignatureGetObjectV2ResponseMPayload**](EzsignsignatureGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignature_get_object_v2_response import EzsignsignatureGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureGetObjectV2Response from a JSON string
ezsignsignature_get_object_v2_response_instance = EzsignsignatureGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsignsignatureGetObjectV2Response.to_json())

# convert the object into a dict
ezsignsignature_get_object_v2_response_dict = ezsignsignature_get_object_v2_response_instance.to_dict()
# create an instance of EzsignsignatureGetObjectV2Response from a dict
ezsignsignature_get_object_v2_response_form_dict = ezsignsignature_get_object_v2_response.from_dict(ezsignsignature_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


