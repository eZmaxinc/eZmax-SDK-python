# EzsignbulksendGetObjectV3Response

Response for GET /3/object/ezsignbulksend/{pkiEzsignbulksendID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignbulksendGetObjectV3ResponseMPayload**](EzsignbulksendGetObjectV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksend_get_object_v3_response import EzsignbulksendGetObjectV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendGetObjectV3Response from a JSON string
ezsignbulksend_get_object_v3_response_instance = EzsignbulksendGetObjectV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendGetObjectV3Response.to_json())

# convert the object into a dict
ezsignbulksend_get_object_v3_response_dict = ezsignbulksend_get_object_v3_response_instance.to_dict()
# create an instance of EzsignbulksendGetObjectV3Response from a dict
ezsignbulksend_get_object_v3_response_from_dict = EzsignbulksendGetObjectV3Response.from_dict(ezsignbulksend_get_object_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


