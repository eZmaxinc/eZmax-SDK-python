# FolderImportIntoEDMV1Response

Response for POST /1/object/folder/{pkiFolderID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**FolderImportIntoEDMV1ResponseMPayload**](FolderImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.folder_import_into_edmv1_response import FolderImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of FolderImportIntoEDMV1Response from a JSON string
folder_import_into_edmv1_response_instance = FolderImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(FolderImportIntoEDMV1Response.to_json())

# convert the object into a dict
folder_import_into_edmv1_response_dict = folder_import_into_edmv1_response_instance.to_dict()
# create an instance of FolderImportIntoEDMV1Response from a dict
folder_import_into_edmv1_response_from_dict = FolderImportIntoEDMV1Response.from_dict(folder_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


