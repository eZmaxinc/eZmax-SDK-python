# EzsigntemplatepackagesignerResponse

A Ezsigntemplatepackagesigner Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatepackagesigner_id** | **int** | The unique ID of the Ezsigntemplatepackagesigner | 
**fki_ezsigntemplatepackage_id** | **int** | The unique ID of the Ezsigntemplatepackage | 
**s_ezsigntemplatepackagesigner_description** | **str** | The description of the Ezsigntemplatepackagesigner | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesigner_response import EzsigntemplatepackagesignerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignerResponse from a JSON string
ezsigntemplatepackagesigner_response_instance = EzsigntemplatepackagesignerResponse.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatepackagesignerResponse.to_json()

# convert the object into a dict
ezsigntemplatepackagesigner_response_dict = ezsigntemplatepackagesigner_response_instance.to_dict()
# create an instance of EzsigntemplatepackagesignerResponse from a dict
ezsigntemplatepackagesigner_response_form_dict = ezsigntemplatepackagesigner_response.from_dict(ezsigntemplatepackagesigner_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


