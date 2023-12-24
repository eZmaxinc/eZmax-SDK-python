# EzsigntemplatesignerRequestCompound

A Ezsigntemplatesigner Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatesigner_id** | **int** | The unique ID of the Ezsigntemplatesigner | [optional] 
**fki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | 
**s_ezsigntemplatesigner_description** | **str** | The description of the Ezsigntemplatesigner | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesigner_request_compound import EzsigntemplatesignerRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignerRequestCompound from a JSON string
ezsigntemplatesigner_request_compound_instance = EzsigntemplatesignerRequestCompound.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatesignerRequestCompound.to_json()

# convert the object into a dict
ezsigntemplatesigner_request_compound_dict = ezsigntemplatesigner_request_compound_instance.to_dict()
# create an instance of EzsigntemplatesignerRequestCompound from a dict
ezsigntemplatesigner_request_compound_form_dict = ezsigntemplatesigner_request_compound.from_dict(ezsigntemplatesigner_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


