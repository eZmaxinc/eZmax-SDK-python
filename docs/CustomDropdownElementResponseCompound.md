# CustomDropdownElementResponseCompound

A Generic DropdownElement Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_label** | **str** | The Description of the element | 
**s_value** | **str** | The Value of the element | 

## Example

```python
from eZmaxApi.models.custom_dropdown_element_response_compound import CustomDropdownElementResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDropdownElementResponseCompound from a JSON string
custom_dropdown_element_response_compound_instance = CustomDropdownElementResponseCompound.from_json(json)
# print the JSON string representation of the object
print CustomDropdownElementResponseCompound.to_json()

# convert the object into a dict
custom_dropdown_element_response_compound_dict = custom_dropdown_element_response_compound_instance.to_dict()
# create an instance of CustomDropdownElementResponseCompound from a dict
custom_dropdown_element_response_compound_form_dict = custom_dropdown_element_response_compound.from_dict(custom_dropdown_element_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


