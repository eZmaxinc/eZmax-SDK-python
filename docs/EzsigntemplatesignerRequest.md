# EzsigntemplatesignerRequest

A Ezsigntemplatesigner Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatesigner_id** | **int** | The unique ID of the Ezsigntemplatesigner | [optional] 
**fki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | 
**s_ezsigntemplatesigner_description** | **str** | The description of the Ezsigntemplatesigner | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesigner_request import EzsigntemplatesignerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignerRequest from a JSON string
ezsigntemplatesigner_request_instance = EzsigntemplatesignerRequest.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignerRequest.to_json())

# convert the object into a dict
ezsigntemplatesigner_request_dict = ezsigntemplatesigner_request_instance.to_dict()
# create an instance of EzsigntemplatesignerRequest from a dict
ezsigntemplatesigner_request_form_dict = ezsigntemplatesigner_request.from_dict(ezsigntemplatesigner_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


