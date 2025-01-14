# InscriptiontempGetCommunicationCountV1Response

Response for GET /1/object/inscriptiontemp/{pkiInscriptiontempID}/getCommunicationCount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InscriptiontempGetCommunicationCountV1ResponseMPayload**](InscriptiontempGetCommunicationCountV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptiontemp_get_communication_count_v1_response import InscriptiontempGetCommunicationCountV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptiontempGetCommunicationCountV1Response from a JSON string
inscriptiontemp_get_communication_count_v1_response_instance = InscriptiontempGetCommunicationCountV1Response.from_json(json)
# print the JSON string representation of the object
print(InscriptiontempGetCommunicationCountV1Response.to_json())

# convert the object into a dict
inscriptiontemp_get_communication_count_v1_response_dict = inscriptiontemp_get_communication_count_v1_response_instance.to_dict()
# create an instance of InscriptiontempGetCommunicationCountV1Response from a dict
inscriptiontemp_get_communication_count_v1_response_from_dict = InscriptiontempGetCommunicationCountV1Response.from_dict(inscriptiontemp_get_communication_count_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


