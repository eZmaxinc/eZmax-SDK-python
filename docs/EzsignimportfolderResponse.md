# EzsignimportfolderResponse

A Ezsignimportfolder Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignimportfolder_id** | **int** | The unique ID of the Ezsignimportfolder | 
**s_ezsignimportfolder_name** | **str** | The name of the Ezsignimportfolder | 

## Example

```python
from eZmaxApi.models.ezsignimportfolder_response import EzsignimportfolderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignimportfolderResponse from a JSON string
ezsignimportfolder_response_instance = EzsignimportfolderResponse.from_json(json)
# print the JSON string representation of the object
print(EzsignimportfolderResponse.to_json())

# convert the object into a dict
ezsignimportfolder_response_dict = ezsignimportfolder_response_instance.to_dict()
# create an instance of EzsignimportfolderResponse from a dict
ezsignimportfolder_response_from_dict = EzsignimportfolderResponse.from_dict(ezsignimportfolder_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


