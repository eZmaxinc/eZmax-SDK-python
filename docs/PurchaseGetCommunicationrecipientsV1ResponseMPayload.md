# PurchaseGetCommunicationrecipientsV1ResponseMPayload

Response for GET /1/object/purchase/{pkiPurchaseID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationrecipientsgroup** | [**List[CustomCommunicationrecipientsgroupResponse]**](CustomCommunicationrecipientsgroupResponse.md) |  | 

## Example

```python
from eZmaxApi.models.purchase_get_communicationrecipients_v1_response_m_payload import PurchaseGetCommunicationrecipientsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseGetCommunicationrecipientsV1ResponseMPayload from a JSON string
purchase_get_communicationrecipients_v1_response_m_payload_instance = PurchaseGetCommunicationrecipientsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(PurchaseGetCommunicationrecipientsV1ResponseMPayload.to_json())

# convert the object into a dict
purchase_get_communicationrecipients_v1_response_m_payload_dict = purchase_get_communicationrecipients_v1_response_m_payload_instance.to_dict()
# create an instance of PurchaseGetCommunicationrecipientsV1ResponseMPayload from a dict
purchase_get_communicationrecipients_v1_response_m_payload_from_dict = PurchaseGetCommunicationrecipientsV1ResponseMPayload.from_dict(purchase_get_communicationrecipients_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


