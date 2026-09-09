# PaymentpreparationGetAttachmentsV1Response

Response for GET /1/object/paymentpreparation/{pkiPaymentpreparationID}/getAttachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**PaymentpreparationGetAttachmentsV1ResponseMPayload**](PaymentpreparationGetAttachmentsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.paymentpreparation_get_attachments_v1_response import PaymentpreparationGetAttachmentsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentpreparationGetAttachmentsV1Response from a JSON string
paymentpreparation_get_attachments_v1_response_instance = PaymentpreparationGetAttachmentsV1Response.from_json(json)
# print the JSON string representation of the object
print(PaymentpreparationGetAttachmentsV1Response.to_json())

# convert the object into a dict
paymentpreparation_get_attachments_v1_response_dict = paymentpreparation_get_attachments_v1_response_instance.to_dict()
# create an instance of PaymentpreparationGetAttachmentsV1Response from a dict
paymentpreparation_get_attachments_v1_response_from_dict = PaymentpreparationGetAttachmentsV1Response.from_dict(paymentpreparation_get_attachments_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


