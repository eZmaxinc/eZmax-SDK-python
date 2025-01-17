# EzsignfolderGetAttachmentsV1Response

Response for GET /1/object/ezsignfolder/{pkiEzsignfolderID}/getAttachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsignfolderGetAttachmentsV1ResponseMPayload**](EzsignfolderGetAttachmentsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_get_attachments_v1_response import EzsignfolderGetAttachmentsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderGetAttachmentsV1Response from a JSON string
ezsignfolder_get_attachments_v1_response_instance = EzsignfolderGetAttachmentsV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderGetAttachmentsV1Response.to_json())

# convert the object into a dict
ezsignfolder_get_attachments_v1_response_dict = ezsignfolder_get_attachments_v1_response_instance.to_dict()
# create an instance of EzsignfolderGetAttachmentsV1Response from a dict
ezsignfolder_get_attachments_v1_response_from_dict = EzsignfolderGetAttachmentsV1Response.from_dict(ezsignfolder_get_attachments_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


