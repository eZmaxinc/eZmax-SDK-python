# TranqcontractGetCommunicationrecipientsV1ResponseMPayload

Response for GET /1/object/tranqcontract/{pkiTranqcontractID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationrecipientsgroup** | [**List[CustomCommunicationrecipientsgroupResponse]**](CustomCommunicationrecipientsgroupResponse.md) |  | 

## Example

```python
from eZmaxApi.models.tranqcontract_get_communicationrecipients_v1_response_m_payload import TranqcontractGetCommunicationrecipientsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of TranqcontractGetCommunicationrecipientsV1ResponseMPayload from a JSON string
tranqcontract_get_communicationrecipients_v1_response_m_payload_instance = TranqcontractGetCommunicationrecipientsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(TranqcontractGetCommunicationrecipientsV1ResponseMPayload.to_json())

# convert the object into a dict
tranqcontract_get_communicationrecipients_v1_response_m_payload_dict = tranqcontract_get_communicationrecipients_v1_response_m_payload_instance.to_dict()
# create an instance of TranqcontractGetCommunicationrecipientsV1ResponseMPayload from a dict
tranqcontract_get_communicationrecipients_v1_response_m_payload_from_dict = TranqcontractGetCommunicationrecipientsV1ResponseMPayload.from_dict(tranqcontract_get_communicationrecipients_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


