# FolderGetCommunicationsendersV1ResponseMPayload

Response for GET /1/object/folder/{pkiFolderID}/getCommunicationsenders

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationsenders** | [**List[CustomCommunicationsenderResponse]**](CustomCommunicationsenderResponse.md) |  | 

## Example

```python
from eZmaxApi.models.folder_get_communicationsenders_v1_response_m_payload import FolderGetCommunicationsendersV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of FolderGetCommunicationsendersV1ResponseMPayload from a JSON string
folder_get_communicationsenders_v1_response_m_payload_instance = FolderGetCommunicationsendersV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(FolderGetCommunicationsendersV1ResponseMPayload.to_json())

# convert the object into a dict
folder_get_communicationsenders_v1_response_m_payload_dict = folder_get_communicationsenders_v1_response_m_payload_instance.to_dict()
# create an instance of FolderGetCommunicationsendersV1ResponseMPayload from a dict
folder_get_communicationsenders_v1_response_m_payload_from_dict = FolderGetCommunicationsendersV1ResponseMPayload.from_dict(folder_get_communicationsenders_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


