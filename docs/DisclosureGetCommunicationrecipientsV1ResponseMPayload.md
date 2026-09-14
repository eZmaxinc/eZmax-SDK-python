# DisclosureGetCommunicationrecipientsV1ResponseMPayload

Response for GET /1/object/disclosure/{pkiDisclosureID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationrecipientsgroup** | [**List[CustomCommunicationrecipientsgroupResponse]**](CustomCommunicationrecipientsgroupResponse.md) |  | 

## Example

```python
from eZmaxApi.models.disclosure_get_communicationrecipients_v1_response_m_payload import DisclosureGetCommunicationrecipientsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DisclosureGetCommunicationrecipientsV1ResponseMPayload from a JSON string
disclosure_get_communicationrecipients_v1_response_m_payload_instance = DisclosureGetCommunicationrecipientsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(DisclosureGetCommunicationrecipientsV1ResponseMPayload.to_json())

# convert the object into a dict
disclosure_get_communicationrecipients_v1_response_m_payload_dict = disclosure_get_communicationrecipients_v1_response_m_payload_instance.to_dict()
# create an instance of DisclosureGetCommunicationrecipientsV1ResponseMPayload from a dict
disclosure_get_communicationrecipients_v1_response_m_payload_from_dict = DisclosureGetCommunicationrecipientsV1ResponseMPayload.from_dict(disclosure_get_communicationrecipients_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


