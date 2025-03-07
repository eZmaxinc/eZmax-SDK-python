# CustomEzsignimportdocumentResponse

An Ezsignimportdocument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignimportdocument_id** | **int** | The unique ID of the Ezsignimportdocument | 
**s_ezsignimportdocument_name** | **str** | The name of the Ezsignimportdocument | 
**fki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | [optional] 
**s_ezsignfolder_description** | **str** | The description of the Ezsignfolder | [optional] 

## Example

```python
from eZmaxApi.models.custom_ezsignimportdocument_response import CustomEzsignimportdocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsignimportdocumentResponse from a JSON string
custom_ezsignimportdocument_response_instance = CustomEzsignimportdocumentResponse.from_json(json)
# print the JSON string representation of the object
print(CustomEzsignimportdocumentResponse.to_json())

# convert the object into a dict
custom_ezsignimportdocument_response_dict = custom_ezsignimportdocument_response_instance.to_dict()
# create an instance of CustomEzsignimportdocumentResponse from a dict
custom_ezsignimportdocument_response_from_dict = CustomEzsignimportdocumentResponse.from_dict(custom_ezsignimportdocument_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


