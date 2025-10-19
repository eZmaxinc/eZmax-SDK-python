# RejectedoffertopurchaseImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/rejectedoffertopurchase/{pkiRejectedoffertopurchaseID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.rejectedoffertopurchase_import_into_edmv1_response_m_payload import RejectedoffertopurchaseImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of RejectedoffertopurchaseImportIntoEDMV1ResponseMPayload from a JSON string
rejectedoffertopurchase_import_into_edmv1_response_m_payload_instance = RejectedoffertopurchaseImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(RejectedoffertopurchaseImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
rejectedoffertopurchase_import_into_edmv1_response_m_payload_dict = rejectedoffertopurchase_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of RejectedoffertopurchaseImportIntoEDMV1ResponseMPayload from a dict
rejectedoffertopurchase_import_into_edmv1_response_m_payload_from_dict = RejectedoffertopurchaseImportIntoEDMV1ResponseMPayload.from_dict(rejectedoffertopurchase_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


