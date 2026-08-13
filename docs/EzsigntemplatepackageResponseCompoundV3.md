# EzsigntemplatepackageResponseCompoundV3

A Ezsigntemplatepackage Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatepackage_id** | **int** | The unique ID of the Ezsigntemplatepackage | 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | 
**fki_ezdoctemplatedocument_id** | **int** | The unique ID of the Ezdoctemplatedocument | [optional] 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**s_ezdoctemplatedocument_name_x** | **str** | The name of the Ezdoctemplatedocument in the language of the requester | [optional] 
**s_language_name_x** | **str** | The Name of the Language in the language of the requester | 
**s_ezsigntemplatepackage_description** | **str** | The description of the Ezsigntemplatepackage | 
**b_ezsigntemplatepackage_adminonly** | **bool** | Whether the Ezsigntemplatepackage can be accessed by admin users only (eUserType&#x3D;Normal) | 
**b_ezsigntemplatepackage_needvalidation** | **bool** | Whether the Ezsignbulksend was automatically modified and needs a manual validation | 
**b_ezsigntemplatepackage_isactive** | **bool** | Whether the Ezsigntemplatepackage is active or not | 
**s_ezsignfoldertype_name_x** | **str** | The name of the Ezsignfoldertype in the language of the requester | 
**b_ezsigntemplatepackage_editallowed** | **bool** | Whether the Ezsigntemplatepackage if allowed to edit or not | 
**a_obj_ezsigntemplatepackagesigner** | [**List[EzsigntemplatepackagesignerResponseCompoundV3]**](EzsigntemplatepackagesignerResponseCompoundV3.md) |  | 
**a_obj_ezsigntemplatepackagemembership** | [**List[EzsigntemplatepackagemembershipResponseCompoundV3]**](EzsigntemplatepackagemembershipResponseCompoundV3.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackage_response_compound_v3 import EzsigntemplatepackageResponseCompoundV3

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackageResponseCompoundV3 from a JSON string
ezsigntemplatepackage_response_compound_v3_instance = EzsigntemplatepackageResponseCompoundV3.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackageResponseCompoundV3.to_json())

# convert the object into a dict
ezsigntemplatepackage_response_compound_v3_dict = ezsigntemplatepackage_response_compound_v3_instance.to_dict()
# create an instance of EzsigntemplatepackageResponseCompoundV3 from a dict
ezsigntemplatepackage_response_compound_v3_from_dict = EzsigntemplatepackageResponseCompoundV3.from_dict(ezsigntemplatepackage_response_compound_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


