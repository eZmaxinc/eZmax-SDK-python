# CustomEzsignformfieldRequest

A Custom Ezsignformfield Object to fill an Ezsignform using submitForm

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignformfield_id** | **int** | The unique ID of the Ezsignformfield | [optional] 
**s_ezsignformfield_label** | **str** | The Label for the Ezsignformfield | [optional] 
**b_ezsignformfield_selected** | **bool** | Whether the Ezsignformfield is selected or not by default.  This can only be set if eEzsignformfieldgroupType is **Checkbox** or **Radio** | [optional] 
**s_ezsignformfield_enteredvalue** | **str** | This is the value enterred for the Ezsignformfield  This can only be set if eEzsignformfieldgroupType is **Dropdown**, **Text** or **Textarea** | [optional] 

## Example

```python
from eZmaxApi.models.custom_ezsignformfield_request import CustomEzsignformfieldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsignformfieldRequest from a JSON string
custom_ezsignformfield_request_instance = CustomEzsignformfieldRequest.from_json(json)
# print the JSON string representation of the object
print(CustomEzsignformfieldRequest.to_json())

# convert the object into a dict
custom_ezsignformfield_request_dict = custom_ezsignformfield_request_instance.to_dict()
# create an instance of CustomEzsignformfieldRequest from a dict
custom_ezsignformfield_request_form_dict = custom_ezsignformfield_request.from_dict(custom_ezsignformfield_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


