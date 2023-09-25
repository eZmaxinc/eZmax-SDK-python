# EzsigntemplateformfieldgroupsignerResponse

A Ezsigntemplateformfieldgroupsigner Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplateformfieldgroupsigner_id** | **int** | The unique ID of the Ezsigntemplateformfieldgroupsigner | 
**fki_ezsigntemplatesigner_id** | **int** | The unique ID of the Ezsigntemplatesigner | 

## Example

```python
from eZmaxApi.models.ezsigntemplateformfieldgroupsigner_response import EzsigntemplateformfieldgroupsignerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateformfieldgroupsignerResponse from a JSON string
ezsigntemplateformfieldgroupsigner_response_instance = EzsigntemplateformfieldgroupsignerResponse.from_json(json)
# print the JSON string representation of the object
print EzsigntemplateformfieldgroupsignerResponse.to_json()

# convert the object into a dict
ezsigntemplateformfieldgroupsigner_response_dict = ezsigntemplateformfieldgroupsigner_response_instance.to_dict()
# create an instance of EzsigntemplateformfieldgroupsignerResponse from a dict
ezsigntemplateformfieldgroupsigner_response_form_dict = ezsigntemplateformfieldgroupsigner_response.from_dict(ezsigntemplateformfieldgroupsigner_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


