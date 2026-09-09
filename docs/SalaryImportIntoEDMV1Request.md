# SalaryImportIntoEDMV1Request

Request for POST /1/object/salary/{pkiSalaryID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMRequest]**](CustomAttachmentImportIntoEDMRequest.md) |  | 

## Example

```python
from eZmaxApi.models.salary_import_into_edmv1_request import SalaryImportIntoEDMV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of SalaryImportIntoEDMV1Request from a JSON string
salary_import_into_edmv1_request_instance = SalaryImportIntoEDMV1Request.from_json(json)
# print the JSON string representation of the object
print(SalaryImportIntoEDMV1Request.to_json())

# convert the object into a dict
salary_import_into_edmv1_request_dict = salary_import_into_edmv1_request_instance.to_dict()
# create an instance of SalaryImportIntoEDMV1Request from a dict
salary_import_into_edmv1_request_from_dict = SalaryImportIntoEDMV1Request.from_dict(salary_import_into_edmv1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


