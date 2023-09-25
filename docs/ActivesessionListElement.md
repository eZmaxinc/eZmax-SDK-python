# ActivesessionListElement

A Activesession List Element

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_activesession_id** | **int** | The unique ID of the Activesession | 
**fki_user_id** | **int** | The unique ID of the User | 
**fki_computer_id** | **int** | The unique ID of the Computer | 
**fki_company_id** | **int** | The unique ID of the Company | 
**fki_department_id** | **int** | The unique ID of the Department | 
**s_company_name_x** | **str** | The Name of the Company in the language of the requester | 
**s_department_name_x** | **str** | The Name of the Department in the language of the requester | 
**s_activesession_loginname** | **str** | The loginname of the Activesession | 
**s_computer_description** | **str** | The description of the Computer | 
**dt_activesession_firsthit** | **str** | The first hit of the Activesession | 
**dt_activesession_lasthit** | **str** | The last hit of the Activesession | 
**s_activesession_ip** | **str** | Represent an IP address. | 

## Example

```python
from eZmaxApi.models.activesession_list_element import ActivesessionListElement

# TODO update the JSON string below
json = "{}"
# create an instance of ActivesessionListElement from a JSON string
activesession_list_element_instance = ActivesessionListElement.from_json(json)
# print the JSON string representation of the object
print ActivesessionListElement.to_json()

# convert the object into a dict
activesession_list_element_dict = activesession_list_element_instance.to_dict()
# create an instance of ActivesessionListElement from a dict
activesession_list_element_form_dict = activesession_list_element.from_dict(activesession_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


