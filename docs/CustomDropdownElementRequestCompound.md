# CustomDropdownElementRequestCompound

A Generic DropdownElement Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_label** | **str** | The Description of the element | 
**s_value** | **str** | The Value of the element | 

## Example

```python
from eZmaxApi.models.custom_dropdown_element_request_compound import CustomDropdownElementRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDropdownElementRequestCompound from a JSON string
custom_dropdown_element_request_compound_instance = CustomDropdownElementRequestCompound.from_json(json)
# print the JSON string representation of the object
print(CustomDropdownElementRequestCompound.to_json())

# convert the object into a dict
custom_dropdown_element_request_compound_dict = custom_dropdown_element_request_compound_instance.to_dict()
# create an instance of CustomDropdownElementRequestCompound from a dict
custom_dropdown_element_request_compound_from_dict = CustomDropdownElementRequestCompound.from_dict(custom_dropdown_element_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


