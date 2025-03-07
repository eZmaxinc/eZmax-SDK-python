# CustomPrefillEzsignformValueRequest

A Custom PrefillEzsignformValue Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_ezsignformfieldgroup_label** | **str** | The Label for the Ezsignformfieldgroup | 
**s_ezsignformfield_label** | **str** | The Label for the Ezsignformfield | [optional] 
**s_ezsignformfield_enteredvalue** | **str** | This is the value enterred for the Ezsignformfield  This can only be set if eEzsignformfieldgroupType is **Dropdown**, **Text** or **Textarea** | [optional] 
**b_ezsignformfield_selected** | **bool** | Whether the Ezsignformfield is selected or not by default.  This can only be set if eEzsignformfieldgroupType is **Checkbox** or **Radio** | [optional] 

## Example

```python
from eZmaxApi.models.custom_prefill_ezsignform_value_request import CustomPrefillEzsignformValueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomPrefillEzsignformValueRequest from a JSON string
custom_prefill_ezsignform_value_request_instance = CustomPrefillEzsignformValueRequest.from_json(json)
# print the JSON string representation of the object
print(CustomPrefillEzsignformValueRequest.to_json())

# convert the object into a dict
custom_prefill_ezsignform_value_request_dict = custom_prefill_ezsignform_value_request_instance.to_dict()
# create an instance of CustomPrefillEzsignformValueRequest from a dict
custom_prefill_ezsignform_value_request_from_dict = CustomPrefillEzsignformValueRequest.from_dict(custom_prefill_ezsignform_value_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


