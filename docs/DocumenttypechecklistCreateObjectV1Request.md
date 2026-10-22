# DocumenttypechecklistCreateObjectV1Request

Request for POST /1/object/documenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[DocumenttypechecklistRequestCompound]**](DocumenttypechecklistRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.documenttypechecklist_create_object_v1_request import DocumenttypechecklistCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of DocumenttypechecklistCreateObjectV1Request from a JSON string
documenttypechecklist_create_object_v1_request_instance = DocumenttypechecklistCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(DocumenttypechecklistCreateObjectV1Request.to_json())

# convert the object into a dict
documenttypechecklist_create_object_v1_request_dict = documenttypechecklist_create_object_v1_request_instance.to_dict()
# create an instance of DocumenttypechecklistCreateObjectV1Request from a dict
documenttypechecklist_create_object_v1_request_from_dict = DocumenttypechecklistCreateObjectV1Request.from_dict(documenttypechecklist_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


