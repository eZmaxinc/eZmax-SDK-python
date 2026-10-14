# PaymentpreparationGetCommunicationCountV1ResponseMPayload

Response for GET /1/object/paymentpreparation/{pkiPaymentpreparationID}/getCommunicationCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_communication_count** | **int** | The count of Communication. | 

## Example

```python
from eZmaxApi.models.paymentpreparation_get_communication_count_v1_response_m_payload import PaymentpreparationGetCommunicationCountV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentpreparationGetCommunicationCountV1ResponseMPayload from a JSON string
paymentpreparation_get_communication_count_v1_response_m_payload_instance = PaymentpreparationGetCommunicationCountV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(PaymentpreparationGetCommunicationCountV1ResponseMPayload.to_json())

# convert the object into a dict
paymentpreparation_get_communication_count_v1_response_m_payload_dict = paymentpreparation_get_communication_count_v1_response_m_payload_instance.to_dict()
# create an instance of PaymentpreparationGetCommunicationCountV1ResponseMPayload from a dict
paymentpreparation_get_communication_count_v1_response_m_payload_from_dict = PaymentpreparationGetCommunicationCountV1ResponseMPayload.from_dict(paymentpreparation_get_communication_count_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


