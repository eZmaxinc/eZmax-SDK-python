# EmployeeImportIntoEDMV1Response

Response for POST /1/object/employee/{pkiEmployeeID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EmployeeImportIntoEDMV1ResponseMPayload**](EmployeeImportIntoEDMV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.employee_import_into_edmv1_response import EmployeeImportIntoEDMV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeImportIntoEDMV1Response from a JSON string
employee_import_into_edmv1_response_instance = EmployeeImportIntoEDMV1Response.from_json(json)
# print the JSON string representation of the object
print(EmployeeImportIntoEDMV1Response.to_json())

# convert the object into a dict
employee_import_into_edmv1_response_dict = employee_import_into_edmv1_response_instance.to_dict()
# create an instance of EmployeeImportIntoEDMV1Response from a dict
employee_import_into_edmv1_response_from_dict = EmployeeImportIntoEDMV1Response.from_dict(employee_import_into_edmv1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


