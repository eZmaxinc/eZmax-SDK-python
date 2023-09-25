# EzsigntemplatepackagesignermembershipRequestCompound

A Ezsigntemplatepackagesignermembership Object and children

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatepackagesignermembership_id** | **int** | The unique ID of the Ezsigntemplatepackagesignermembership | [optional] 
**fki_ezsigntemplatepackagemembership_id** | **int** | The unique ID of the Ezsigntemplatepackagemembership | 
**fki_ezsigntemplatepackagesigner_id** | **int** | The unique ID of the Ezsigntemplatepackagesigner | 
**fki_ezsigntemplatesigner_id** | **int** | The unique ID of the Ezsigntemplatesigner | 
**i_ezsigntemplatepackagesignermembership_copy** | **int** | The Copy number in case of multiple copies. | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesignermembership_request_compound import EzsigntemplatepackagesignermembershipRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignermembershipRequestCompound from a JSON string
ezsigntemplatepackagesignermembership_request_compound_instance = EzsigntemplatepackagesignermembershipRequestCompound.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatepackagesignermembershipRequestCompound.to_json()

# convert the object into a dict
ezsigntemplatepackagesignermembership_request_compound_dict = ezsigntemplatepackagesignermembership_request_compound_instance.to_dict()
# create an instance of EzsigntemplatepackagesignermembershipRequestCompound from a dict
ezsigntemplatepackagesignermembership_request_compound_form_dict = ezsigntemplatepackagesignermembership_request_compound.from_dict(ezsigntemplatepackagesignermembership_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


