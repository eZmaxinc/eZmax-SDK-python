# EzsignfolderGetCommunicationListV1Response

Response for GET /1/object/ezsignfolder/{pkiEzsignfolderID}/getCommunicationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfolderGetCommunicationListV1ResponseMPayload**](EzsignfolderGetCommunicationListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_get_communication_list_v1_response import EzsignfolderGetCommunicationListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderGetCommunicationListV1Response from a JSON string
ezsignfolder_get_communication_list_v1_response_instance = EzsignfolderGetCommunicationListV1Response.from_json(json)
# print the JSON string representation of the object
print EzsignfolderGetCommunicationListV1Response.to_json()

# convert the object into a dict
ezsignfolder_get_communication_list_v1_response_dict = ezsignfolder_get_communication_list_v1_response_instance.to_dict()
# create an instance of EzsignfolderGetCommunicationListV1Response from a dict
ezsignfolder_get_communication_list_v1_response_form_dict = ezsignfolder_get_communication_list_v1_response.from_dict(ezsignfolder_get_communication_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


