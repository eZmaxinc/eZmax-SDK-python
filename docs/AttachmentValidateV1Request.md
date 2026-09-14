# AttachmentValidateV1Request

Request for PATCH /1/object/attachment/{pkiAttachmentID}/validate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_attachment_verified** | [**FieldEAttachmentVerified**](FieldEAttachmentVerified.md) |  | 

## Example

```python
from eZmaxApi.models.attachment_validate_v1_request import AttachmentValidateV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentValidateV1Request from a JSON string
attachment_validate_v1_request_instance = AttachmentValidateV1Request.from_json(json)
# print the JSON string representation of the object
print(AttachmentValidateV1Request.to_json())

# convert the object into a dict
attachment_validate_v1_request_dict = attachment_validate_v1_request_instance.to_dict()
# create an instance of AttachmentValidateV1Request from a dict
attachment_validate_v1_request_from_dict = AttachmentValidateV1Request.from_dict(attachment_validate_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


