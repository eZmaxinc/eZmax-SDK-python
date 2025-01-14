# OtherincomeGetCommunicationrecipientsV1ResponseMPayload

Response for GET /1/object/otherincome/{pkiOtherincomeID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationrecipientsgroup** | [**List[CustomCommunicationrecipientsgroupResponse]**](CustomCommunicationrecipientsgroupResponse.md) |  | 

## Example

```python
from eZmaxApi.models.otherincome_get_communicationrecipients_v1_response_m_payload import OtherincomeGetCommunicationrecipientsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of OtherincomeGetCommunicationrecipientsV1ResponseMPayload from a JSON string
otherincome_get_communicationrecipients_v1_response_m_payload_instance = OtherincomeGetCommunicationrecipientsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(OtherincomeGetCommunicationrecipientsV1ResponseMPayload.to_json())

# convert the object into a dict
otherincome_get_communicationrecipients_v1_response_m_payload_dict = otherincome_get_communicationrecipients_v1_response_m_payload_instance.to_dict()
# create an instance of OtherincomeGetCommunicationrecipientsV1ResponseMPayload from a dict
otherincome_get_communicationrecipients_v1_response_m_payload_from_dict = OtherincomeGetCommunicationrecipientsV1ResponseMPayload.from_dict(otherincome_get_communicationrecipients_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


