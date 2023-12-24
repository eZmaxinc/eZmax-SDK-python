# EzsigntemplateResponseCompound

A Ezsigntemplate Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | 
**fki_ezsigntemplatedocument_id** | **int** | The unique ID of the Ezsigntemplatedocument | [optional] 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**s_language_name_x** | **str** | The Name of the Language in the language of the requester | 
**s_ezsigntemplate_description** | **str** | The description of the Ezsigntemplate | 
**b_ezsigntemplate_adminonly** | **bool** | Whether the Ezsigntemplate can be accessed by admin users only (eUserType&#x3D;Normal) | 
**s_ezsignfoldertype_name_x** | **str** | The name of the Ezsignfoldertype in the language of the requester | 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | 
**obj_ezsigntemplatedocument** | [**EzsigntemplatedocumentResponse**](EzsigntemplatedocumentResponse.md) |  | [optional] 
**a_obj_ezsigntemplatesigner** | [**List[EzsigntemplatesignerResponseCompound]**](EzsigntemplatesignerResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_response_compound import EzsigntemplateResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateResponseCompound from a JSON string
ezsigntemplate_response_compound_instance = EzsigntemplateResponseCompound.from_json(json)
# print the JSON string representation of the object
print EzsigntemplateResponseCompound.to_json()

# convert the object into a dict
ezsigntemplate_response_compound_dict = ezsigntemplate_response_compound_instance.to_dict()
# create an instance of EzsigntemplateResponseCompound from a dict
ezsigntemplate_response_compound_form_dict = ezsigntemplate_response_compound.from_dict(ezsigntemplate_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


