# PaymentpreparationImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/paymentpreparation/{pkiPaymentpreparationID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.paymentpreparation_import_into_edmv1_response_m_payload import PaymentpreparationImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentpreparationImportIntoEDMV1ResponseMPayload from a JSON string
paymentpreparation_import_into_edmv1_response_m_payload_instance = PaymentpreparationImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(PaymentpreparationImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
paymentpreparation_import_into_edmv1_response_m_payload_dict = paymentpreparation_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of PaymentpreparationImportIntoEDMV1ResponseMPayload from a dict
paymentpreparation_import_into_edmv1_response_m_payload_from_dict = PaymentpreparationImportIntoEDMV1ResponseMPayload.from_dict(paymentpreparation_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


