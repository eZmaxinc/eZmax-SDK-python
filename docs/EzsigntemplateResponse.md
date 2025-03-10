# EzsigntemplateResponse

A Ezsigntemplate Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | 
**fki_ezsigntemplatedocument_id** | **int** | The unique ID of the Ezsigntemplatedocument | [optional] 
**fki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | [optional] 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**fki_ezdoctemplatedocument_id** | **int** | The unique ID of the Ezdoctemplatedocument | [optional] 
**s_language_name_x** | **str** | The Name of the Language in the language of the requester | 
**s_ezsigntemplate_description** | **str** | The description of the Ezsigntemplate | 
**s_ezsigntemplate_externaldescription** | **str** | The external description of the Ezsigntemplate | [optional] 
**t_ezsigntemplate_comment** | **str** | The comment of the Ezsigntemplate | [optional] 
**s_ezsigntemplate_filenamepattern** | **str** | The filename pattern of the Ezsigntemplate | [optional] 
**b_ezsigntemplate_adminonly** | **bool** | Whether the Ezsigntemplate can be accessed by admin users only (eUserType&#x3D;Normal) | 
**s_ezsignfoldertype_name_x** | **str** | The name of the Ezsignfoldertype in the language of the requester | [optional] 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | 
**b_ezsigntemplate_editallowed** | **bool** | Whether the Ezsigntemplate if allowed to edit or not | 
**e_ezsigntemplate_type** | [**FieldEEzsigntemplateType**](FieldEEzsigntemplateType.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplate_response import EzsigntemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateResponse from a JSON string
ezsigntemplate_response_instance = EzsigntemplateResponse.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateResponse.to_json())

# convert the object into a dict
ezsigntemplate_response_dict = ezsigntemplate_response_instance.to_dict()
# create an instance of EzsigntemplateResponse from a dict
ezsigntemplate_response_from_dict = EzsigntemplateResponse.from_dict(ezsigntemplate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


