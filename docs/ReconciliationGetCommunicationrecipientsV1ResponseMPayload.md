# ReconciliationGetCommunicationrecipientsV1ResponseMPayload

Response for GET /1/object/reconciliation/{pkiReconciliationID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationrecipientsgroup** | [**List[CustomCommunicationrecipientsgroupResponse]**](CustomCommunicationrecipientsgroupResponse.md) |  | 

## Example

```python
from eZmaxApi.models.reconciliation_get_communicationrecipients_v1_response_m_payload import ReconciliationGetCommunicationrecipientsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ReconciliationGetCommunicationrecipientsV1ResponseMPayload from a JSON string
reconciliation_get_communicationrecipients_v1_response_m_payload_instance = ReconciliationGetCommunicationrecipientsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(ReconciliationGetCommunicationrecipientsV1ResponseMPayload.to_json())

# convert the object into a dict
reconciliation_get_communicationrecipients_v1_response_m_payload_dict = reconciliation_get_communicationrecipients_v1_response_m_payload_instance.to_dict()
# create an instance of ReconciliationGetCommunicationrecipientsV1ResponseMPayload from a dict
reconciliation_get_communicationrecipients_v1_response_m_payload_from_dict = ReconciliationGetCommunicationrecipientsV1ResponseMPayload.from_dict(reconciliation_get_communicationrecipients_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


