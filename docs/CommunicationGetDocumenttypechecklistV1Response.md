# CommunicationGetDocumenttypechecklistV1Response

Response for GET /1/object/communication/{pkiCommunicationID}/getDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**CommunicationGetDocumenttypechecklistV1ResponseMPayload**](CommunicationGetDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.communication_get_documenttypechecklist_v1_response import CommunicationGetDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationGetDocumenttypechecklistV1Response from a JSON string
communication_get_documenttypechecklist_v1_response_instance = CommunicationGetDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(CommunicationGetDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
communication_get_documenttypechecklist_v1_response_dict = communication_get_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of CommunicationGetDocumenttypechecklistV1Response from a dict
communication_get_documenttypechecklist_v1_response_from_dict = CommunicationGetDocumenttypechecklistV1Response.from_dict(communication_get_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


