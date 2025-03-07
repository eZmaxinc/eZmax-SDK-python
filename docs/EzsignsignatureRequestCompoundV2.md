# EzsignsignatureRequestCompoundV2

An Ezsignsignature Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignsignature_id** | **int** | The unique ID of the Ezsignsignature | [optional] 
**fki_ezsignfoldersignerassociation_id** | **int** | The unique ID of the Ezsignfoldersignerassociation | 
**fki_paymentgateway_id** | **int** | The unique ID of the Paymentgateway | [optional] 
**i_ezsignpage_pagenumber** | **int** | The page number in the Ezsigndocument | 
**i_ezsignsignature_x** | **int** | The X coordinate (Horizontal) where to put the Ezsignsignature on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsignsignature 2 inches from the left border of the page, you would use \&quot;200\&quot; for the X coordinate. | 
**i_ezsignsignature_y** | **int** | The Y coordinate (Vertical) where to put the Ezsignsignature on the page.  Coordinate is calculated at 100dpi (dot per inch). So for example, if you want to put the Ezsignsignature 3 inches from the top border of the page, you would use \&quot;300\&quot; for the Y coordinate. | 
**i_ezsignsignature_width** | **int** | The width of the Ezsignsignature.  Size is calculated at 100dpi (dot per inch). So for example, if you want the Ezsignsignature to have a width of 2 inches, you would use \&quot;200\&quot; for the iEzsignsignatureWidth. | [optional] 
**i_ezsignsignature_height** | **int** | The height of the Ezsignsignature.  Size is calculated at 100dpi (dot per inch). So for example, if you want the Ezsignsignature to have an height of 2 inches, you would use \&quot;200\&quot; for the iEzsignsignatureHeight. | [optional] 
**i_ezsignsignature_step** | **int** | The step when the Ezsignsigner will be invited to sign | 
**e_ezsignsignature_type** | [**FieldEEzsignsignatureType**](FieldEEzsignsignatureType.md) |  | 
**fki_ezsigndocument_id** | **int** | The unique ID of the Ezsigndocument | 
**t_ezsignsignature_tooltip** | **str** | A tooltip that will be presented to Ezsignsigner about the Ezsignsignature | [optional] 
**e_ezsignsignature_tooltipposition** | [**FieldEEzsignsignatureTooltipposition**](FieldEEzsignsignatureTooltipposition.md) |  | [optional] 
**e_ezsignsignature_font** | [**FieldEEzsignsignatureFont**](FieldEEzsignsignatureFont.md) |  | [optional] 
**fki_ezsignfoldersignerassociation_id_validation** | **int** | The unique ID of the Ezsignfoldersignerassociation | [optional] 
**b_ezsignsignature_handwritten** | **bool** | Whether the Ezsignsignature must be handwritten or not when eEzsignsignatureType &#x3D; Signature. | [optional] 
**b_ezsignsignature_reason** | **bool** | Whether the Ezsignsignature must include a reason or not when eEzsignsignatureType &#x3D; Signature. | [optional] 
**b_ezsignsignature_required** | **bool** | Whether the Ezsignsignature is required or not. This field is relevant only with Ezsignsignature with eEzsignsignatureType &#x3D; Attachments, Text or Textarea. | [optional] 
**e_ezsignsignature_attachmentnamesource** | [**FieldEEzsignsignatureAttachmentnamesource**](FieldEEzsignsignatureAttachmentnamesource.md) |  | [optional] 
**s_ezsignsignature_attachmentdescription** | **str** | The description attached to the attachment name added in Ezsignsignature of eEzsignsignatureType Attachments | [optional] 
**e_ezsignsignature_consultationtrigger** | [**FieldEEzsignsignatureConsultationtrigger**](FieldEEzsignsignatureConsultationtrigger.md) |  | [optional] 
**i_ezsignsignature_validationstep** | **int** | The step when the Ezsignsigner will be invited to validate the Ezsignsignature of eEzsignsignatureType Attachments | [optional] 
**i_ezsignsignature_maxlength** | **int** | The maximum length for the value in the Ezsignsignature  This can only be set if eEzsignsignatureType is **FieldText** or **FieldTextarea** | [optional] 
**s_ezsignsignature_defaultvalue** | **str** | The default value for the Ezsignsignature  You can use the codes below and they will be replaced at signature time.    | Code | Description | Example | | ------------------------- | ------------ | ------------ | | {sUserFirstname} | The first name of the contact | John | | {sUserLastname} | The last name of the contact | Doe | | {sUserJobtitle} | The job title | Sales Representative | | {sCompany} | Company name | eZmax Solutions Inc. | | {sEmailAddress} | The email address | email@example.com | | {sPhoneE164} | A phone number in E.164 Format | +15149901516 | | {sPhoneE164Cell} | A phone number in E.164 Format | +15149901516 | | [optional] 
**e_ezsignsignature_textvalidation** | [**EnumTextvalidation**](EnumTextvalidation.md) |  | [optional] 
**s_ezsignsignature_textvalidationcustommessage** | **str** | Description of validation rule. Show by signatory. | [optional] 
**s_ezsignsignature_regexp** | **str** | A regular expression to indicate what values are acceptable for the Ezsignsignature.  This can only be set if eEzsignsignatureType is **FieldText** or **FieldTextarea** and eEzsignsignatureTextvalidation is **Custom** | [optional] 
**e_ezsignsignature_dependencyrequirement** | [**FieldEEzsignsignatureDependencyrequirement**](FieldEEzsignsignatureDependencyrequirement.md) |  | [optional] 
**b_ezsignsignature_customdate** | **bool** | Whether the Ezsignsignature has a custom date format or not. (Only possible when eEzsignsignatureType is **Name** or **Handwritten**) | [optional] 
**a_obj_ezsignsignaturecustomdate** | [**List[EzsignsignaturecustomdateRequestCompoundV2]**](EzsignsignaturecustomdateRequestCompoundV2.md) | An array of custom date blocks that will be filled at the time of signature.  Can only be used if bEzsignsignatureCustomdate is true.  Use an empty array if you don&#39;t want to have a date at all. | [optional] 
**a_obj_ezsignelementdependency** | [**List[EzsignelementdependencyRequestCompound]**](EzsignelementdependencyRequestCompound.md) |  | [optional] 
**a_obj_ezsignsignaturepaymentdetail** | [**List[EzsignsignaturepaymentdetailRequestCompound]**](EzsignsignaturepaymentdetailRequestCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignsignature_request_compound_v2 import EzsignsignatureRequestCompoundV2

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureRequestCompoundV2 from a JSON string
ezsignsignature_request_compound_v2_instance = EzsignsignatureRequestCompoundV2.from_json(json)
# print the JSON string representation of the object
print(EzsignsignatureRequestCompoundV2.to_json())

# convert the object into a dict
ezsignsignature_request_compound_v2_dict = ezsignsignature_request_compound_v2_instance.to_dict()
# create an instance of EzsignsignatureRequestCompoundV2 from a dict
ezsignsignature_request_compound_v2_from_dict = EzsignsignatureRequestCompoundV2.from_dict(ezsignsignature_request_compound_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


