# EzsignfolderGetCommunicationrecipientsV1Response

Response for GET /1/object/ezsignfolder/{pkiEzsignfolderID}/getCommunicationrecipients

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfolderGetCommunicationrecipientsV1ResponseMPayload**](EzsignfolderGetCommunicationrecipientsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_get_communicationrecipients_v1_response import EzsignfolderGetCommunicationrecipientsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderGetCommunicationrecipientsV1Response from a JSON string
ezsignfolder_get_communicationrecipients_v1_response_instance = EzsignfolderGetCommunicationrecipientsV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderGetCommunicationrecipientsV1Response.to_json())

# convert the object into a dict
ezsignfolder_get_communicationrecipients_v1_response_dict = ezsignfolder_get_communicationrecipients_v1_response_instance.to_dict()
# create an instance of EzsignfolderGetCommunicationrecipientsV1Response from a dict
ezsignfolder_get_communicationrecipients_v1_response_from_dict = EzsignfolderGetCommunicationrecipientsV1Response.from_dict(ezsignfolder_get_communicationrecipients_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


