# EzsigntemplateformfieldgroupsignerRequestCompound

An Ezsigntemplateformfieldgroupsigner Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplateformfieldgroupsigner_id** | **int** | The unique ID of the Ezsigntemplateformfieldgroupsigner | [optional] 
**fki_ezsigntemplatesigner_id** | **int** | The unique ID of the Ezsigntemplatesigner | 

## Example

```python
from eZmaxApi.models.ezsigntemplateformfieldgroupsigner_request_compound import EzsigntemplateformfieldgroupsignerRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateformfieldgroupsignerRequestCompound from a JSON string
ezsigntemplateformfieldgroupsigner_request_compound_instance = EzsigntemplateformfieldgroupsignerRequestCompound.from_json(json)
# print the JSON string representation of the object
print EzsigntemplateformfieldgroupsignerRequestCompound.to_json()

# convert the object into a dict
ezsigntemplateformfieldgroupsigner_request_compound_dict = ezsigntemplateformfieldgroupsigner_request_compound_instance.to_dict()
# create an instance of EzsigntemplateformfieldgroupsignerRequestCompound from a dict
ezsigntemplateformfieldgroupsigner_request_compound_form_dict = ezsigntemplateformfieldgroupsigner_request_compound.from_dict(ezsigntemplateformfieldgroupsigner_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


