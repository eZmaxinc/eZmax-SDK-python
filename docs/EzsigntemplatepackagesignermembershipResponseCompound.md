# EzsigntemplatepackagesignermembershipResponseCompound

A Ezsigntemplatepackagesignermembership Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatepackagesignermembership_id** | **int** | The unique ID of the Ezsigntemplatepackagesignermembership | 
**fki_ezsigntemplatepackagemembership_id** | **int** | The unique ID of the Ezsigntemplatepackagemembership | 
**fki_ezsigntemplatepackagesigner_id** | **int** | The unique ID of the Ezsigntemplatepackagesigner | 
**fki_ezsigntemplatesigner_id** | **int** | The unique ID of the Ezsigntemplatesigner | 
**i_ezsigntemplatepackagesignermembership_copy** | **int** | The Copy number in case of multiple copies. | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesignermembership_response_compound import EzsigntemplatepackagesignermembershipResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignermembershipResponseCompound from a JSON string
ezsigntemplatepackagesignermembership_response_compound_instance = EzsigntemplatepackagesignermembershipResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagesignermembershipResponseCompound.to_json())

# convert the object into a dict
ezsigntemplatepackagesignermembership_response_compound_dict = ezsigntemplatepackagesignermembership_response_compound_instance.to_dict()
# create an instance of EzsigntemplatepackagesignermembershipResponseCompound from a dict
ezsigntemplatepackagesignermembership_response_compound_from_dict = EzsigntemplatepackagesignermembershipResponseCompound.from_dict(ezsigntemplatepackagesignermembership_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


