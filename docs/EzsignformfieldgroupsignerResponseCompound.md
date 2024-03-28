# EzsignformfieldgroupsignerResponseCompound

An Ezsignformfieldgroupsigner Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignformfieldgroupsigner_id** | **int** | The unique ID of the Ezsignformfieldgroupsigner | 
**fki_ezsignfoldersignerassociation_id** | **int** | The unique ID of the Ezsignfoldersignerassociation | 

## Example

```python
from eZmaxApi.models.ezsignformfieldgroupsigner_response_compound import EzsignformfieldgroupsignerResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignformfieldgroupsignerResponseCompound from a JSON string
ezsignformfieldgroupsigner_response_compound_instance = EzsignformfieldgroupsignerResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignformfieldgroupsignerResponseCompound.to_json())

# convert the object into a dict
ezsignformfieldgroupsigner_response_compound_dict = ezsignformfieldgroupsigner_response_compound_instance.to_dict()
# create an instance of EzsignformfieldgroupsignerResponseCompound from a dict
ezsignformfieldgroupsigner_response_compound_form_dict = ezsignformfieldgroupsigner_response_compound.from_dict(ezsignformfieldgroupsigner_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


