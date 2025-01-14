# InscriptionGetCommunicationCountV1ResponseMPayload

Response for GET /1/object/inscription/{pkiInscriptionID}/getCommunicationCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_communication_count** | **int** | The count of Communication. | 

## Example

```python
from eZmaxApi.models.inscription_get_communication_count_v1_response_m_payload import InscriptionGetCommunicationCountV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionGetCommunicationCountV1ResponseMPayload from a JSON string
inscription_get_communication_count_v1_response_m_payload_instance = InscriptionGetCommunicationCountV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(InscriptionGetCommunicationCountV1ResponseMPayload.to_json())

# convert the object into a dict
inscription_get_communication_count_v1_response_m_payload_dict = inscription_get_communication_count_v1_response_m_payload_instance.to_dict()
# create an instance of InscriptionGetCommunicationCountV1ResponseMPayload from a dict
inscription_get_communication_count_v1_response_m_payload_from_dict = InscriptionGetCommunicationCountV1ResponseMPayload.from_dict(inscription_get_communication_count_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


