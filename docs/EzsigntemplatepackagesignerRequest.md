# EzsigntemplatepackagesignerRequest

A Ezsigntemplatepackagesigner Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatepackagesigner_id** | **int** | The unique ID of the Ezsigntemplatepackagesigner | [optional] 
**fki_ezsigntemplatepackage_id** | **int** | The unique ID of the Ezsigntemplatepackage | 
**s_ezsigntemplatepackagesigner_description** | **str** | The description of the Ezsigntemplatepackagesigner | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagesigner_request import EzsigntemplatepackagesignerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagesignerRequest from a JSON string
ezsigntemplatepackagesigner_request_instance = EzsigntemplatepackagesignerRequest.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatepackagesignerRequest.to_json()

# convert the object into a dict
ezsigntemplatepackagesigner_request_dict = ezsigntemplatepackagesigner_request_instance.to_dict()
# create an instance of EzsigntemplatepackagesignerRequest from a dict
ezsigntemplatepackagesigner_request_form_dict = ezsigntemplatepackagesigner_request.from_dict(ezsigntemplatepackagesigner_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


