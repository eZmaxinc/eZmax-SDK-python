# PurchaseImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/purchase/{pkiPurchaseID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.purchase_import_into_edmv1_response_m_payload import PurchaseImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseImportIntoEDMV1ResponseMPayload from a JSON string
purchase_import_into_edmv1_response_m_payload_instance = PurchaseImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(PurchaseImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
purchase_import_into_edmv1_response_m_payload_dict = purchase_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of PurchaseImportIntoEDMV1ResponseMPayload from a dict
purchase_import_into_edmv1_response_m_payload_from_dict = PurchaseImportIntoEDMV1ResponseMPayload.from_dict(purchase_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


