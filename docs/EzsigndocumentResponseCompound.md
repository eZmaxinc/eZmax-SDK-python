# EzsigndocumentResponseCompound

An Ezsigndocument Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_ezsigndocument_steptype** | [**ComputedEEzsigndocumentSteptype**](ComputedEEzsigndocumentSteptype.md) |  | 
**i_ezsigndocument_stepformtotal** | **int** | The total number of steps in the form filling phase | 
**i_ezsigndocument_stepformcurrent** | **int** | The current step in the form filling phase | 
**i_ezsigndocument_stepsignaturetotal** | **int** | The total number of steps in the signature filling phase | 
**i_ezsigndocument_stepsignature_current** | **int** | The current step in the signature phase | 
**a_obj_ezsignfoldersignerassociationstatus** | [**List[CustomEzsignfoldersignerassociationstatusResponse]**](CustomEzsignfoldersignerassociationstatusResponse.md) |  | 
**a_obj_ezsigndocumentdependency** | [**List[EzsigndocumentdependencyResponse]**](EzsigndocumentdependencyResponse.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigndocument_response_compound import EzsigndocumentResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentResponseCompound from a JSON string
ezsigndocument_response_compound_instance = EzsigndocumentResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentResponseCompound.to_json())

# convert the object into a dict
ezsigndocument_response_compound_dict = ezsigndocument_response_compound_instance.to_dict()
# create an instance of EzsigndocumentResponseCompound from a dict
ezsigndocument_response_compound_from_dict = EzsigndocumentResponseCompound.from_dict(ezsigndocument_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


