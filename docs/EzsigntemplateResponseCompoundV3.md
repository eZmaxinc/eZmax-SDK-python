# EzsigntemplateResponseCompoundV3

A Ezsigntemplate Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | 
**fki_ezsigntemplatedocument_id** | **int** | The unique ID of the Ezsigntemplatedocument | [optional] 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | [optional] 
**obj_ezsignfoldertype** | [**CustomEzsignfoldertypeTemplateResponse**](CustomEzsignfoldertypeTemplateResponse.md) |  | [optional] 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**fki_ezdoctemplatedocument_id** | **int** | The unique ID of the Ezdoctemplatedocument | [optional] 
**s_ezdoctemplatedocument_name_x** | **str** | The name of the Ezdoctemplatedocument in the language of the requester | [optional] 
**s_language_name_x** | **str** | The Name of the Language in the language of the requester | 
**s_ezsigntemplate_description** | **str** | The description of the Ezsigntemplate | 
**s_ezsigntemplate_externaldescription** | **str** | The external description of the Ezsigntemplate | [optional] 
**t_ezsigntemplate_comment** | **str** | The comment of the Ezsigntemplate | [optional] 
**e_ezsigntemplate_recognition** | [**FieldEEzsigntemplateRecognition**](FieldEEzsigntemplateRecognition.md) |  | [optional] [default to FieldEEzsigntemplateRecognition.NO]
**s_ezsigntemplate_filenameregexp** | **str** | The filename regexp of the Ezsigntemplate. | [optional] 
**b_ezsigntemplate_adminonly** | **bool** | Whether the Ezsigntemplate can be accessed by admin users only (eUserType&#x3D;Normal) | 
**s_ezsignfoldertype_name_x** | **str** | The name of the Ezsignfoldertype in the language of the requester | [optional] 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | 
**b_ezsigntemplate_editallowed** | **bool** | Whether the Ezsigntemplate if allowed to edit or not | 
**e_ezsigntemplate_type** | [**FieldEEzsigntemplateType**](FieldEEzsigntemplateType.md) |  | [optional] 
**obj_ezsigntemplatedocument** | [**EzsigntemplatedocumentResponse**](EzsigntemplatedocumentResponse.md) |  | [optional] 
**a_obj_ezsigntemplatesigner** | [**List[EzsigntemplatesignerResponseCompound]**](EzsigntemplatesignerResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_response_compound_v3 import EzsigntemplateResponseCompoundV3

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateResponseCompoundV3 from a JSON string
ezsigntemplate_response_compound_v3_instance = EzsigntemplateResponseCompoundV3.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateResponseCompoundV3.to_json())

# convert the object into a dict
ezsigntemplate_response_compound_v3_dict = ezsigntemplate_response_compound_v3_instance.to_dict()
# create an instance of EzsigntemplateResponseCompoundV3 from a dict
ezsigntemplate_response_compound_v3_from_dict = EzsigntemplateResponseCompoundV3.from_dict(ezsigntemplate_response_compound_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


