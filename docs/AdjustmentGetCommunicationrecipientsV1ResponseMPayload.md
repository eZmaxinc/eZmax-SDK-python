# AdjustmentGetCommunicationrecipientsV1ResponseMPayload

Response for GET /1/object/adjustment/{pkiAdjustmentID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationrecipientsgroup** | [**List[CustomCommunicationrecipientsgroupResponse]**](CustomCommunicationrecipientsgroupResponse.md) |  | 

## Example

```python
from eZmaxApi.models.adjustment_get_communicationrecipients_v1_response_m_payload import AdjustmentGetCommunicationrecipientsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AdjustmentGetCommunicationrecipientsV1ResponseMPayload from a JSON string
adjustment_get_communicationrecipients_v1_response_m_payload_instance = AdjustmentGetCommunicationrecipientsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(AdjustmentGetCommunicationrecipientsV1ResponseMPayload.to_json())

# convert the object into a dict
adjustment_get_communicationrecipients_v1_response_m_payload_dict = adjustment_get_communicationrecipients_v1_response_m_payload_instance.to_dict()
# create an instance of AdjustmentGetCommunicationrecipientsV1ResponseMPayload from a dict
adjustment_get_communicationrecipients_v1_response_m_payload_from_dict = AdjustmentGetCommunicationrecipientsV1ResponseMPayload.from_dict(adjustment_get_communicationrecipients_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


