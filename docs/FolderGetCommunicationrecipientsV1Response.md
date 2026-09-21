# FolderGetCommunicationrecipientsV1Response

Response for GET /1/object/folder/{pkiFolderID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**FolderGetCommunicationrecipientsV1ResponseMPayload**](FolderGetCommunicationrecipientsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.folder_get_communicationrecipients_v1_response import FolderGetCommunicationrecipientsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of FolderGetCommunicationrecipientsV1Response from a JSON string
folder_get_communicationrecipients_v1_response_instance = FolderGetCommunicationrecipientsV1Response.from_json(json)
# print the JSON string representation of the object
print(FolderGetCommunicationrecipientsV1Response.to_json())

# convert the object into a dict
folder_get_communicationrecipients_v1_response_dict = folder_get_communicationrecipients_v1_response_instance.to_dict()
# create an instance of FolderGetCommunicationrecipientsV1Response from a dict
folder_get_communicationrecipients_v1_response_from_dict = FolderGetCommunicationrecipientsV1Response.from_dict(folder_get_communicationrecipients_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


