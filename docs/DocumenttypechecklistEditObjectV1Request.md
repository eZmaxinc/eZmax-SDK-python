# DocumenttypechecklistEditObjectV1Request

Request for PUT /1/object/documenttypechecklist/{pkiDocumenttypechecklistID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_documenttypechecklist** | [**DocumenttypechecklistRequestCompound**](DocumenttypechecklistRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.documenttypechecklist_edit_object_v1_request import DocumenttypechecklistEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of DocumenttypechecklistEditObjectV1Request from a JSON string
documenttypechecklist_edit_object_v1_request_instance = DocumenttypechecklistEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(DocumenttypechecklistEditObjectV1Request.to_json())

# convert the object into a dict
documenttypechecklist_edit_object_v1_request_dict = documenttypechecklist_edit_object_v1_request_instance.to_dict()
# create an instance of DocumenttypechecklistEditObjectV1Request from a dict
documenttypechecklist_edit_object_v1_request_from_dict = DocumenttypechecklistEditObjectV1Request.from_dict(documenttypechecklist_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


