# SalaryListElement

A Salary List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_salary_id** | **int** | The unique ID of the Salary | 
**fki_period_id** | **int** | The unique ID of the Period | 
**fki_salaryperiod_id** | **int** | The unique ID of the Salaryperiod | 
**fki_u_ser_id_created** | **int** | The unique ID of the User | [optional] 
**dt_salary_paymentdate** | **str** | The paymentdate of the Salary | 
**s_salaryperiod** | **str** | The period in Salaryperiodgroup | [optional] 
**s_period_yyyymm** | **str** | The YYYYMM of the Period | [optional] 
**i_salarypreparation_count** | **int** | The count of Salarypreparation. | [optional] 
**d_salarypreparation_total** | **str** | The total of the Salarypreparation | [optional] 
**dt_salaryperiod_start** | **str** | The start of the Salaryperiod | [optional] 
**dt_salaryperiod_end** | **str** | The end of the Salaryperiod | [optional] 
**s_user_loginname** | **str** | The login name of the User. | [optional] 
**dt_created_date** | **str** | The date and time at which the object was created | [optional] 
**b_salarypreparation_ispaid** | **bool** | Whether if it&#39;s an ispaid | [optional] 
**i_salaryperiodgroup_year** | **int** | The year of the Salaryperiodgroup | [optional] 

## Example

```python
from eZmaxApi.models.salary_list_element import SalaryListElement

# TODO update the JSON string below
json = "{}"
# create an instance of SalaryListElement from a JSON string
salary_list_element_instance = SalaryListElement.from_json(json)
# print the JSON string representation of the object
print(SalaryListElement.to_json())

# convert the object into a dict
salary_list_element_dict = salary_list_element_instance.to_dict()
# create an instance of SalaryListElement from a dict
salary_list_element_from_dict = SalaryListElement.from_dict(salary_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


