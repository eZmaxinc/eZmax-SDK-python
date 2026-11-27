# OfficetaxreportSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/officetaxreport/{pkiOfficetaxreportID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.officetaxreport_sync_documenttypechecklist_v1_response_m_payload import OfficetaxreportSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of OfficetaxreportSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
officetaxreport_sync_documenttypechecklist_v1_response_m_payload_instance = OfficetaxreportSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(OfficetaxreportSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
officetaxreport_sync_documenttypechecklist_v1_response_m_payload_dict = officetaxreport_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of OfficetaxreportSyncDocumenttypechecklistV1ResponseMPayload from a dict
officetaxreport_sync_documenttypechecklist_v1_response_m_payload_from_dict = OfficetaxreportSyncDocumenttypechecklistV1ResponseMPayload.from_dict(officetaxreport_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


