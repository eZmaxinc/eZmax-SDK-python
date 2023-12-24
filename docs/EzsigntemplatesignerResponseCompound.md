# EzsigntemplatesignerResponseCompound

A Ezsigntemplatesigner Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatesigner_id** | **int** | The unique ID of the Ezsigntemplatesigner | 
**fki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | 
**s_ezsigntemplatesigner_description** | **str** | The description of the Ezsigntemplatesigner | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesigner_response_compound import EzsigntemplatesignerResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignerResponseCompound from a JSON string
ezsigntemplatesigner_response_compound_instance = EzsigntemplatesignerResponseCompound.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatesignerResponseCompound.to_json()

# convert the object into a dict
ezsigntemplatesigner_response_compound_dict = ezsigntemplatesigner_response_compound_instance.to_dict()
# create an instance of EzsigntemplatesignerResponseCompound from a dict
ezsigntemplatesigner_response_compound_form_dict = ezsigntemplatesigner_response_compound.from_dict(ezsigntemplatesigner_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


