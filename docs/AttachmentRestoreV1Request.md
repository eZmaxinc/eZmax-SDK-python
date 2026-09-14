# AttachmentRestoreV1Request

Request for POST /1/object/attachment/{pkiAttachmentID}/restore

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**b_force_override** | **bool** | Forces an override if the attachment name and category conflicts with another attachment. | [optional] 

## Example

```python
from eZmaxApi.models.attachment_restore_v1_request import AttachmentRestoreV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentRestoreV1Request from a JSON string
attachment_restore_v1_request_instance = AttachmentRestoreV1Request.from_json(json)
# print the JSON string representation of the object
print(AttachmentRestoreV1Request.to_json())

# convert the object into a dict
attachment_restore_v1_request_dict = attachment_restore_v1_request_instance.to_dict()
# create an instance of AttachmentRestoreV1Request from a dict
attachment_restore_v1_request_from_dict = AttachmentRestoreV1Request.from_dict(attachment_restore_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


