# SalarySyncDocumenttypechecklistV1Response

Response for POST /1/object/salary/{pkiSalaryID}/syncDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**SalarySyncDocumenttypechecklistV1ResponseMPayload**](SalarySyncDocumenttypechecklistV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.salary_sync_documenttypechecklist_v1_response import SalarySyncDocumenttypechecklistV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of SalarySyncDocumenttypechecklistV1Response from a JSON string
salary_sync_documenttypechecklist_v1_response_instance = SalarySyncDocumenttypechecklistV1Response.from_json(json)
# print the JSON string representation of the object
print(SalarySyncDocumenttypechecklistV1Response.to_json())

# convert the object into a dict
salary_sync_documenttypechecklist_v1_response_dict = salary_sync_documenttypechecklist_v1_response_instance.to_dict()
# create an instance of SalarySyncDocumenttypechecklistV1Response from a dict
salary_sync_documenttypechecklist_v1_response_from_dict = SalarySyncDocumenttypechecklistV1Response.from_dict(salary_sync_documenttypechecklist_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


