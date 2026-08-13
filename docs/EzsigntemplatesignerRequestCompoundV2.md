# EzsigntemplatesignerRequestCompoundV2

A Ezsigntemplatesigner Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatesigner_id** | **int** | The unique ID of the Ezsigntemplatesigner | [optional] 
**fki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**fki_usergroup_id** | **int** | The unique ID of the Usergroup | [optional] 
**fki_ezdoctemplatedocument_id** | **int** | The unique ID of the Ezdoctemplatedocument | [optional] 
**e_ezsigntemplatesigner_role** | [**FieldEEzsigntemplatesignerRole**](FieldEEzsigntemplatesignerRole.md) |  | [optional] 
**e_ezsigntemplatesigner_mapping** | [**FieldEEzsigntemplatesignerMapping**](FieldEEzsigntemplatesignerMapping.md) |  | [optional] 
**s_ezsigntemplatesigner_description** | **str** | The description of the Ezsigntemplatesigner | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesigner_request_compound_v2 import EzsigntemplatesignerRequestCompoundV2

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignerRequestCompoundV2 from a JSON string
ezsigntemplatesigner_request_compound_v2_instance = EzsigntemplatesignerRequestCompoundV2.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignerRequestCompoundV2.to_json())

# convert the object into a dict
ezsigntemplatesigner_request_compound_v2_dict = ezsigntemplatesigner_request_compound_v2_instance.to_dict()
# create an instance of EzsigntemplatesignerRequestCompoundV2 from a dict
ezsigntemplatesigner_request_compound_v2_from_dict = EzsigntemplatesignerRequestCompoundV2.from_dict(ezsigntemplatesigner_request_compound_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


