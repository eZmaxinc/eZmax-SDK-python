# EzsigntemplateformfieldgroupRequestCompound

A Ezsigntemplateformfieldgroup Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplateformfieldgroup_id** | **int** | The unique ID of the Ezsigntemplateformfieldgroup | [optional] 
**fki_ezsigntemplatedocument_id** | **int** | The unique ID of the Ezsigntemplatedocument | 
**e_ezsigntemplateformfieldgroup_type** | [**FieldEEzsigntemplateformfieldgroupType**](FieldEEzsigntemplateformfieldgroupType.md) |  | 
**e_ezsigntemplateformfieldgroup_signerrequirement** | [**FieldEEzsigntemplateformfieldgroupSignerrequirement**](FieldEEzsigntemplateformfieldgroupSignerrequirement.md) |  | [optional] 
**s_ezsigntemplateformfieldgroup_label** | **str** | The Label for the Ezsigntemplateformfieldgroup | 
**i_ezsigntemplateformfieldgroup_step** | **int** | The step when the Ezsigntemplatesigner will be invited to fill the form fields | 
**s_ezsigntemplateformfieldgroup_defaultvalue** | **str** | The default value for the Ezsigntemplateformfieldgroup  You can use the codes below and they will be replaced at signature time.    | Code | Description | Example | | ------------------------- | ------------ | ------------ | | {sUserFirstname} | The first name of the contact | John | | {sUserLastname} | The last name of the contact | Doe | | {sUserJobtitle} | The job title | Sales Representative | | {sEmailAddress} | The email address | email@example.com | | {sPhoneE164} | A phone number in E.164 Format | +15149901516 | | {sPhoneE164Cell} | A phone number in E.164 Format | +15149901516 | | 
**i_ezsigntemplateformfieldgroup_filledmin** | **int** | The minimum number of Ezsigntemplateformfield that must be filled in the Ezsigntemplateformfieldgroup | 
**i_ezsigntemplateformfieldgroup_filledmax** | **int** | The maximum number of Ezsigntemplateformfield that must be filled in the Ezsigntemplateformfieldgroup | 
**b_ezsigntemplateformfieldgroup_readonly** | **bool** | Whether the Ezsigntemplateformfieldgroup is read only or not. | 
**i_ezsigntemplateformfieldgroup_maxlength** | **int** | The maximum length for the value in the Ezsigntemplateformfieldgroup  This can only be set if eEzsigntemplateformfieldgroupType is **Text** or **Textarea** | [optional] 
**b_ezsigntemplateformfieldgroup_encrypted** | **bool** | Whether the Ezsigntemplateformfieldgroup is encrypted in the database or not. Encrypted values are not displayed on the Ezsigndocument. This can only be set if eEzsigntemplateformfieldgroupType is **Text** or **Textarea** | [optional] 
**s_ezsigntemplateformfieldgroup_regexp** | **str** | A regular expression to indicate what values are acceptable for the Ezsigntemplateformfieldgroup.  This can only be set if eEzsigntemplateformfieldgroupType is **Text** or **Textarea** | [optional] 
**s_ezsigntemplateformfieldgroup_textvalidationcustommessage** | **str** | Description of validation rule. Show by signatory. | [optional] 
**e_ezsigntemplateformfieldgroup_textvalidation** | [**EnumTextvalidation**](EnumTextvalidation.md) |  | [optional] 
**t_ezsigntemplateformfieldgroup_tooltip** | **str** | A tooltip that will be presented to Ezsigntemplatesigner about the Ezsigntemplateformfieldgroup | [optional] 
**e_ezsigntemplateformfieldgroup_tooltipposition** | [**FieldEEzsigntemplateformfieldgroupTooltipposition**](FieldEEzsigntemplateformfieldgroupTooltipposition.md) |  | [optional] 
**a_obj_ezsigntemplateformfieldgroupsigner** | [**List[EzsigntemplateformfieldgroupsignerRequestCompound]**](EzsigntemplateformfieldgroupsignerRequestCompound.md) |  | 
**a_obj_dropdown_element** | [**List[CustomDropdownElementRequestCompound]**](CustomDropdownElementRequestCompound.md) |  | [optional] 
**a_obj_ezsigntemplateformfield** | [**List[EzsigntemplateformfieldRequestCompound]**](EzsigntemplateformfieldRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplateformfieldgroup_request_compound import EzsigntemplateformfieldgroupRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateformfieldgroupRequestCompound from a JSON string
ezsigntemplateformfieldgroup_request_compound_instance = EzsigntemplateformfieldgroupRequestCompound.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateformfieldgroupRequestCompound.to_json())

# convert the object into a dict
ezsigntemplateformfieldgroup_request_compound_dict = ezsigntemplateformfieldgroup_request_compound_instance.to_dict()
# create an instance of EzsigntemplateformfieldgroupRequestCompound from a dict
ezsigntemplateformfieldgroup_request_compound_from_dict = EzsigntemplateformfieldgroupRequestCompound.from_dict(ezsigntemplateformfieldgroup_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


