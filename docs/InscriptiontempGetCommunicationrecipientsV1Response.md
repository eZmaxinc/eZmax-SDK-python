# InscriptiontempGetCommunicationrecipientsV1Response

Response for GET /1/object/inscriptiontemp/{pkiInscriptiontempID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InscriptiontempGetCommunicationrecipientsV1ResponseMPayload**](InscriptiontempGetCommunicationrecipientsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptiontemp_get_communicationrecipients_v1_response import InscriptiontempGetCommunicationrecipientsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptiontempGetCommunicationrecipientsV1Response from a JSON string
inscriptiontemp_get_communicationrecipients_v1_response_instance = InscriptiontempGetCommunicationrecipientsV1Response.from_json(json)
# print the JSON string representation of the object
print(InscriptiontempGetCommunicationrecipientsV1Response.to_json())

# convert the object into a dict
inscriptiontemp_get_communicationrecipients_v1_response_dict = inscriptiontemp_get_communicationrecipients_v1_response_instance.to_dict()
# create an instance of InscriptiontempGetCommunicationrecipientsV1Response from a dict
inscriptiontemp_get_communicationrecipients_v1_response_from_dict = InscriptiontempGetCommunicationrecipientsV1Response.from_dict(inscriptiontemp_get_communicationrecipients_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


