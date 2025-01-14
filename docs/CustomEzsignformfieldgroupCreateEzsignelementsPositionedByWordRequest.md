# CustomEzsignformfieldgroupCreateEzsignelementsPositionedByWordRequest

An Ezsignformfieldgroup Object in the context of a createEzsignelementsPositionedByWord path

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignformfieldgroup_id** | **int** | The unique ID of the Ezsignformfieldgroup | [optional] 
**fki_ezsigndocument_id** | **int** | The unique ID of the Ezsigndocument | 
**e_ezsignformfieldgroup_type** | [**FieldEEzsignformfieldgroupType**](FieldEEzsignformfieldgroupType.md) |  | 
**e_ezsignformfieldgroup_signerrequirement** | [**FieldEEzsignformfieldgroupSignerrequirement**](FieldEEzsignformfieldgroupSignerrequirement.md) |  | [optional] 
**s_ezsignformfieldgroup_label** | **str** | The Label for the Ezsignformfieldgroup | 
**i_ezsignformfieldgroup_step** | **int** | The step when the Ezsignsigner will be invited to fill the form fields | 
**s_ezsignformfieldgroup_defaultvalue** | **str** | The default value for the Ezsignformfieldgroup  You can use the codes below and they will be replaced at signature time.    | Code | Description | Example | | ------------------------- | ------------ | ------------ | | {sUserFirstname} | The first name of the contact | John | | {sUserLastname} | The last name of the contact | Doe | | {sUserJobtitle} | The job title | Sales Representative | | {sCompany} | Company name | eZmax Solutions Inc. | | {sEmailAddress} | The email address | email@example.com | | {sPhoneE164} | A phone number in E.164 Format | +15149901516 | | {sPhoneE164Cell} | A phone number in E.164 Format | +15149901516 | | [optional] 
**i_ezsignformfieldgroup_filledmin** | **int** | The minimum number of Ezsignformfield that must be filled in the Ezsignformfieldgroup | 
**i_ezsignformfieldgroup_filledmax** | **int** | The maximum number of Ezsignformfield that must be filled in the Ezsignformfieldgroup | 
**b_ezsignformfieldgroup_readonly** | **bool** | Whether the Ezsignformfieldgroup is read only or not. | 
**i_ezsignformfieldgroup_maxlength** | **int** | The maximum length for the value in the Ezsignformfieldgroup  This can only be set if eEzsignformfieldgroupType is **Text** or **Textarea** | [optional] 
**b_ezsignformfieldgroup_encrypted** | **bool** | Whether the Ezsignformfieldgroup is encrypted in the database or not. Encrypted values are not displayed on the Ezsigndocument. This can only be set if eEzsignformfieldgroupType is **Text** or **Textarea** | [optional] 
**s_ezsignformfieldgroup_regexp** | **str** | A regular expression to indicate what values are acceptable for the Ezsignformfieldgroup.  This can only be set if eEzsignformfieldgroupType is **Text** or **Textarea** | [optional] 
**s_ezsignformfieldgroup_textvalidationcustommessage** | **str** | Description of validation rule. Show by signatory. | [optional] 
**t_ezsignformfieldgroup_tooltip** | **str** | A tooltip that will be presented to Ezsignsigner about the Ezsignformfieldgroup | [optional] 
**e_ezsignformfieldgroup_tooltipposition** | [**FieldEEzsignformfieldgroupTooltipposition**](FieldEEzsignformfieldgroupTooltipposition.md) |  | [optional] 
**e_ezsignformfieldgroup_textvalidation** | [**EnumTextvalidation**](EnumTextvalidation.md) |  | [optional] 
**a_obj_ezsignformfieldgroupsigner** | [**List[EzsignformfieldgroupsignerRequestCompound]**](EzsignformfieldgroupsignerRequestCompound.md) |  | 
**a_obj_dropdown_element** | [**List[CustomDropdownElementRequestCompound]**](CustomDropdownElementRequestCompound.md) |  | [optional] 
**a_obj_ezsignformfield** | [**List[EzsignformfieldRequestCompound]**](EzsignformfieldRequestCompound.md) |  | 
**obj_createezsignelementspositionedbyword** | [**CustomCreateEzsignelementsPositionedByWordRequest**](CustomCreateEzsignelementsPositionedByWordRequest.md) |  | 

## Example

```python
from eZmaxApi.models.custom_ezsignformfieldgroup_create_ezsignelements_positioned_by_word_request import CustomEzsignformfieldgroupCreateEzsignelementsPositionedByWordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsignformfieldgroupCreateEzsignelementsPositionedByWordRequest from a JSON string
custom_ezsignformfieldgroup_create_ezsignelements_positioned_by_word_request_instance = CustomEzsignformfieldgroupCreateEzsignelementsPositionedByWordRequest.from_json(json)
# print the JSON string representation of the object
print(CustomEzsignformfieldgroupCreateEzsignelementsPositionedByWordRequest.to_json())

# convert the object into a dict
custom_ezsignformfieldgroup_create_ezsignelements_positioned_by_word_request_dict = custom_ezsignformfieldgroup_create_ezsignelements_positioned_by_word_request_instance.to_dict()
# create an instance of CustomEzsignformfieldgroupCreateEzsignelementsPositionedByWordRequest from a dict
custom_ezsignformfieldgroup_create_ezsignelements_positioned_by_word_request_from_dict = CustomEzsignformfieldgroupCreateEzsignelementsPositionedByWordRequest.from_dict(custom_ezsignformfieldgroup_create_ezsignelements_positioned_by_word_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


