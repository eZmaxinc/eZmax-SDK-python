# CustomAttachmentImportIntoEDMRequest

A AttachmentImportIntoEDM object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_attachment_source** | **str** | The source of the Attachment | 
**fki_attachment_id** | **int** | The unique ID of the Attachment. | [optional] 
**fki_inscriptionchecklist_id** | **int** | The unique ID of the Inscriptionchecklist | [optional] 
**s_attachment_url** | **str** | The url of the file to import | [optional] 
**s_attachment_base64** | **bytearray** | The Base64 encoded binary content of the attachment. | [optional] 
**s_attachment_name** | **str** | The name of the Attachment | 
**s_attachment_category** | **str** | The attachment category | 
**e_attachment_privacy** | [**FieldEAttachmentPrivacy**](FieldEAttachmentPrivacy.md) |  | 
**fki_user_id_specific** | **int** | The unique ID of the User | [optional] 
**s_attachment_md5** | **str** | The MD5 of the Attachment | [optional] 
**b_attachment_forceoverwrite** | **bool** | Whether we force an overwrite of an existing file | [optional] 
**b_attachment_forcerestore** | **bool** | Whether we force a restore of a deleted file | [optional] 

## Example

```python
from eZmaxApi.models.custom_attachment_import_into_edm_request import CustomAttachmentImportIntoEDMRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttachmentImportIntoEDMRequest from a JSON string
custom_attachment_import_into_edm_request_instance = CustomAttachmentImportIntoEDMRequest.from_json(json)
# print the JSON string representation of the object
print(CustomAttachmentImportIntoEDMRequest.to_json())

# convert the object into a dict
custom_attachment_import_into_edm_request_dict = custom_attachment_import_into_edm_request_instance.to_dict()
# create an instance of CustomAttachmentImportIntoEDMRequest from a dict
custom_attachment_import_into_edm_request_from_dict = CustomAttachmentImportIntoEDMRequest.from_dict(custom_attachment_import_into_edm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


