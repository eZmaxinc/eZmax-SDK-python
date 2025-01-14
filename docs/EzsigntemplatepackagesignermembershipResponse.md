# EzsigntemplatepackagesignermembershipResponse

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
from eZmaxApi.models.ezsigntemplatepackagesignermembership_response import EzsigntemplatepackagesignermembershipResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignermembershipResponse from a JSON string
ezsigntemplatepackagesignermembership_response_instance = EzsigntemplatepackagesignermembershipResponse.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagesignermembershipResponse.to_json())

# convert the object into a dict
ezsigntemplatepackagesignermembership_response_dict = ezsigntemplatepackagesignermembership_response_instance.to_dict()
# create an instance of EzsigntemplatepackagesignermembershipResponse from a dict
ezsigntemplatepackagesignermembership_response_from_dict = EzsigntemplatepackagesignermembershipResponse.from_dict(ezsigntemplatepackagesignermembership_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


