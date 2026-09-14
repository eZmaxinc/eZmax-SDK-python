# ExternalbrokerGetCommunicationrecipientsV1Response

Response for GET /1/object/externalbroker/{pkiExternalbrokerID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**ExternalbrokerGetCommunicationrecipientsV1ResponseMPayload**](ExternalbrokerGetCommunicationrecipientsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.externalbroker_get_communicationrecipients_v1_response import ExternalbrokerGetCommunicationrecipientsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalbrokerGetCommunicationrecipientsV1Response from a JSON string
externalbroker_get_communicationrecipients_v1_response_instance = ExternalbrokerGetCommunicationrecipientsV1Response.from_json(json)
# print the JSON string representation of the object
print(ExternalbrokerGetCommunicationrecipientsV1Response.to_json())

# convert the object into a dict
externalbroker_get_communicationrecipients_v1_response_dict = externalbroker_get_communicationrecipients_v1_response_instance.to_dict()
# create an instance of ExternalbrokerGetCommunicationrecipientsV1Response from a dict
externalbroker_get_communicationrecipients_v1_response_from_dict = ExternalbrokerGetCommunicationrecipientsV1Response.from_dict(externalbroker_get_communicationrecipients_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


