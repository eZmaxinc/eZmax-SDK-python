# CustomDropdownElementResponse

Generic DropdownElement Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_label** | **str** | The Description of the element | 
**s_value** | **str** | The Value of the element | 

## Example

```python
from eZmaxApi.models.custom_dropdown_element_response import CustomDropdownElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDropdownElementResponse from a JSON string
custom_dropdown_element_response_instance = CustomDropdownElementResponse.from_json(json)
# print the JSON string representation of the object
print(CustomDropdownElementResponse.to_json())

# convert the object into a dict
custom_dropdown_element_response_dict = custom_dropdown_element_response_instance.to_dict()
# create an instance of CustomDropdownElementResponse from a dict
custom_dropdown_element_response_from_dict = CustomDropdownElementResponse.from_dict(custom_dropdown_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


