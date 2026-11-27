# OfficetaxreportSyncDocumenttypechecklistV1Response

Response for POST /1/object/officetaxreport/{pkiOfficetaxreportID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**OfficetaxreportSyncDocumenttypechecklistV1ResponseMPayload**](OfficetaxreportSyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.officetaxreport_sync_documenttypechecklist_v1_response import OfficetaxreportSyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of OfficetaxreportSyncDocumenttypechecklistV1Response from a JSON string
officetaxreport_sync_documenttypechecklist_v1_response_instance = OfficetaxreportSyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(OfficetaxreportSyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
officetaxreport_sync_documenttypechecklist_v1_response_dict = officetaxreport_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of OfficetaxreportSyncDocumenttypechecklistV1Response from a dict
officetaxreport_sync_documenttypechecklist_v1_response_from_dict = OfficetaxreportSyncDocumenttypechecklistV1Response.from_dict(officetaxreport_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


