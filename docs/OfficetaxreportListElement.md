# OfficetaxreportListElement

A Officetaxreport List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_officetaxreport_id** | **int** | The unique ID of the Officetaxreport | 
**fki_period_id** | **int** | The unique ID of the Period | 
**s_period_yyyymm** | **str** | The YYYYMM of the Period | 
**dt_created_date** | **str** | The date and time at which the object was created | 
**s_user_loginname** | **str** | The login name of the User. | 

## Example

```python
from eZmaxApi.models.officetaxreport_list_element import OfficetaxreportListElement

# TODO update the JSON string below
json = "{}"
# create an instance of OfficetaxreportListElement from a JSON string
officetaxreport_list_element_instance = OfficetaxreportListElement.from_json(json)
# print the JSON string representation of the object
print(OfficetaxreportListElement.to_json())

# convert the object into a dict
officetaxreport_list_element_dict = officetaxreport_list_element_instance.to_dict()
# create an instance of OfficetaxreportListElement from a dict
officetaxreport_list_element_from_dict = OfficetaxreportListElement.from_dict(officetaxreport_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


