# CustomDropdownElementRequest

Generic DropdownElement Request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_label** | **str** | The Description of the element | 
**s_value** | **str** | The Value of the element | 

## Example

```python
from eZmaxApi.models.custom_dropdown_element_request import CustomDropdownElementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDropdownElementRequest from a JSON string
custom_dropdown_element_request_instance = CustomDropdownElementRequest.from_json(json)
# print the JSON string representation of the object
print CustomDropdownElementRequest.to_json()

# convert the object into a dict
custom_dropdown_element_request_dict = custom_dropdown_element_request_instance.to_dict()
# create an instance of CustomDropdownElementRequest from a dict
custom_dropdown_element_request_form_dict = custom_dropdown_element_request.from_dict(custom_dropdown_element_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


