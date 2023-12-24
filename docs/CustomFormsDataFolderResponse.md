# CustomFormsDataFolderResponse

A forms Data Folder Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | 
**s_ezsignfolder_description** | **str** | The description of the Ezsignfolder | 
**a_obj_form_data_document** | [**List[CustomFormDataDocumentResponse]**](CustomFormDataDocumentResponse.md) |  | 

## Example

```python
from eZmaxApi.models.custom_forms_data_folder_response import CustomFormsDataFolderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFormsDataFolderResponse from a JSON string
custom_forms_data_folder_response_instance = CustomFormsDataFolderResponse.from_json(json)
# print the JSON string representation of the object
print CustomFormsDataFolderResponse.to_json()

# convert the object into a dict
custom_forms_data_folder_response_dict = custom_forms_data_folder_response_instance.to_dict()
# create an instance of CustomFormsDataFolderResponse from a dict
custom_forms_data_folder_response_form_dict = custom_forms_data_folder_response.from_dict(custom_forms_data_folder_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


