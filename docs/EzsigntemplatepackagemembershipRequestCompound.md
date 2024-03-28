# EzsigntemplatepackagemembershipRequestCompound

A Ezsigntemplatepackagemembership Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatepackagemembership_id** | **int** | The unique ID of the Ezsigntemplatepackagemembership | [optional] 
**fki_ezsigntemplatepackage_id** | **int** | The unique ID of the Ezsigntemplatepackage | 
**fki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagemembership_request_compound import EzsigntemplatepackagemembershipRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagemembershipRequestCompound from a JSON string
ezsigntemplatepackagemembership_request_compound_instance = EzsigntemplatepackagemembershipRequestCompound.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagemembershipRequestCompound.to_json())

# convert the object into a dict
ezsigntemplatepackagemembership_request_compound_dict = ezsigntemplatepackagemembership_request_compound_instance.to_dict()
# create an instance of EzsigntemplatepackagemembershipRequestCompound from a dict
ezsigntemplatepackagemembership_request_compound_form_dict = ezsigntemplatepackagemembership_request_compound.from_dict(ezsigntemplatepackagemembership_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


