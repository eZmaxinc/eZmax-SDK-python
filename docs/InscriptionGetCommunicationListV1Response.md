# InscriptionGetCommunicationListV1Response

Response for GET /1/object/inscription/{pkiInscriptionID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InscriptionGetCommunicationListV1ResponseMPayload**](InscriptionGetCommunicationListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.inscription_get_communication_list_v1_response import InscriptionGetCommunicationListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionGetCommunicationListV1Response from a JSON string
inscription_get_communication_list_v1_response_instance = InscriptionGetCommunicationListV1Response.from_json(json)
# print the JSON string representation of the object
print(InscriptionGetCommunicationListV1Response.to_json())

# convert the object into a dict
inscription_get_communication_list_v1_response_dict = inscription_get_communication_list_v1_response_instance.to_dict()
# create an instance of InscriptionGetCommunicationListV1Response from a dict
inscription_get_communication_list_v1_response_form_dict = inscription_get_communication_list_v1_response.from_dict(inscription_get_communication_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


