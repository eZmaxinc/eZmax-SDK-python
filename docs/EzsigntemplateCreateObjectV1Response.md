# EzsigntemplateCreateObjectV1Response

Response for POST /1/object/ezsigntemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplateCreateObjectV1ResponseMPayload**](EzsigntemplateCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_create_object_v1_response import EzsigntemplateCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateCreateObjectV1Response from a JSON string
ezsigntemplate_create_object_v1_response_instance = EzsigntemplateCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateCreateObjectV1Response.to_json())

# convert the object into a dict
ezsigntemplate_create_object_v1_response_dict = ezsigntemplate_create_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplateCreateObjectV1Response from a dict
ezsigntemplate_create_object_v1_response_form_dict = ezsigntemplate_create_object_v1_response.from_dict(ezsigntemplate_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


