# CustomFormDataEzsignformfieldResponse

An Ezsignformfield Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_ezsignformfield_label** | **str** | The Label for the Ezsignformfield | 
**s_ezsignformfield_value** | **str** | The value for the Ezsignformfield  This can only be set if eEzsignformfieldgroupType is Checkbox or Radio | 

## Example

```python
from eZmaxApi.models.custom_form_data_ezsignformfield_response import CustomFormDataEzsignformfieldResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFormDataEzsignformfieldResponse from a JSON string
custom_form_data_ezsignformfield_response_instance = CustomFormDataEzsignformfieldResponse.from_json(json)
# print the JSON string representation of the object
print CustomFormDataEzsignformfieldResponse.to_json()

# convert the object into a dict
custom_form_data_ezsignformfield_response_dict = custom_form_data_ezsignformfield_response_instance.to_dict()
# create an instance of CustomFormDataEzsignformfieldResponse from a dict
custom_form_data_ezsignformfield_response_form_dict = custom_form_data_ezsignformfield_response.from_dict(custom_form_data_ezsignformfield_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


