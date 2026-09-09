# SalaryGetAttachmentsV1Response

Response for GET /1/object/salary/{pkiSalaryID}/getAttachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**SalaryGetAttachmentsV1ResponseMPayload**](SalaryGetAttachmentsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.salary_get_attachments_v1_response import SalaryGetAttachmentsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of SalaryGetAttachmentsV1Response from a JSON string
salary_get_attachments_v1_response_instance = SalaryGetAttachmentsV1Response.from_json(json)
# print the JSON string representation of the object
print(SalaryGetAttachmentsV1Response.to_json())

# convert the object into a dict
salary_get_attachments_v1_response_dict = salary_get_attachments_v1_response_instance.to_dict()
# create an instance of SalaryGetAttachmentsV1Response from a dict
salary_get_attachments_v1_response_from_dict = SalaryGetAttachmentsV1Response.from_dict(salary_get_attachments_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


