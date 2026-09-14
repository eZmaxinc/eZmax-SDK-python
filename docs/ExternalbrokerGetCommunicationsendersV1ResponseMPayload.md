# ExternalbrokerGetCommunicationsendersV1ResponseMPayload

Response for GET /1/object/externalbroker/{pkiExternalbrokerID}/getCommunicationsenders

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationsenders** | [**List[CustomCommunicationsenderResponse]**](CustomCommunicationsenderResponse.md) |  | 

## Example

```python
from eZmaxApi.models.externalbroker_get_communicationsenders_v1_response_m_payload import ExternalbrokerGetCommunicationsendersV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalbrokerGetCommunicationsendersV1ResponseMPayload from a JSON string
externalbroker_get_communicationsenders_v1_response_m_payload_instance = ExternalbrokerGetCommunicationsendersV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(ExternalbrokerGetCommunicationsendersV1ResponseMPayload.to_json())

# convert the object into a dict
externalbroker_get_communicationsenders_v1_response_m_payload_dict = externalbroker_get_communicationsenders_v1_response_m_payload_instance.to_dict()
# create an instance of ExternalbrokerGetCommunicationsendersV1ResponseMPayload from a dict
externalbroker_get_communicationsenders_v1_response_m_payload_from_dict = ExternalbrokerGetCommunicationsendersV1ResponseMPayload.from_dict(externalbroker_get_communicationsenders_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


