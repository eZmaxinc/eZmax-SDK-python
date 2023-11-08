# InscriptiontempGetCommunicationListV1ResponseMPayload

Response for GET /1/object/inscriptiontemp/{pkiInscriptiontempID}/getCommunicationList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communication** | [**List[CustomCommunicationListElementResponse]**](CustomCommunicationListElementResponse.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptiontemp_get_communication_list_v1_response_m_payload import InscriptiontempGetCommunicationListV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptiontempGetCommunicationListV1ResponseMPayload from a JSON string
inscriptiontemp_get_communication_list_v1_response_m_payload_instance = InscriptiontempGetCommunicationListV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print InscriptiontempGetCommunicationListV1ResponseMPayload.to_json()

# convert the object into a dict
inscriptiontemp_get_communication_list_v1_response_m_payload_dict = inscriptiontemp_get_communication_list_v1_response_m_payload_instance.to_dict()
# create an instance of InscriptiontempGetCommunicationListV1ResponseMPayload from a dict
inscriptiontemp_get_communication_list_v1_response_m_payload_form_dict = inscriptiontemp_get_communication_list_v1_response_m_payload.from_dict(inscriptiontemp_get_communication_list_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


