# EmployeeGetAttachmentsV1Response

Response for GET /1/object/employee/{pkiEmployeeID}/getAttachments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EmployeeGetAttachmentsV1ResponseMPayload**](EmployeeGetAttachmentsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.employee_get_attachments_v1_response import EmployeeGetAttachmentsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeGetAttachmentsV1Response from a JSON string
employee_get_attachments_v1_response_instance = EmployeeGetAttachmentsV1Response.from_json(json)
# print the JSON string representation of the object
print(EmployeeGetAttachmentsV1Response.to_json())

# convert the object into a dict
employee_get_attachments_v1_response_dict = employee_get_attachments_v1_response_instance.to_dict()
# create an instance of EmployeeGetAttachmentsV1Response from a dict
employee_get_attachments_v1_response_from_dict = EmployeeGetAttachmentsV1Response.from_dict(employee_get_attachments_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


