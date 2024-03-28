# EzsigntemplatepackagesignerRequestCompound

A Ezsigntemplatepackagesigner Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatepackagesigner_id** | **int** | The unique ID of the Ezsigntemplatepackagesigner | [optional] 
**fki_ezsigntemplatepackage_id** | **int** | The unique ID of the Ezsigntemplatepackage | 
**s_ezsigntemplatepackagesigner_description** | **str** | The description of the Ezsigntemplatepackagesigner | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesigner_request_compound import EzsigntemplatepackagesignerRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignerRequestCompound from a JSON string
ezsigntemplatepackagesigner_request_compound_instance = EzsigntemplatepackagesignerRequestCompound.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagesignerRequestCompound.to_json())

# convert the object into a dict
ezsigntemplatepackagesigner_request_compound_dict = ezsigntemplatepackagesigner_request_compound_instance.to_dict()
# create an instance of EzsigntemplatepackagesignerRequestCompound from a dict
ezsigntemplatepackagesigner_request_compound_form_dict = ezsigntemplatepackagesigner_request_compound.from_dict(ezsigntemplatepackagesigner_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


