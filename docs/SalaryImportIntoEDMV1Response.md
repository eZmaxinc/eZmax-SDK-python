# SalaryImportIntoEDMV1Response

Response for POST /1/object/salary/{pkiSalaryID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**SalaryImportIntoEDMV1ResponseMPayload**](SalaryImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.salary_import_into_edmv1_response import SalaryImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of SalaryImportIntoEDMV1Response from a JSON string
salary_import_into_edmv1_response_instance = SalaryImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(SalaryImportIntoEDMV1Response.to_json())

# convert the object into a dict
salary_import_into_edmv1_response_dict = salary_import_into_edmv1_response_instance.to_dict()
# create an instance of SalaryImportIntoEDMV1Response from a dict
salary_import_into_edmv1_response_from_dict = SalaryImportIntoEDMV1Response.from_dict(salary_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


