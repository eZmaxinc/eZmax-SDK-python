# CustomFormDataDocumentResponse

A form Data Document Object 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigndocument_id** | **int** | The unique ID of the Ezsigndocument | 
**fki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | 
**s_ezsigndocument_name** | **str** | The name of the document that will be presented to Ezsignfoldersignerassociations | 
**dt_modified_date** | **str** | The date and time at which the object was last modified | 
**a_obj_form_data_signer** | [**List[CustomFormDataSignerResponse]**](CustomFormDataSignerResponse.md) |  | 

## Example

```python
from eZmaxApi.models.custom_form_data_document_response import CustomFormDataDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFormDataDocumentResponse from a JSON string
custom_form_data_document_response_instance = CustomFormDataDocumentResponse.from_json(json)
# print the JSON string representation of the object
print(CustomFormDataDocumentResponse.to_json())

# convert the object into a dict
custom_form_data_document_response_dict = custom_form_data_document_response_instance.to_dict()
# create an instance of CustomFormDataDocumentResponse from a dict
custom_form_data_document_response_from_dict = CustomFormDataDocumentResponse.from_dict(custom_form_data_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


