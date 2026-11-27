# PaymentpreparationSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/paymentpreparation/{pkiPaymentpreparationID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.paymentpreparation_sync_documenttypechecklist_v1_response_m_payload import PaymentpreparationSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentpreparationSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
paymentpreparation_sync_documenttypechecklist_v1_response_m_payload_instance = PaymentpreparationSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(PaymentpreparationSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
paymentpreparation_sync_documenttypechecklist_v1_response_m_payload_dict = paymentpreparation_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of PaymentpreparationSyncDocumenttypechecklistV1ResponseMPayload from a dict
paymentpreparation_sync_documenttypechecklist_v1_response_m_payload_from_dict = PaymentpreparationSyncDocumenttypechecklistV1ResponseMPayload.from_dict(paymentpreparation_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


