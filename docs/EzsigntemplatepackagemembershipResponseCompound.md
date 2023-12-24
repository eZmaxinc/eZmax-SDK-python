# EzsigntemplatepackagemembershipResponseCompound

A Ezsigntemplatepackagemembership Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatepackagemembership_id** | **int** | The unique ID of the Ezsigntemplatepackagemembership | 
**fki_ezsigntemplatepackage_id** | **int** | The unique ID of the Ezsigntemplatepackage | 
**fki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | 
**i_ezsigntemplatepackagemembership_order** | **int** | The order in which the Ezsigntemplate will be imported when using an Ezsigntemplatepackage. | 
**obj_ezsigntemplate** | [**EzsigntemplateResponseCompound**](EzsigntemplateResponseCompound.md) |  | 
**a_obj_ezsigntemplatepackagesignermembership** | [**List[EzsigntemplatepackagesignermembershipResponseCompound]**](EzsigntemplatepackagesignermembershipResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagemembership_response_compound import EzsigntemplatepackagemembershipResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagemembershipResponseCompound from a JSON string
ezsigntemplatepackagemembership_response_compound_instance = EzsigntemplatepackagemembershipResponseCompound.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatepackagemembershipResponseCompound.to_json()

# convert the object into a dict
ezsigntemplatepackagemembership_response_compound_dict = ezsigntemplatepackagemembership_response_compound_instance.to_dict()
# create an instance of EzsigntemplatepackagemembershipResponseCompound from a dict
ezsigntemplatepackagemembership_response_compound_form_dict = ezsigntemplatepackagemembership_response_compound.from_dict(ezsigntemplatepackagemembership_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


