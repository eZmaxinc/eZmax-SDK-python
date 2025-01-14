# AttachmentlogResponse

An Attachmentlog Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_attachment_id** | **int** | The unique ID of the Attachment. | 
**fki_user_id** | **int** | The unique ID of the User | 
**dt_attachmentlog_datetime** | **str** | The created date | 
**e_attachmentlog_type** | [**FieldEAttachmentlogType**](FieldEAttachmentlogType.md) |  | 
**s_attachmentlog_detail** | **str** | The additionnal detail | [optional] 

## Example

```python
from eZmaxApi.models.attachmentlog_response import AttachmentlogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentlogResponse from a JSON string
attachmentlog_response_instance = AttachmentlogResponse.from_json(json)
# print the JSON string representation of the object
print(AttachmentlogResponse.to_json())

# convert the object into a dict
attachmentlog_response_dict = attachmentlog_response_instance.to_dict()
# create an instance of AttachmentlogResponse from a dict
attachmentlog_response_from_dict = AttachmentlogResponse.from_dict(attachmentlog_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


