# EmployeeImportIntoEDMV1Request

Request for POST /1/object/employee/{pkiEmployeeID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.employee_import_into_edmv1_request import EmployeeImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeImportIntoEDMV1Request from a JSON string
employee_import_into_edmv1_request_instance = EmployeeImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(EmployeeImportIntoEDMV1Request.to_json())

# convert the object into a dict
employee_import_into_edmv1_request_dict = employee_import_into_edmv1_request_instance.to_dict()
# create an instance of EmployeeImportIntoEDMV1Request from a dict
employee_import_into_edmv1_request_from_dict = EmployeeImportIntoEDMV1Request.from_dict(employee_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


