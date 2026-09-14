# DisclosureGetCommunicationCountV1ResponseMPayload

Response for GET /1/object/disclosure/{pkiDisclosureID}/getCommunicationCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_communication_count** | **int** | The count of Communication. | 

## Example

```python
from eZmaxApi.models.disclosure_get_communication_count_v1_response_m_payload import DisclosureGetCommunicationCountV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DisclosureGetCommunicationCountV1ResponseMPayload from a JSON string
disclosure_get_communication_count_v1_response_m_payload_instance = DisclosureGetCommunicationCountV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(DisclosureGetCommunicationCountV1ResponseMPayload.to_json())

# convert the object into a dict
disclosure_get_communication_count_v1_response_m_payload_dict = disclosure_get_communication_count_v1_response_m_payload_instance.to_dict()
# create an instance of DisclosureGetCommunicationCountV1ResponseMPayload from a dict
disclosure_get_communication_count_v1_response_m_payload_from_dict = DisclosureGetCommunicationCountV1ResponseMPayload.from_dict(disclosure_get_communication_count_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


