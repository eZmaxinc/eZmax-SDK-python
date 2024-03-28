# AttachmentlogResponseCompound

A Attachmentlog Object

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
from eZmaxApi.models.attachmentlog_response_compound import AttachmentlogResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentlogResponseCompound from a JSON string
attachmentlog_response_compound_instance = AttachmentlogResponseCompound.from_json(json)
# print the JSON string representation of the object
print(AttachmentlogResponseCompound.to_json())

# convert the object into a dict
attachmentlog_response_compound_dict = attachmentlog_response_compound_instance.to_dict()
# create an instance of AttachmentlogResponseCompound from a dict
attachmentlog_response_compound_form_dict = attachmentlog_response_compound.from_dict(attachmentlog_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


