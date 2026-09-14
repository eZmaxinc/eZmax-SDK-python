# DisclosureGetCommunicationsendersV1ResponseMPayload

Response for GET /1/object/disclosure/{pkiDisclosureID}/getCommunicationsenders

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationsenders** | [**List[CustomCommunicationsenderResponse]**](CustomCommunicationsenderResponse.md) |  | 

## Example

```python
from eZmaxApi.models.disclosure_get_communicationsenders_v1_response_m_payload import DisclosureGetCommunicationsendersV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of DisclosureGetCommunicationsendersV1ResponseMPayload from a JSON string
disclosure_get_communicationsenders_v1_response_m_payload_instance = DisclosureGetCommunicationsendersV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(DisclosureGetCommunicationsendersV1ResponseMPayload.to_json())

# convert the object into a dict
disclosure_get_communicationsenders_v1_response_m_payload_dict = disclosure_get_communicationsenders_v1_response_m_payload_instance.to_dict()
# create an instance of DisclosureGetCommunicationsendersV1ResponseMPayload from a dict
disclosure_get_communicationsenders_v1_response_m_payload_from_dict = DisclosureGetCommunicationsendersV1ResponseMPayload.from_dict(disclosure_get_communicationsenders_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


