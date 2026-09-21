# FolderGetCommunicationsendersV1Response

Response for GET /1/object/folder/{pkiFolderID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**FolderGetCommunicationsendersV1ResponseMPayload**](FolderGetCommunicationsendersV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.folder_get_communicationsenders_v1_response import FolderGetCommunicationsendersV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of FolderGetCommunicationsendersV1Response from a JSON string
folder_get_communicationsenders_v1_response_instance = FolderGetCommunicationsendersV1Response.from_json(json)
# print the JSON string representation of the object
print(FolderGetCommunicationsendersV1Response.to_json())

# convert the object into a dict
folder_get_communicationsenders_v1_response_dict = folder_get_communicationsenders_v1_response_instance.to_dict()
# create an instance of FolderGetCommunicationsendersV1Response from a dict
folder_get_communicationsenders_v1_response_from_dict = FolderGetCommunicationsendersV1Response.from_dict(folder_get_communicationsenders_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


