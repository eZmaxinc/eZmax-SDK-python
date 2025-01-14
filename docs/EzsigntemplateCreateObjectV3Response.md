# EzsigntemplateCreateObjectV3Response

Response for POST /3/object/ezsigntemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplateCreateObjectV3ResponseMPayload**](EzsigntemplateCreateObjectV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_create_object_v3_response import EzsigntemplateCreateObjectV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateCreateObjectV3Response from a JSON string
ezsigntemplate_create_object_v3_response_instance = EzsigntemplateCreateObjectV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateCreateObjectV3Response.to_json())

# convert the object into a dict
ezsigntemplate_create_object_v3_response_dict = ezsigntemplate_create_object_v3_response_instance.to_dict()
# create an instance of EzsigntemplateCreateObjectV3Response from a dict
ezsigntemplate_create_object_v3_response_from_dict = EzsigntemplateCreateObjectV3Response.from_dict(ezsigntemplate_create_object_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


