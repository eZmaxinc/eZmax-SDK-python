# BrokerGetCommunicationCountV1ResponseMPayload

Response for GET /1/object/broker/{pkiBrokerID}/getCommunicationCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_communication_count** | **int** | The count of Communication. | 

## Example

```python
from eZmaxApi.models.broker_get_communication_count_v1_response_m_payload import BrokerGetCommunicationCountV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BrokerGetCommunicationCountV1ResponseMPayload from a JSON string
broker_get_communication_count_v1_response_m_payload_instance = BrokerGetCommunicationCountV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(BrokerGetCommunicationCountV1ResponseMPayload.to_json())

# convert the object into a dict
broker_get_communication_count_v1_response_m_payload_dict = broker_get_communication_count_v1_response_m_payload_instance.to_dict()
# create an instance of BrokerGetCommunicationCountV1ResponseMPayload from a dict
broker_get_communication_count_v1_response_m_payload_from_dict = BrokerGetCommunicationCountV1ResponseMPayload.from_dict(broker_get_communication_count_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


