# EzsigntemplateformfieldgroupsignerResponseCompound

An Ezsigntemplateformfieldgroupsigner Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplateformfieldgroupsigner_id** | **int** | The unique ID of the Ezsigntemplateformfieldgroupsigner | 
**fki_ezsigntemplatesigner_id** | **int** | The unique ID of the Ezsigntemplatesigner | 

## Example

```python
from eZmaxApi.models.ezsigntemplateformfieldgroupsigner_response_compound import EzsigntemplateformfieldgroupsignerResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateformfieldgroupsignerResponseCompound from a JSON string
ezsigntemplateformfieldgroupsigner_response_compound_instance = EzsigntemplateformfieldgroupsignerResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateformfieldgroupsignerResponseCompound.to_json())

# convert the object into a dict
ezsigntemplateformfieldgroupsigner_response_compound_dict = ezsigntemplateformfieldgroupsigner_response_compound_instance.to_dict()
# create an instance of EzsigntemplateformfieldgroupsignerResponseCompound from a dict
ezsigntemplateformfieldgroupsigner_response_compound_form_dict = ezsigntemplateformfieldgroupsigner_response_compound.from_dict(ezsigntemplateformfieldgroupsigner_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


