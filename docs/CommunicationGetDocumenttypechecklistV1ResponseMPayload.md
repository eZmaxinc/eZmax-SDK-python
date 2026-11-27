# CommunicationGetDocumenttypechecklistV1ResponseMPayload

Response for GET /1/object/communication/{pkiCommunicationID}/getDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.communication_get_documenttypechecklist_v1_response_m_payload import CommunicationGetDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationGetDocumenttypechecklistV1ResponseMPayload from a JSON string
communication_get_documenttypechecklist_v1_response_m_payload_instance = CommunicationGetDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(CommunicationGetDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
communication_get_documenttypechecklist_v1_response_m_payload_dict = communication_get_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of CommunicationGetDocumenttypechecklistV1ResponseMPayload from a dict
communication_get_documenttypechecklist_v1_response_m_payload_from_dict = CommunicationGetDocumenttypechecklistV1ResponseMPayload.from_dict(communication_get_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


