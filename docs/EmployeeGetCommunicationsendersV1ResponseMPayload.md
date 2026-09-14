# EmployeeGetCommunicationsendersV1ResponseMPayload

Response for GET /1/object/employee/{pkiEmployeeID}/getCommunicationsenders

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_communicationsenders** | [**List[CustomCommunicationsenderResponse]**](CustomCommunicationsenderResponse.md) |  | 

## Example

```python
from eZmaxApi.models.employee_get_communicationsenders_v1_response_m_payload import EmployeeGetCommunicationsendersV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeGetCommunicationsendersV1ResponseMPayload from a JSON string
employee_get_communicationsenders_v1_response_m_payload_instance = EmployeeGetCommunicationsendersV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(EmployeeGetCommunicationsendersV1ResponseMPayload.to_json())

# convert the object into a dict
employee_get_communicationsenders_v1_response_m_payload_dict = employee_get_communicationsenders_v1_response_m_payload_instance.to_dict()
# create an instance of EmployeeGetCommunicationsendersV1ResponseMPayload from a dict
employee_get_communicationsenders_v1_response_m_payload_from_dict = EmployeeGetCommunicationsendersV1ResponseMPayload.from_dict(employee_get_communicationsenders_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


