# InscriptiontempGetCommunicationListV1Response

Response for GET /1/object/inscriptiontemp/{pkiInscriptiontempID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InscriptiontempGetCommunicationListV1ResponseMPayload**](InscriptiontempGetCommunicationListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptiontemp_get_communication_list_v1_response import InscriptiontempGetCommunicationListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptiontempGetCommunicationListV1Response from a JSON string
inscriptiontemp_get_communication_list_v1_response_instance = InscriptiontempGetCommunicationListV1Response.from_json(json)
# print the JSON string representation of the object
print InscriptiontempGetCommunicationListV1Response.to_json()

# convert the object into a dict
inscriptiontemp_get_communication_list_v1_response_dict = inscriptiontemp_get_communication_list_v1_response_instance.to_dict()
# create an instance of InscriptiontempGetCommunicationListV1Response from a dict
inscriptiontemp_get_communication_list_v1_response_form_dict = inscriptiontemp_get_communication_list_v1_response.from_dict(inscriptiontemp_get_communication_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


