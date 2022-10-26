# EzsignsignatureRequestCompound

An Ezsignsignature Object and children to create a complete structure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezsignfoldersignerassociation_id** | [**FieldPkiEzsignfoldersignerassociationID**](FieldPkiEzsignfoldersignerassociationID.md) |  | 
**i_ezsignpage_pagenumber** | [**FieldIEzsignpagePagenumber**](FieldIEzsignpagePagenumber.md) |  | 
**i_ezsignsignature_x** | [**FieldIEzsignsignatureX**](FieldIEzsignsignatureX.md) |  | 
**i_ezsignsignature_y** | [**FieldIEzsignsignatureY**](FieldIEzsignsignatureY.md) |  | 
**i_ezsignsignature_step** | **int** | The step when the Ezsignsigner will be invited to sign | 
**e_ezsignsignature_type** | [**FieldEEzsignsignatureType**](FieldEEzsignsignatureType.md) |  | 
**fki_ezsigndocument_id** | [**FieldPkiEzsigndocumentID**](FieldPkiEzsigndocumentID.md) |  | 
**pki_ezsignsignature_id** | [**FieldPkiEzsignsignatureID**](FieldPkiEzsignsignatureID.md) |  | [optional] 
**t_ezsignsignature_tooltip** | **str** | A tooltip that will be presented to Ezsignsigner about the Ezsignsignature | [optional] 
**e_ezsignsignature_tooltipposition** | [**FieldEEzsignsignatureTooltipposition**](FieldEEzsignsignatureTooltipposition.md) |  | [optional] 
**e_ezsignsignature_font** | [**FieldEEzsignsignatureFont**](FieldEEzsignsignatureFont.md) |  | [optional] 
**fki_ezsignfoldersignerassociation_id_validation** | [**FieldPkiEzsignfoldersignerassociationID**](FieldPkiEzsignfoldersignerassociationID.md) |  | [optional] 
**b_ezsignsignature_required** | **bool** | Whether the Ezsignsignature is required or not. This field is relevant only with Ezsignsignature with eEzsignsignatureType &#x3D; Attachments. | [optional] 
**e_ezsignsignature_attachmentnamesource** | [**FieldEEzsignsignatureAttachmentnamesource**](FieldEEzsignsignatureAttachmentnamesource.md) |  | [optional] 
**s_ezsignsignature_attachmentdescription** | **str** | The description attached to the attachment name added in Ezsignsignature of eEzsignsignatureType Attachments | [optional] 
**i_ezsignsignature_validationstep** | **int** | The step when the Ezsignsigner will be invited to validate the Ezsignsignature of eEzsignsignatureType Attachments | [optional] 
**b_ezsignsignature_customdate** | **bool** | Whether the Ezsignsignature has a custom date format or not. (Only possible when eEzsignsignatureType is **Name** or **Handwritten**) | [optional] 
**a_obj_ezsignsignaturecustomdate** | [**[EzsignsignaturecustomdateRequestCompound]**](EzsignsignaturecustomdateRequestCompound.md) | An array of custom date blocks that will be filled at the time of signature.  Can only be used if bEzsignsignatureCustomdate is true.  Use an empty array if you don&#39;t want to have a date at all. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


