# EzsigntemplatepackagesignerResponseCompound

A Ezsigntemplatepackagesigner Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatepackagesigner_id** | **int** | The unique ID of the Ezsigntemplatepackagesigner | 
**fki_ezsigntemplatepackage_id** | **int** | The unique ID of the Ezsigntemplatepackage | 
**s_ezsigntemplatepackagesigner_description** | **str** | The description of the Ezsigntemplatepackagesigner | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesigner_response_compound import EzsigntemplatepackagesignerResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignerResponseCompound from a JSON string
ezsigntemplatepackagesigner_response_compound_instance = EzsigntemplatepackagesignerResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagesignerResponseCompound.to_json())

# convert the object into a dict
ezsigntemplatepackagesigner_response_compound_dict = ezsigntemplatepackagesigner_response_compound_instance.to_dict()
# create an instance of EzsigntemplatepackagesignerResponseCompound from a dict
ezsigntemplatepackagesigner_response_compound_form_dict = ezsigntemplatepackagesigner_response_compound.from_dict(ezsigntemplatepackagesigner_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


