# NotaryGetAttachmentsV1Response

Response for GET /1/object/notary/{pkiNotaryID}/getAttachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**NotaryGetAttachmentsV1ResponseMPayload**](NotaryGetAttachmentsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.notary_get_attachments_v1_response import NotaryGetAttachmentsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of NotaryGetAttachmentsV1Response from a JSON string
notary_get_attachments_v1_response_instance = NotaryGetAttachmentsV1Response.from_json(json)
# print the JSON string representation of the object
print(NotaryGetAttachmentsV1Response.to_json())

# convert the object into a dict
notary_get_attachments_v1_response_dict = notary_get_attachments_v1_response_instance.to_dict()
# create an instance of NotaryGetAttachmentsV1Response from a dict
notary_get_attachments_v1_response_from_dict = NotaryGetAttachmentsV1Response.from_dict(notary_get_attachments_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


