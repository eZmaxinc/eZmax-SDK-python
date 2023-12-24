# EzsigntemplateformfieldgroupsignerRequest

A Ezsigntemplateformfieldgroupsigner Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplateformfieldgroupsigner_id** | **int** | The unique ID of the Ezsigntemplateformfieldgroupsigner | [optional] 
**fki_ezsigntemplatesigner_id** | **int** | The unique ID of the Ezsigntemplatesigner | 

## Example

```python
from eZmaxApi.models.ezsigntemplateformfieldgroupsigner_request import EzsigntemplateformfieldgroupsignerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateformfieldgroupsignerRequest from a JSON string
ezsigntemplateformfieldgroupsigner_request_instance = EzsigntemplateformfieldgroupsignerRequest.from_json(json)
# print the JSON string representation of the object
print EzsigntemplateformfieldgroupsignerRequest.to_json()

# convert the object into a dict
ezsigntemplateformfieldgroupsigner_request_dict = ezsigntemplateformfieldgroupsigner_request_instance.to_dict()
# create an instance of EzsigntemplateformfieldgroupsignerRequest from a dict
ezsigntemplateformfieldgroupsigner_request_form_dict = ezsigntemplateformfieldgroupsigner_request.from_dict(ezsigntemplateformfieldgroupsigner_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


