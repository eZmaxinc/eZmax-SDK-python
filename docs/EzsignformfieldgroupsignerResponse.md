# EzsignformfieldgroupsignerResponse

A Ezsignformfieldgroupsigner Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignformfieldgroupsigner_id** | **int** | The unique ID of the Ezsignformfieldgroupsigner | 
**fki_ezsignfoldersignerassociation_id** | **int** | The unique ID of the Ezsignfoldersignerassociation | 

## Example

```python
from eZmaxApi.models.ezsignformfieldgroupsigner_response import EzsignformfieldgroupsignerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignformfieldgroupsignerResponse from a JSON string
ezsignformfieldgroupsigner_response_instance = EzsignformfieldgroupsignerResponse.from_json(json)
# print the JSON string representation of the object
print EzsignformfieldgroupsignerResponse.to_json()

# convert the object into a dict
ezsignformfieldgroupsigner_response_dict = ezsignformfieldgroupsigner_response_instance.to_dict()
# create an instance of EzsignformfieldgroupsignerResponse from a dict
ezsignformfieldgroupsigner_response_form_dict = ezsignformfieldgroupsigner_response.from_dict(ezsignformfieldgroupsigner_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


