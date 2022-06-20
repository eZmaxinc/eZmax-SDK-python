# EzsigntemplatepackagemembershipCreateObjectV1ResponseMPayload

Payload for POST /1/object/ezsigntemplatepackagemembership

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_ezsigntemplatepackagemembership_id** | [**[FieldPkiEzsigntemplatepackagemembershipID]**](FieldPkiEzsigntemplatepackagemembershipID.md) | An array of unique IDs representing the object that were requested to be created.  They are returned in the same order as the array containing the objects to be created that was sent in the request. | 
**b_ezsigntemplatepackage_needvalidation** | **bool** | Whether the Ezsignbulksend was automatically modified and needs a manual validation | 
**b_ezsignbulksend_needvalidation** | **bool** | Whether the Ezsigntemplatepackage was automatically modified and needs a manual validation | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


