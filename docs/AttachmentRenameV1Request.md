# AttachmentRenameV1Request

Request for POST /1/object/attachment/{pkiAttachmentID}/rename

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_attachment_name** | **str** | The name of the Attachment | 
**s_attachment_category** | **str** | The attachment category | 
**b_force_override** | **bool** | Forces an override if the attachment name and category conflicts with another attachment. | [optional] 

## Example

```python
from eZmaxApi.models.attachment_rename_v1_request import AttachmentRenameV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentRenameV1Request from a JSON string
attachment_rename_v1_request_instance = AttachmentRenameV1Request.from_json(json)
# print the JSON string representation of the object
print(AttachmentRenameV1Request.to_json())

# convert the object into a dict
attachment_rename_v1_request_dict = attachment_rename_v1_request_instance.to_dict()
# create an instance of AttachmentRenameV1Request from a dict
attachment_rename_v1_request_from_dict = AttachmentRenameV1Request.from_dict(attachment_rename_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


