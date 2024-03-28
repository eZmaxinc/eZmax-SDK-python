# EzsigntemplateglobalsignerResponseCompound

A Ezsigntemplateglobalsigner Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplateglobalsigner_id** | **int** | The unique ID of the Ezsigntemplateglobalsigner | 
**fki_ezsigntemplateglobal_id** | **int** | The unique ID of the Ezsigntemplateglobal | 
**s_ezsigntemplateglobalsigner_description** | **str** | The description of the Ezsigntemplateglobalsigner | 

## Example

```python
from eZmaxApi.models.ezsigntemplateglobalsigner_response_compound import EzsigntemplateglobalsignerResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateglobalsignerResponseCompound from a JSON string
ezsigntemplateglobalsigner_response_compound_instance = EzsigntemplateglobalsignerResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateglobalsignerResponseCompound.to_json())

# convert the object into a dict
ezsigntemplateglobalsigner_response_compound_dict = ezsigntemplateglobalsigner_response_compound_instance.to_dict()
# create an instance of EzsigntemplateglobalsignerResponseCompound from a dict
ezsigntemplateglobalsigner_response_compound_form_dict = ezsigntemplateglobalsigner_response_compound.from_dict(ezsigntemplateglobalsigner_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


