# PaymentpreparationImportIntoEDMV1Request

Request for POST /1/object/paymentpreparation/{pkiPaymentpreparationID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.paymentpreparation_import_into_edmv1_request import PaymentpreparationImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentpreparationImportIntoEDMV1Request from a JSON string
paymentpreparation_import_into_edmv1_request_instance = PaymentpreparationImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(PaymentpreparationImportIntoEDMV1Request.to_json())

# convert the object into a dict
paymentpreparation_import_into_edmv1_request_dict = paymentpreparation_import_into_edmv1_request_instance.to_dict()
# create an instance of PaymentpreparationImportIntoEDMV1Request from a dict
paymentpreparation_import_into_edmv1_request_from_dict = PaymentpreparationImportIntoEDMV1Request.from_dict(paymentpreparation_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


