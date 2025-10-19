# CustomAttachmentPrepareFilesTransferResponse

A AttachmentPrepareFilesTransfer object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_attachment_name** | **str** | The name of the Attachment | 
**s_attachment_md5** | **str** | The MD5 of the Attachment | 
**e_attachment_action** | **str** | Returns the action required for the attachment | 

## Example

```python
from eZmaxApi.models.custom_attachment_prepare_files_transfer_response import CustomAttachmentPrepareFilesTransferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttachmentPrepareFilesTransferResponse from a JSON string
custom_attachment_prepare_files_transfer_response_instance = CustomAttachmentPrepareFilesTransferResponse.from_json(json)
# print the JSON string representation of the object
print(CustomAttachmentPrepareFilesTransferResponse.to_json())

# convert the object into a dict
custom_attachment_prepare_files_transfer_response_dict = custom_attachment_prepare_files_transfer_response_instance.to_dict()
# create an instance of CustomAttachmentPrepareFilesTransferResponse from a dict
custom_attachment_prepare_files_transfer_response_from_dict = CustomAttachmentPrepareFilesTransferResponse.from_dict(custom_attachment_prepare_files_transfer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


