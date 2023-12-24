# EzsigntemplatepackageResponseCompound

A Ezsigntemplatepackage Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatepackage_id** | **int** | The unique ID of the Ezsigntemplatepackage | 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**s_language_name_x** | **str** | The Name of the Language in the language of the requester | 
**s_ezsigntemplatepackage_description** | **str** | The description of the Ezsigntemplatepackage | 
**b_ezsigntemplatepackage_adminonly** | **bool** | Whether the Ezsigntemplatepackage can be accessed by admin users only (eUserType&#x3D;Normal) | 
**b_ezsigntemplatepackage_needvalidation** | **bool** | Whether the Ezsignbulksend was automatically modified and needs a manual validation | 
**b_ezsigntemplatepackage_isactive** | **bool** | Whether the Ezsigntemplatepackage is active or not | 
**s_ezsignfoldertype_name_x** | **str** | The name of the Ezsignfoldertype in the language of the requester | 
**a_obj_ezsigntemplatepackagesigner** | [**List[EzsigntemplatepackagesignerResponseCompound]**](EzsigntemplatepackagesignerResponseCompound.md) |  | 
**a_obj_ezsigntemplatepackagemembership** | [**List[EzsigntemplatepackagemembershipResponseCompound]**](EzsigntemplatepackagemembershipResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackage_response_compound import EzsigntemplatepackageResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackageResponseCompound from a JSON string
ezsigntemplatepackage_response_compound_instance = EzsigntemplatepackageResponseCompound.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatepackageResponseCompound.to_json()

# convert the object into a dict
ezsigntemplatepackage_response_compound_dict = ezsigntemplatepackage_response_compound_instance.to_dict()
# create an instance of EzsigntemplatepackageResponseCompound from a dict
ezsigntemplatepackage_response_compound_form_dict = ezsigntemplatepackage_response_compound.from_dict(ezsigntemplatepackage_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


