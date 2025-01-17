# RejectedoffertopurchaseGetCommunicationrecipientsV1Response

Response for GET /1/object/rejectedoffertopurchase/{pkiRejectedoffertopurchaseID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**RejectedoffertopurchaseGetCommunicationrecipientsV1ResponseMPayload**](RejectedoffertopurchaseGetCommunicationrecipientsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.rejectedoffertopurchase_get_communicationrecipients_v1_response import RejectedoffertopurchaseGetCommunicationrecipientsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of RejectedoffertopurchaseGetCommunicationrecipientsV1Response from a JSON string
rejectedoffertopurchase_get_communicationrecipients_v1_response_instance = RejectedoffertopurchaseGetCommunicationrecipientsV1Response.from_json(json)
# print the JSON string representation of the object
print(RejectedoffertopurchaseGetCommunicationrecipientsV1Response.to_json())

# convert the object into a dict
rejectedoffertopurchase_get_communicationrecipients_v1_response_dict = rejectedoffertopurchase_get_communicationrecipients_v1_response_instance.to_dict()
# create an instance of RejectedoffertopurchaseGetCommunicationrecipientsV1Response from a dict
rejectedoffertopurchase_get_communicationrecipients_v1_response_from_dict = RejectedoffertopurchaseGetCommunicationrecipientsV1Response.from_dict(rejectedoffertopurchase_get_communicationrecipients_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


