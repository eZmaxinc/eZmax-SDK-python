# EmployeeImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/employee/{pkiEmployeeID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.employee_import_into_edmv1_response_m_payload import EmployeeImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeImportIntoEDMV1ResponseMPayload from a JSON string
employee_import_into_edmv1_response_m_payload_instance = EmployeeImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EmployeeImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
employee_import_into_edmv1_response_m_payload_dict = employee_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of EmployeeImportIntoEDMV1ResponseMPayload from a dict
employee_import_into_edmv1_response_m_payload_from_dict = EmployeeImportIntoEDMV1ResponseMPayload.from_dict(employee_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


