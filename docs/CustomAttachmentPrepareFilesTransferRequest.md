# CustomAttachmentPrepareFilesTransferRequest

A AttachmentPrepareFilesTransfer object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_attachment_name** | **str** | The name of the Attachment | 
**s_attachment_md5** | **str** | The MD5 of the Attachment | 

## Example

```python
from eZmaxApi.models.custom_attachment_prepare_files_transfer_request import CustomAttachmentPrepareFilesTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttachmentPrepareFilesTransferRequest from a JSON string
custom_attachment_prepare_files_transfer_request_instance = CustomAttachmentPrepareFilesTransferRequest.from_json(json)
# print the JSON string representation of the object
print(CustomAttachmentPrepareFilesTransferRequest.to_json())

# convert the object into a dict
custom_attachment_prepare_files_transfer_request_dict = custom_attachment_prepare_files_transfer_request_instance.to_dict()
# create an instance of CustomAttachmentPrepareFilesTransferRequest from a dict
custom_attachment_prepare_files_transfer_request_from_dict = CustomAttachmentPrepareFilesTransferRequest.from_dict(custom_attachment_prepare_files_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


