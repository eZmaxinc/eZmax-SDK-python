# AdjustmentImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/adjustment/{pkiAdjustmentID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.adjustment_import_into_edmv1_response_m_payload import AdjustmentImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustmentImportIntoEDMV1ResponseMPayload from a JSON string
adjustment_import_into_edmv1_response_m_payload_instance = AdjustmentImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(AdjustmentImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
adjustment_import_into_edmv1_response_m_payload_dict = adjustment_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of AdjustmentImportIntoEDMV1ResponseMPayload from a dict
adjustment_import_into_edmv1_response_m_payload_from_dict = AdjustmentImportIntoEDMV1ResponseMPayload.from_dict(adjustment_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


