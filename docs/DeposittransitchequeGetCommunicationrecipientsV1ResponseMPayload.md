# DeposittransitchequeGetCommunicationrecipientsV1ResponseMPayload

Response for GET /1/object/deposittransitcheque/{pkiDeposittransitchequeID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationrecipientsgroup** | [**List[CustomCommunicationrecipientsgroupResponse]**](CustomCommunicationrecipientsgroupResponse.md) |  | 

## Example

```python
from eZmaxApi.models.deposittransitcheque_get_communicationrecipients_v1_response_m_payload import DeposittransitchequeGetCommunicationrecipientsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DeposittransitchequeGetCommunicationrecipientsV1ResponseMPayload from a JSON string
deposittransitcheque_get_communicationrecipients_v1_response_m_payload_instance = DeposittransitchequeGetCommunicationrecipientsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(DeposittransitchequeGetCommunicationrecipientsV1ResponseMPayload.to_json())

# convert the object into a dict
deposittransitcheque_get_communicationrecipients_v1_response_m_payload_dict = deposittransitcheque_get_communicationrecipients_v1_response_m_payload_instance.to_dict()
# create an instance of DeposittransitchequeGetCommunicationrecipientsV1ResponseMPayload from a dict
deposittransitcheque_get_communicationrecipients_v1_response_m_payload_from_dict = DeposittransitchequeGetCommunicationrecipientsV1ResponseMPayload.from_dict(deposittransitcheque_get_communicationrecipients_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


