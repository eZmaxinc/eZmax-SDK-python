# DocumenttypeEditObjectV1Request

Request for PUT /1/object/documenttype/{pkiDocumenttypeID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_documenttype** | [**DocumenttypeRequestCompound**](DocumenttypeRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.documenttype_edit_object_v1_request import DocumenttypeEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of DocumenttypeEditObjectV1Request from a JSON string
documenttype_edit_object_v1_request_instance = DocumenttypeEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(DocumenttypeEditObjectV1Request.to_json())

# convert the object into a dict
documenttype_edit_object_v1_request_dict = documenttype_edit_object_v1_request_instance.to_dict()
# create an instance of DocumenttypeEditObjectV1Request from a dict
documenttype_edit_object_v1_request_from_dict = DocumenttypeEditObjectV1Request.from_dict(documenttype_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


