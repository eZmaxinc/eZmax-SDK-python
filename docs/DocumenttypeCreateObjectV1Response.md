# DocumenttypeCreateObjectV1Response

Response for POST /1/object/documenttype

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DocumenttypeCreateObjectV1ResponseMPayload**](DocumenttypeCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.documenttype_create_object_v1_response import DocumenttypeCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DocumenttypeCreateObjectV1Response from a JSON string
documenttype_create_object_v1_response_instance = DocumenttypeCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(DocumenttypeCreateObjectV1Response.to_json())

# convert the object into a dict
documenttype_create_object_v1_response_dict = documenttype_create_object_v1_response_instance.to_dict()
# create an instance of DocumenttypeCreateObjectV1Response from a dict
documenttype_create_object_v1_response_from_dict = DocumenttypeCreateObjectV1Response.from_dict(documenttype_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


