# EzsigntemplatepackagemembershipResponse

A Ezsigntemplatepackagemembership Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatepackagemembership_id** | **int** | The unique ID of the Ezsigntemplatepackagemembership | 
**fki_ezsigntemplatepackage_id** | **int** | The unique ID of the Ezsigntemplatepackage | 
**fki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | 
**i_ezsigntemplatepackagemembership_order** | **int** | The order in which the Ezsigntemplate will be imported when using an Ezsigntemplatepackage. | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagemembership_response import EzsigntemplatepackagemembershipResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagemembershipResponse from a JSON string
ezsigntemplatepackagemembership_response_instance = EzsigntemplatepackagemembershipResponse.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagemembershipResponse.to_json())

# convert the object into a dict
ezsigntemplatepackagemembership_response_dict = ezsigntemplatepackagemembership_response_instance.to_dict()
# create an instance of EzsigntemplatepackagemembershipResponse from a dict
ezsigntemplatepackagemembership_response_from_dict = EzsigntemplatepackagemembershipResponse.from_dict(ezsigntemplatepackagemembership_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


