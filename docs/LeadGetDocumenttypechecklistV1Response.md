# LeadGetDocumenttypechecklistV1Response

Response for GET /1/object/lead/{pkiLeadID}/getDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**LeadGetDocumenttypechecklistV1ResponseMPayload**](LeadGetDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.lead_get_documenttypechecklist_v1_response import LeadGetDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of LeadGetDocumenttypechecklistV1Response from a JSON string
lead_get_documenttypechecklist_v1_response_instance = LeadGetDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(LeadGetDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
lead_get_documenttypechecklist_v1_response_dict = lead_get_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of LeadGetDocumenttypechecklistV1Response from a dict
lead_get_documenttypechecklist_v1_response_from_dict = LeadGetDocumenttypechecklistV1Response.from_dict(lead_get_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


