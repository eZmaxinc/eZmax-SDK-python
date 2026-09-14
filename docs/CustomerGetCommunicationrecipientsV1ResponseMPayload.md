# CustomerGetCommunicationrecipientsV1ResponseMPayload

Response for GET /1/object/customer/{pkiCustomerID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationrecipientsgroup** | [**List[CustomCommunicationrecipientsgroupResponse]**](CustomCommunicationrecipientsgroupResponse.md) |  | 

## Example

```python
from eZmaxApi.models.customer_get_communicationrecipients_v1_response_m_payload import CustomerGetCommunicationrecipientsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerGetCommunicationrecipientsV1ResponseMPayload from a JSON string
customer_get_communicationrecipients_v1_response_m_payload_instance = CustomerGetCommunicationrecipientsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CustomerGetCommunicationrecipientsV1ResponseMPayload.to_json())

# convert the object into a dict
customer_get_communicationrecipients_v1_response_m_payload_dict = customer_get_communicationrecipients_v1_response_m_payload_instance.to_dict()
# create an instance of CustomerGetCommunicationrecipientsV1ResponseMPayload from a dict
customer_get_communicationrecipients_v1_response_m_payload_from_dict = CustomerGetCommunicationrecipientsV1ResponseMPayload.from_dict(customer_get_communicationrecipients_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


