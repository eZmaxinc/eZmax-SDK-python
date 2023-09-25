# EzsignformfieldgroupsignerRequestCompound

An Ezsignformfieldgroupsigner Object and children to create a complete structure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignformfieldgroupsigner_id** | **int** | The unique ID of the Ezsignformfieldgroupsigner | [optional] 
**fki_ezsignfoldersignerassociation_id** | **int** | The unique ID of the Ezsignfoldersignerassociation | 

## Example

```python
from eZmaxApi.models.ezsignformfieldgroupsigner_request_compound import EzsignformfieldgroupsignerRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignformfieldgroupsignerRequestCompound from a JSON string
ezsignformfieldgroupsigner_request_compound_instance = EzsignformfieldgroupsignerRequestCompound.from_json(json)
# print the JSON string representation of the object
print EzsignformfieldgroupsignerRequestCompound.to_json()

# convert the object into a dict
ezsignformfieldgroupsigner_request_compound_dict = ezsignformfieldgroupsigner_request_compound_instance.to_dict()
# create an instance of EzsignformfieldgroupsignerRequestCompound from a dict
ezsignformfieldgroupsigner_request_compound_form_dict = ezsignformfieldgroupsigner_request_compound.from_dict(ezsignformfieldgroupsigner_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


