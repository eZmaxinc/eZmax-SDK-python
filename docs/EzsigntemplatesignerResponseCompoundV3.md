# EzsigntemplatesignerResponseCompoundV3

A Ezsigntemplatesigner Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatesigner_id** | **int** | The unique ID of the Ezsigntemplatesigner | 
**fki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_usergroup_id** | **int** | The unique ID of the Usergroup | [optional] 
**fki_ezdoctemplatedocument_id** | **int** | The unique ID of the Ezdoctemplatedocument | [optional] 
**e_ezsigntemplatesigner_role** | [**FieldEEzsigntemplatesignerRole**](FieldEEzsigntemplatesignerRole.md) |  | [optional] 
**e_ezsigntemplatesigner_mapping** | [**FieldEEzsigntemplatesignerMapping**](FieldEEzsigntemplatesignerMapping.md) |  | [optional] 
**s_ezsigntemplatesigner_description** | **str** | The description of the Ezsigntemplatesigner | 
**s_user_name** | **str** | The description of the User in the language of the requester | [optional] 
**s_usergroup_name_x** | **str** | The Name of the Usergroup in the language of the requester | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplatesigner_response_compound_v3 import EzsigntemplatesignerResponseCompoundV3

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignerResponseCompoundV3 from a JSON string
ezsigntemplatesigner_response_compound_v3_instance = EzsigntemplatesignerResponseCompoundV3.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignerResponseCompoundV3.to_json())

# convert the object into a dict
ezsigntemplatesigner_response_compound_v3_dict = ezsigntemplatesigner_response_compound_v3_instance.to_dict()
# create an instance of EzsigntemplatesignerResponseCompoundV3 from a dict
ezsigntemplatesigner_response_compound_v3_from_dict = EzsigntemplatesignerResponseCompoundV3.from_dict(ezsigntemplatesigner_response_compound_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


