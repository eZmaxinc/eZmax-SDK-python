# EzsignimportfolderResponseCompound

A Ezsignimportfolder Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignimportfolder_id** | **int** | The unique ID of the Ezsignimportfolder | 
**s_ezsignimportfolder_name** | **str** | The name of the Ezsignimportfolder | 
**a_obj_ezsignimportdocument** | [**List[CustomEzsignimportdocumentResponse]**](CustomEzsignimportdocumentResponse.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignimportfolder_response_compound import EzsignimportfolderResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignimportfolderResponseCompound from a JSON string
ezsignimportfolder_response_compound_instance = EzsignimportfolderResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignimportfolderResponseCompound.to_json())

# convert the object into a dict
ezsignimportfolder_response_compound_dict = ezsignimportfolder_response_compound_instance.to_dict()
# create an instance of EzsignimportfolderResponseCompound from a dict
ezsignimportfolder_response_compound_from_dict = EzsignimportfolderResponseCompound.from_dict(ezsignimportfolder_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


