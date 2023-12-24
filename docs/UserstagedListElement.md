# UserstagedListElement

A Userstaged List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_userstaged_id** | **int** | The unique ID of the Userstaged | 
**s_email_address** | **str** | The email address. | 
**s_userstaged_firstname** | **str** | The firstname of the Userstaged | 
**s_userstaged_lastname** | **str** | The lastname of the Userstaged | 
**s_userstaged_externalid** | **str** | The externalid of the Userstaged | 

## Example

```python
from eZmaxApi.models.userstaged_list_element import UserstagedListElement

# TODO update the JSON string below
json = "{}"
# create an instance of UserstagedListElement from a JSON string
userstaged_list_element_instance = UserstagedListElement.from_json(json)
# print the JSON string representation of the object
print UserstagedListElement.to_json()

# convert the object into a dict
userstaged_list_element_dict = userstaged_list_element_instance.to_dict()
# create an instance of UserstagedListElement from a dict
userstaged_list_element_form_dict = userstaged_list_element.from_dict(userstaged_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


