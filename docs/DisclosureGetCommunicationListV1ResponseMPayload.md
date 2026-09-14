# DisclosureGetCommunicationListV1ResponseMPayload

Response for GET /1/object/disclosure/{pkiDisclosureID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communication** | [**List[CustomCommunicationListElementResponse]**](CustomCommunicationListElementResponse.md) |  | 

## Example

```python
from eZmaxApi.models.disclosure_get_communication_list_v1_response_m_payload import DisclosureGetCommunicationListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DisclosureGetCommunicationListV1ResponseMPayload from a JSON string
disclosure_get_communication_list_v1_response_m_payload_instance = DisclosureGetCommunicationListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(DisclosureGetCommunicationListV1ResponseMPayload.to_json())

# convert the object into a dict
disclosure_get_communication_list_v1_response_m_payload_dict = disclosure_get_communication_list_v1_response_m_payload_instance.to_dict()
# create an instance of DisclosureGetCommunicationListV1ResponseMPayload from a dict
disclosure_get_communication_list_v1_response_m_payload_from_dict = DisclosureGetCommunicationListV1ResponseMPayload.from_dict(disclosure_get_communication_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


