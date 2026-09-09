# AdjustmentGetAttachmentsV1Response

Response for GET /1/object/adjustment/{pkiAdjustmentID}/getAttachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**AdjustmentGetAttachmentsV1ResponseMPayload**](AdjustmentGetAttachmentsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.adjustment_get_attachments_v1_response import AdjustmentGetAttachmentsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustmentGetAttachmentsV1Response from a JSON string
adjustment_get_attachments_v1_response_instance = AdjustmentGetAttachmentsV1Response.from_json(json)
# print the JSON string representation of the object
print(AdjustmentGetAttachmentsV1Response.to_json())

# convert the object into a dict
adjustment_get_attachments_v1_response_dict = adjustment_get_attachments_v1_response_instance.to_dict()
# create an instance of AdjustmentGetAttachmentsV1Response from a dict
adjustment_get_attachments_v1_response_from_dict = AdjustmentGetAttachmentsV1Response.from_dict(adjustment_get_attachments_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


