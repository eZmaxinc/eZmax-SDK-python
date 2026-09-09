# DisclosureGetAttachmentsV1Response

Response for GET /1/object/disclosure/{pkiDisclosureID}/getAttachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DisclosureGetAttachmentsV1ResponseMPayload**](DisclosureGetAttachmentsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.disclosure_get_attachments_v1_response import DisclosureGetAttachmentsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DisclosureGetAttachmentsV1Response from a JSON string
disclosure_get_attachments_v1_response_instance = DisclosureGetAttachmentsV1Response.from_json(json)
# print the JSON string representation of the object
print(DisclosureGetAttachmentsV1Response.to_json())

# convert the object into a dict
disclosure_get_attachments_v1_response_dict = disclosure_get_attachments_v1_response_instance.to_dict()
# create an instance of DisclosureGetAttachmentsV1Response from a dict
disclosure_get_attachments_v1_response_from_dict = DisclosureGetAttachmentsV1Response.from_dict(disclosure_get_attachments_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


