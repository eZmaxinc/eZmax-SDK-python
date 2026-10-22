# DocumenttypeCreateObjectV1Request

Request for POST /1/object/documenttype

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttype** | [**List[DocumenttypeRequestCompound]**](DocumenttypeRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.documenttype_create_object_v1_request import DocumenttypeCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of DocumenttypeCreateObjectV1Request from a JSON string
documenttype_create_object_v1_request_instance = DocumenttypeCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(DocumenttypeCreateObjectV1Request.to_json())

# convert the object into a dict
documenttype_create_object_v1_request_dict = documenttype_create_object_v1_request_instance.to_dict()
# create an instance of DocumenttypeCreateObjectV1Request from a dict
documenttype_create_object_v1_request_from_dict = DocumenttypeCreateObjectV1Request.from_dict(documenttype_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


