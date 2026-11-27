# OtherincomeSyncDocumenttypechecklistV1Response

Response for POST /1/object/otherincome/{pkiOtherincomeID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**OtherincomeSyncDocumenttypechecklistV1ResponseMPayload**](OtherincomeSyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.otherincome_sync_documenttypechecklist_v1_response import OtherincomeSyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of OtherincomeSyncDocumenttypechecklistV1Response from a JSON string
otherincome_sync_documenttypechecklist_v1_response_instance = OtherincomeSyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(OtherincomeSyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
otherincome_sync_documenttypechecklist_v1_response_dict = otherincome_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of OtherincomeSyncDocumenttypechecklistV1Response from a dict
otherincome_sync_documenttypechecklist_v1_response_from_dict = OtherincomeSyncDocumenttypechecklistV1Response.from_dict(otherincome_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


