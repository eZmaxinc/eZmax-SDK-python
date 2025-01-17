# EzsigntemplatesignerResponseCompound

A Ezsigntemplatesigner Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatesigner_id** | **int** | The unique ID of the Ezsigntemplatesigner | 
**fki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_usergroup_id** | **int** | The unique ID of the Usergroup | [optional] 
**fki_ezdoctemplatedocument_id** | **int** | The unique ID of the Ezdoctemplatedocument | [optional] 
**b_ezsigntemplatesigner_receivecopy** | **bool** | If this flag is true. The signatory will receive a copy of every signed Ezsigndocument even if it ain&#39;t required to sign the document. | [optional] 
**e_ezsigntemplatesigner_mapping** | [**FieldEEzsigntemplatesignerMapping**](FieldEEzsigntemplatesignerMapping.md) |  | [optional] 
**s_ezsigntemplatesigner_description** | **str** | The description of the Ezsigntemplatesigner | 
**s_user_name** | **str** | The description of the User in the language of the requester | [optional] 
**s_usergroup_name_x** | **str** | The Name of the Usergroup in the language of the requester | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplatesigner_response_compound import EzsigntemplatesignerResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignerResponseCompound from a JSON string
ezsigntemplatesigner_response_compound_instance = EzsigntemplatesignerResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignerResponseCompound.to_json())

# convert the object into a dict
ezsigntemplatesigner_response_compound_dict = ezsigntemplatesigner_response_compound_instance.to_dict()
# create an instance of EzsigntemplatesignerResponseCompound from a dict
ezsigntemplatesigner_response_compound_from_dict = EzsigntemplatesignerResponseCompound.from_dict(ezsigntemplatesigner_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


