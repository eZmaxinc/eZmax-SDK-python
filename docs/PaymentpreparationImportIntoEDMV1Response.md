# PaymentpreparationImportIntoEDMV1Response

Response for POST /1/object/paymentpreparation/{pkiPaymentpreparationID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**PaymentpreparationImportIntoEDMV1ResponseMPayload**](PaymentpreparationImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.paymentpreparation_import_into_edmv1_response import PaymentpreparationImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentpreparationImportIntoEDMV1Response from a JSON string
paymentpreparation_import_into_edmv1_response_instance = PaymentpreparationImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(PaymentpreparationImportIntoEDMV1Response.to_json())

# convert the object into a dict
paymentpreparation_import_into_edmv1_response_dict = paymentpreparation_import_into_edmv1_response_instance.to_dict()
# create an instance of PaymentpreparationImportIntoEDMV1Response from a dict
paymentpreparation_import_into_edmv1_response_from_dict = PaymentpreparationImportIntoEDMV1Response.from_dict(paymentpreparation_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


