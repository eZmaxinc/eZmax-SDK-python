# EzsignformfieldgroupsignerRequest

A Ezsignformfieldgroupsigner Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignformfieldgroupsigner_id** | **int** | The unique ID of the Ezsignformfieldgroupsigner | [optional] 
**fki_ezsignfoldersignerassociation_id** | **int** | The unique ID of the Ezsignfoldersignerassociation | 

## Example

```python
from eZmaxApi.models.ezsignformfieldgroupsigner_request import EzsignformfieldgroupsignerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignformfieldgroupsignerRequest from a JSON string
ezsignformfieldgroupsigner_request_instance = EzsignformfieldgroupsignerRequest.from_json(json)
# print the JSON string representation of the object
print(EzsignformfieldgroupsignerRequest.to_json())

# convert the object into a dict
ezsignformfieldgroupsigner_request_dict = ezsignformfieldgroupsigner_request_instance.to_dict()
# create an instance of EzsignformfieldgroupsignerRequest from a dict
ezsignformfieldgroupsigner_request_from_dict = EzsignformfieldgroupsignerRequest.from_dict(ezsignformfieldgroupsigner_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


