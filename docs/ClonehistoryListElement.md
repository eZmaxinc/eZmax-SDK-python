# ClonehistoryListElement

A Clonehistory List Element

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_clonehistory_id** | **int** | The unique ID of the Clonehistory | 
**fki_user_id_cloning** | **int** | The unique ID of the User | 
**fki_user_id_cloned** | **int** | The unique ID of the User | 
**dt_clonehistory_firsthit** | **str** | The firsthit of the Clonehistory | 
**dt_clonehistory_lasthit** | **str** | The lasthit of the Clonehistory | [optional] 
**s_user_loginname_cloning** | **str** | The login name of the User. | 
**s_user_firstname_cloning** | **str** | The first name of the user | 
**s_user_lastname_cloning** | **str** | The last name of the user | 
**s_user_loginname_cloned** | **str** | The login name of the User. | 
**s_user_firstname_cloned** | **str** | The first name of the user | 
**s_user_lastname_cloned** | **str** | The last name of the user | 

## Example

```python
from eZmaxApi.models.clonehistory_list_element import ClonehistoryListElement

# TODO update the JSON string below
json = "{}"
# create an instance of ClonehistoryListElement from a JSON string
clonehistory_list_element_instance = ClonehistoryListElement.from_json(json)
# print the JSON string representation of the object
print ClonehistoryListElement.to_json()

# convert the object into a dict
clonehistory_list_element_dict = clonehistory_list_element_instance.to_dict()
# create an instance of ClonehistoryListElement from a dict
clonehistory_list_element_form_dict = clonehistory_list_element.from_dict(clonehistory_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


