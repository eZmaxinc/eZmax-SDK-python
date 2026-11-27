# OfficetaxreportGetDocumenttypechecklistV1ResponseMPayload

Response for GET /1/object/officetaxreport/{pkiOfficetaxreportID}/getDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.officetaxreport_get_documenttypechecklist_v1_response_m_payload import OfficetaxreportGetDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of OfficetaxreportGetDocumenttypechecklistV1ResponseMPayload from a JSON string
officetaxreport_get_documenttypechecklist_v1_response_m_payload_instance = OfficetaxreportGetDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(OfficetaxreportGetDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
officetaxreport_get_documenttypechecklist_v1_response_m_payload_dict = officetaxreport_get_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of OfficetaxreportGetDocumenttypechecklistV1ResponseMPayload from a dict
officetaxreport_get_documenttypechecklist_v1_response_m_payload_from_dict = OfficetaxreportGetDocumenttypechecklistV1ResponseMPayload.from_dict(officetaxreport_get_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


