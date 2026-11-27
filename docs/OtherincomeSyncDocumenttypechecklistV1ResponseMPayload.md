# OtherincomeSyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/otherincome/{pkiOtherincomeID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.otherincome_sync_documenttypechecklist_v1_response_m_payload import OtherincomeSyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of OtherincomeSyncDocumenttypechecklistV1ResponseMPayload from a JSON string
otherincome_sync_documenttypechecklist_v1_response_m_payload_instance = OtherincomeSyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(OtherincomeSyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
otherincome_sync_documenttypechecklist_v1_response_m_payload_dict = otherincome_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of OtherincomeSyncDocumenttypechecklistV1ResponseMPayload from a dict
otherincome_sync_documenttypechecklist_v1_response_m_payload_from_dict = OtherincomeSyncDocumenttypechecklistV1ResponseMPayload.from_dict(otherincome_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


