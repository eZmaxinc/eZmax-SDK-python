# EzsigntemplateGetObjectV1ResponseMPayload

Payload for GET /1/object/ezsigntemplate/{pkiEzsigntemplateID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplate_id** | [**FieldPkiEzsigntemplateID**](FieldPkiEzsigntemplateID.md) |  | 
**fki_ezsignfoldertype_id** | [**FieldPkiEzsignfoldertypeID**](FieldPkiEzsignfoldertypeID.md) |  | 
**fki_language_id** | [**FieldPkiLanguageID**](FieldPkiLanguageID.md) |  | 
**s_language_name_x** | **str** | The Name of the Language in the language of the requester | 
**s_ezsigntemplate_description** | **str** | The description of the Ezsigntemplate | 
**b_ezsigntemplate_adminonly** | **bool** | Whether the Ezsigntemplate can be accessed by admin users only (eUserType&#x3D;Normal) | 
**s_ezsignfoldertype_name_x** | **str** | The name of the Ezsignfoldertype in the language of the requester | 
**a_obj_ezsigntemplatesigner** | [**[EzsigntemplatesignerResponseCompound]**](EzsigntemplatesignerResponseCompound.md) |  | 
**fki_ezsigntemplatedocument_id** | [**FieldPkiEzsigntemplatedocumentID**](FieldPkiEzsigntemplatedocumentID.md) |  | [optional] 
**obj_ezsigntemplatedocument** | [**EzsigntemplatedocumentResponse**](EzsigntemplatedocumentResponse.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


