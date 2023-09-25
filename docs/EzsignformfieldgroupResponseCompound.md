# EzsignformfieldgroupResponseCompound

An Ezsignformfieldgroup Object and children to create a complete structure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignformfieldgroup_id** | **int** | The unique ID of the Ezsignformfieldgroup | 
**fki_ezsigndocument_id** | **int** | The unique ID of the Ezsigndocument | 
**e_ezsignformfieldgroup_type** | [**FieldEEzsignformfieldgroupType**](FieldEEzsignformfieldgroupType.md) |  | 
**e_ezsignformfieldgroup_signerrequirement** | [**FieldEEzsignformfieldgroupSignerrequirement**](FieldEEzsignformfieldgroupSignerrequirement.md) |  | 
**s_ezsignformfieldgroup_label** | **str** | The Label for the Ezsignformfieldgroup | 
**i_ezsignformfieldgroup_step** | **int** | The step when the Ezsignsigner will be invited to fill the form fields | 
**s_ezsignformfieldgroup_defaultvalue** | **str** | The default value for the Ezsignformfieldgroup | [optional] 
**i_ezsignformfieldgroup_filledmin** | **int** | The minimum number of Ezsignformfield that must be filled in the Ezsignformfieldgroup | 
**i_ezsignformfieldgroup_filledmax** | **int** | The maximum number of Ezsignformfield that must be filled in the Ezsignformfieldgroup | 
**b_ezsignformfieldgroup_readonly** | **bool** | Whether the Ezsignformfieldgroup is read only or not. | 
**i_ezsignformfieldgroup_maxlength** | **int** | The maximum length for the value in the Ezsignformfieldgroup  This can only be set if eEzsignformfieldgroupType is **Text** or **Textarea** | [optional] 
**b_ezsignformfieldgroup_encrypted** | **bool** | Whether the Ezsignformfieldgroup is encrypted in the database or not. Encrypted values are not displayed on the Ezsigndocument. This can only be set if eEzsignformfieldgroupType is **Text** or **Textarea** | [optional] 
**e_ezsignformfieldgroup_textvalidation** | [**EnumTextvalidation**](EnumTextvalidation.md) |  | [optional] 
**s_ezsignformfieldgroup_regexp** | **str** | A regular expression to indicate what values are acceptable for the Ezsignformfieldgroup.  This can only be set if eEzsignformfieldgroupType is **Text** or **Textarea** | [optional] 
**t_ezsignformfieldgroup_tooltip** | **str** | A tooltip that will be presented to Ezsignsigner about the Ezsignformfieldgroup | [optional] 
**e_ezsignformfieldgroup_tooltipposition** | [**FieldEEzsignformfieldgroupTooltipposition**](FieldEEzsignformfieldgroupTooltipposition.md) |  | [optional] 
**a_obj_ezsignformfield** | [**List[EzsignformfieldResponseCompound]**](EzsignformfieldResponseCompound.md) |  | 
**a_obj_dropdown_element** | [**List[CustomDropdownElementResponseCompound]**](CustomDropdownElementResponseCompound.md) |  | [optional] 
**a_obj_ezsignformfieldgroupsigner** | [**List[EzsignformfieldgroupsignerResponseCompound]**](EzsignformfieldgroupsignerResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignformfieldgroup_response_compound import EzsignformfieldgroupResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignformfieldgroupResponseCompound from a JSON string
ezsignformfieldgroup_response_compound_instance = EzsignformfieldgroupResponseCompound.from_json(json)
# print the JSON string representation of the object
print EzsignformfieldgroupResponseCompound.to_json()

# convert the object into a dict
ezsignformfieldgroup_response_compound_dict = ezsignformfieldgroup_response_compound_instance.to_dict()
# create an instance of EzsignformfieldgroupResponseCompound from a dict
ezsignformfieldgroup_response_compound_form_dict = ezsignformfieldgroup_response_compound.from_dict(ezsignformfieldgroup_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


