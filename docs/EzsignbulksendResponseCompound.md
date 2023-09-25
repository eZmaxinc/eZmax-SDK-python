# EzsignbulksendResponseCompound

An Ezsignbulksend Object and children to create a complete structure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignbulksend_id** | **int** | The unique ID of the Ezsignbulksend | 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**s_language_name_x** | **str** | The Name of the Language in the language of the requester | 
**e_ezsignfoldertype_privacylevel** | [**FieldEEzsignfoldertypePrivacylevel**](FieldEEzsignfoldertypePrivacylevel.md) |  | 
**s_ezsignfoldertype_name_x** | **str** | The name of the Ezsignfoldertype in the language of the requester | 
**s_ezsignbulksend_description** | **str** | The description of the Ezsignbulksend | 
**t_ezsignbulksend_note** | **str** | Note about the Ezsignbulksend | 
**b_ezsignbulksend_needvalidation** | **bool** | Whether the Ezsigntemplatepackage was automatically modified and needs a manual validation | 
**b_ezsignbulksend_isactive** | **bool** | Whether the Ezsignbulksend is active or not | 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | 
**a_obj_ezsignbulksenddocumentmapping** | [**List[EzsignbulksenddocumentmappingResponseCompound]**](EzsignbulksenddocumentmappingResponseCompound.md) |  | 
**a_obj_ezsignbulksendsignermapping** | [**List[EzsignbulksendsignermappingResponse]**](EzsignbulksendsignermappingResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksend_response_compound import EzsignbulksendResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendResponseCompound from a JSON string
ezsignbulksend_response_compound_instance = EzsignbulksendResponseCompound.from_json(json)
# print the JSON string representation of the object
print EzsignbulksendResponseCompound.to_json()

# convert the object into a dict
ezsignbulksend_response_compound_dict = ezsignbulksend_response_compound_instance.to_dict()
# create an instance of EzsignbulksendResponseCompound from a dict
ezsignbulksend_response_compound_form_dict = ezsignbulksend_response_compound.from_dict(ezsignbulksend_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


