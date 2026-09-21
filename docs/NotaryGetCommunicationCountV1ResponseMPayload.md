# NotaryGetCommunicationCountV1ResponseMPayload

Response for GET /1/object/notary/{pkiNotaryID}/getCommunicationCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_communication_count** | **int** | The count of Communication. | 

## Example

```python
from eZmaxApi.models.notary_get_communication_count_v1_response_m_payload import NotaryGetCommunicationCountV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of NotaryGetCommunicationCountV1ResponseMPayload from a JSON string
notary_get_communication_count_v1_response_m_payload_instance = NotaryGetCommunicationCountV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(NotaryGetCommunicationCountV1ResponseMPayload.to_json())

# convert the object into a dict
notary_get_communication_count_v1_response_m_payload_dict = notary_get_communication_count_v1_response_m_payload_instance.to_dict()
# create an instance of NotaryGetCommunicationCountV1ResponseMPayload from a dict
notary_get_communication_count_v1_response_m_payload_from_dict = NotaryGetCommunicationCountV1ResponseMPayload.from_dict(notary_get_communication_count_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


