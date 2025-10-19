# EmployeeListElement

A Employee List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_employee_id** | **int** | The unique ID of the Employee. | 
**fki_department_id** | **int** | The unique ID of the Department | 
**s_employee_code** | **str** | The code of the Employee | 
**s_employee_internalcode** | **str** | The internalcode of the Employee | 
**b_employee_isactive** | **bool** | Whether the employee is active or not | 
**dt_employee_hiredate** | **str** | The hiredate of the Employee | [optional] 
**dt_employee_leavedate** | **str** | The leavedate of the Employee | [optional] 
**s_department_name_x** | **str** | The Name of the Department in the language of the requester | [optional] 
**s_contact_firstname** | **str** | The First name of the contact | [optional] 
**s_contact_lastname** | **str** | The Last name of the contact | [optional] 
**s_phone_e164** | **str** | A phone number in E.164 Format | [optional] 
**s_email_address** | **str** | The email address. | [optional] 
**s_address_civic** | **str** | The Civic number. | [optional] 
**s_address_street** | **str** | The Street Name | [optional] 
**s_address_suite** | **str** | The Suite or appartment number | [optional] 
**s_address_city** | **str** | The City name | [optional] 
**s_address_zip** | **str** | The Postal/Zip Code  The value must be entered without spaces | [optional] 
**s_province_name_x** | **str** | The name of the Province in the language of the requester | [optional] 
**s_country_name_x** | **str** | The name of the Country in the language of the requester | [optional] 

## Example

```python
from eZmaxApi.models.employee_list_element import EmployeeListElement

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeListElement from a JSON string
employee_list_element_instance = EmployeeListElement.from_json(json)
# print the JSON string representation of the object
print(EmployeeListElement.to_json())

# convert the object into a dict
employee_list_element_dict = employee_list_element_instance.to_dict()
# create an instance of EmployeeListElement from a dict
employee_list_element_from_dict = EmployeeListElement.from_dict(employee_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


