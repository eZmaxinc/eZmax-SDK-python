# SalarySyncDocumenttypechecklistV1ResponseMPayload

Response for POST /1/object/salary/{pkiSalaryID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.salary_sync_documenttypechecklist_v1_response_m_payload import SalarySyncDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SalarySyncDocumenttypechecklistV1ResponseMPayload from a JSON string
salary_sync_documenttypechecklist_v1_response_m_payload_instance = SalarySyncDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(SalarySyncDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
salary_sync_documenttypechecklist_v1_response_m_payload_dict = salary_sync_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of SalarySyncDocumenttypechecklistV1ResponseMPayload from a dict
salary_sync_documenttypechecklist_v1_response_m_payload_from_dict = SalarySyncDocumenttypechecklistV1ResponseMPayload.from_dict(salary_sync_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


