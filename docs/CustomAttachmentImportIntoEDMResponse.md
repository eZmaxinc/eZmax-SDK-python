# CustomAttachmentImportIntoEDMResponse

A AttachmentImportIntoEDM object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_attachment_id_source** | **int** | The unique ID of the Attachment. | [optional] 
**pki_attachment_id_new** | **int** | The unique ID of the Attachment. | [optional] 
**e_attachment_status** | **str** |  | [optional] 
**b_allow_overwrite** | **bool** | Whether we allow or not the file overwrite | [optional] 

## Example

```python
from eZmaxApi.models.custom_attachment_import_into_edm_response import CustomAttachmentImportIntoEDMResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttachmentImportIntoEDMResponse from a JSON string
custom_attachment_import_into_edm_response_instance = CustomAttachmentImportIntoEDMResponse.from_json(json)
# print the JSON string representation of the object
print(CustomAttachmentImportIntoEDMResponse.to_json())

# convert the object into a dict
custom_attachment_import_into_edm_response_dict = custom_attachment_import_into_edm_response_instance.to_dict()
# create an instance of CustomAttachmentImportIntoEDMResponse from a dict
custom_attachment_import_into_edm_response_from_dict = CustomAttachmentImportIntoEDMResponse.from_dict(custom_attachment_import_into_edm_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


