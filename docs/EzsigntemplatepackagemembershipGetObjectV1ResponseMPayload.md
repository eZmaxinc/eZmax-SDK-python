# EzsigntemplatepackagemembershipGetObjectV1ResponseMPayload

Payload for GET /1/object/ezsigntemplatepackagemembership/{pkiEzsigntemplatepackagemembershipID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatepackagemembership_id** | **int** | The unique ID of the Ezsigntemplatepackagemembership | 
**fki_ezsigntemplatepackage_id** | **int** | The unique ID of the Ezsigntemplatepackage | 
**fki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | 
**i_ezsigntemplatepackagemembership_order** | **int** | The order in which the Ezsigntemplate will be imported when using an Ezsigntemplatepackage. | 
**obj_ezsigntemplate** | [**EzsigntemplateResponseCompound**](EzsigntemplateResponseCompound.md) |  | 
**a_obj_ezsigntemplatepackagesignermembership** | [**[EzsigntemplatepackagesignermembershipResponseCompound]**](EzsigntemplatepackagesignermembershipResponseCompound.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


