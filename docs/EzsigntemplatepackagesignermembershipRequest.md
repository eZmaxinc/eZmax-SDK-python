# EzsigntemplatepackagesignermembershipRequest

A Ezsigntemplatepackagesignermembership Object

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
from eZmaxApi.models.ezsigntemplatepackagesignermembership_request import EzsigntemplatepackagesignermembershipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignermembershipRequest from a JSON string
ezsigntemplatepackagesignermembership_request_instance = EzsigntemplatepackagesignermembershipRequest.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatepackagesignermembershipRequest.to_json()

# convert the object into a dict
ezsigntemplatepackagesignermembership_request_dict = ezsigntemplatepackagesignermembership_request_instance.to_dict()
# create an instance of EzsigntemplatepackagesignermembershipRequest from a dict
ezsigntemplatepackagesignermembership_request_form_dict = ezsigntemplatepackagesignermembership_request.from_dict(ezsigntemplatepackagesignermembership_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


