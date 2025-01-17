# EzsigntemplatepackagemembershipResponseCompound

A Ezsigntemplatepackagemembership Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
print(EzsigntemplatepackagemembershipResponseCompound.to_json())

# convert the object into a dict
ezsigntemplatepackagemembership_response_compound_dict = ezsigntemplatepackagemembership_response_compound_instance.to_dict()
# create an instance of EzsigntemplatepackagemembershipResponseCompound from a dict
ezsigntemplatepackagemembership_response_compound_from_dict = EzsigntemplatepackagemembershipResponseCompound.from_dict(ezsigntemplatepackagemembership_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


