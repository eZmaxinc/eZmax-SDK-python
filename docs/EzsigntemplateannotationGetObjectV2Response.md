# EzsigntemplateannotationGetObjectV2Response

Response for GET /2/object/ezsigntemplateannotation/{pkiEzsigntemplateannotationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplateannotationGetObjectV2ResponseMPayload**](EzsigntemplateannotationGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplateannotation_get_object_v2_response import EzsigntemplateannotationGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateannotationGetObjectV2Response from a JSON string
ezsigntemplateannotation_get_object_v2_response_instance = EzsigntemplateannotationGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateannotationGetObjectV2Response.to_json())

# convert the object into a dict
ezsigntemplateannotation_get_object_v2_response_dict = ezsigntemplateannotation_get_object_v2_response_instance.to_dict()
# create an instance of EzsigntemplateannotationGetObjectV2Response from a dict
ezsigntemplateannotation_get_object_v2_response_from_dict = EzsigntemplateannotationGetObjectV2Response.from_dict(ezsigntemplateannotation_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


