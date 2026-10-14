# PaymentpreparationGetCommunicationListV1ResponseMPayload

Response for GET /1/object/paymentpreparation/{pkiPaymentpreparationID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communication** | [**List[CustomCommunicationListElementResponse]**](CustomCommunicationListElementResponse.md) |  | 

## Example

```python
from eZmaxApi.models.paymentpreparation_get_communication_list_v1_response_m_payload import PaymentpreparationGetCommunicationListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentpreparationGetCommunicationListV1ResponseMPayload from a JSON string
paymentpreparation_get_communication_list_v1_response_m_payload_instance = PaymentpreparationGetCommunicationListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(PaymentpreparationGetCommunicationListV1ResponseMPayload.to_json())

# convert the object into a dict
paymentpreparation_get_communication_list_v1_response_m_payload_dict = paymentpreparation_get_communication_list_v1_response_m_payload_instance.to_dict()
# create an instance of PaymentpreparationGetCommunicationListV1ResponseMPayload from a dict
paymentpreparation_get_communication_list_v1_response_m_payload_from_dict = PaymentpreparationGetCommunicationListV1ResponseMPayload.from_dict(paymentpreparation_get_communication_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


