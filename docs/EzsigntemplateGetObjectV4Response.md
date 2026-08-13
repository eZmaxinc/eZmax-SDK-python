# EzsigntemplateGetObjectV4Response

Response for GET /4/object/ezsigntemplate/{pkiEzsigntemplateID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplateGetObjectV4ResponseMPayload**](EzsigntemplateGetObjectV4ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_get_object_v4_response import EzsigntemplateGetObjectV4Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateGetObjectV4Response from a JSON string
ezsigntemplate_get_object_v4_response_instance = EzsigntemplateGetObjectV4Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateGetObjectV4Response.to_json())

# convert the object into a dict
ezsigntemplate_get_object_v4_response_dict = ezsigntemplate_get_object_v4_response_instance.to_dict()
# create an instance of EzsigntemplateGetObjectV4Response from a dict
ezsigntemplate_get_object_v4_response_from_dict = EzsigntemplateGetObjectV4Response.from_dict(ezsigntemplate_get_object_v4_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


