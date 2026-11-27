# DisclosureSyncDocumenttypechecklistV1Response

Response for POST /1/object/disclosure/{pkiDisclosureID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DisclosureSyncDocumenttypechecklistV1ResponseMPayload**](DisclosureSyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.disclosure_sync_documenttypechecklist_v1_response import DisclosureSyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DisclosureSyncDocumenttypechecklistV1Response from a JSON string
disclosure_sync_documenttypechecklist_v1_response_instance = DisclosureSyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(DisclosureSyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
disclosure_sync_documenttypechecklist_v1_response_dict = disclosure_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of DisclosureSyncDocumenttypechecklistV1Response from a dict
disclosure_sync_documenttypechecklist_v1_response_from_dict = DisclosureSyncDocumenttypechecklistV1Response.from_dict(disclosure_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


