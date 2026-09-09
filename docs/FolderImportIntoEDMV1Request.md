# FolderImportIntoEDMV1Request

Request for POST /1/object/folder/{pkiFolderID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.folder_import_into_edmv1_request import FolderImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of FolderImportIntoEDMV1Request from a JSON string
folder_import_into_edmv1_request_instance = FolderImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(FolderImportIntoEDMV1Request.to_json())

# convert the object into a dict
folder_import_into_edmv1_request_dict = folder_import_into_edmv1_request_instance.to_dict()
# create an instance of FolderImportIntoEDMV1Request from a dict
folder_import_into_edmv1_request_from_dict = FolderImportIntoEDMV1Request.from_dict(folder_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


