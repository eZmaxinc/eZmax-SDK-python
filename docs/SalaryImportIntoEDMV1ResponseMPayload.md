# SalaryImportIntoEDMV1ResponseMPayload

Payload for POST /1/object/salary/{pkiSalaryID}/importIntoEDM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_attachment** | [**List[CustomAttachmentImportIntoEDMResponse]**](CustomAttachmentImportIntoEDMResponse.md) |  | 

## Example

```python
from eZmaxApi.models.salary_import_into_edmv1_response_m_payload import SalaryImportIntoEDMV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SalaryImportIntoEDMV1ResponseMPayload from a JSON string
salary_import_into_edmv1_response_m_payload_instance = SalaryImportIntoEDMV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(SalaryImportIntoEDMV1ResponseMPayload.to_json())

# convert the object into a dict
salary_import_into_edmv1_response_m_payload_dict = salary_import_into_edmv1_response_m_payload_instance.to_dict()
# create an instance of SalaryImportIntoEDMV1ResponseMPayload from a dict
salary_import_into_edmv1_response_m_payload_from_dict = SalaryImportIntoEDMV1ResponseMPayload.from_dict(salary_import_into_edmv1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


