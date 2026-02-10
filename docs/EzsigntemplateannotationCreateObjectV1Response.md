# EzsigntemplateannotationCreateObjectV1Response

Response for POST /1/object/ezsigntemplateannotation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplateannotationCreateObjectV1ResponseMPayload**](EzsigntemplateannotationCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplateannotation_create_object_v1_response import EzsigntemplateannotationCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateannotationCreateObjectV1Response from a JSON string
ezsigntemplateannotation_create_object_v1_response_instance = EzsigntemplateannotationCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateannotationCreateObjectV1Response.to_json())

# convert the object into a dict
ezsigntemplateannotation_create_object_v1_response_dict = ezsigntemplateannotation_create_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplateannotationCreateObjectV1Response from a dict
ezsigntemplateannotation_create_object_v1_response_from_dict = EzsigntemplateannotationCreateObjectV1Response.from_dict(ezsigntemplateannotation_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


