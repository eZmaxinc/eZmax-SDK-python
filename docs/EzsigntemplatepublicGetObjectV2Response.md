# EzsigntemplatepublicGetObjectV2Response

Response for GET /2/object/ezsigntemplatepublic/{pkiEzsigntemplatepublicID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatepublicGetObjectV2ResponseMPayload**](EzsigntemplatepublicGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepublic_get_object_v2_response import EzsigntemplatepublicGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepublicGetObjectV2Response from a JSON string
ezsigntemplatepublic_get_object_v2_response_instance = EzsigntemplatepublicGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepublicGetObjectV2Response.to_json())

# convert the object into a dict
ezsigntemplatepublic_get_object_v2_response_dict = ezsigntemplatepublic_get_object_v2_response_instance.to_dict()
# create an instance of EzsigntemplatepublicGetObjectV2Response from a dict
ezsigntemplatepublic_get_object_v2_response_from_dict = EzsigntemplatepublicGetObjectV2Response.from_dict(ezsigntemplatepublic_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


