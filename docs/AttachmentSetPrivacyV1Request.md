# AttachmentSetPrivacyV1Request

Request for POST /1/object/attachment/{pkiAttachmentID}/setPrivacy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_attachment_privacy** | [**FieldEAttachmentPrivacy**](FieldEAttachmentPrivacy.md) |  | 
**fki_user_id_specific** | **int** | The unique ID of the User | [optional] 

## Example

```python
from eZmaxApi.models.attachment_set_privacy_v1_request import AttachmentSetPrivacyV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentSetPrivacyV1Request from a JSON string
attachment_set_privacy_v1_request_instance = AttachmentSetPrivacyV1Request.from_json(json)
# print the JSON string representation of the object
print(AttachmentSetPrivacyV1Request.to_json())

# convert the object into a dict
attachment_set_privacy_v1_request_dict = attachment_set_privacy_v1_request_instance.to_dict()
# create an instance of AttachmentSetPrivacyV1Request from a dict
attachment_set_privacy_v1_request_from_dict = AttachmentSetPrivacyV1Request.from_dict(attachment_set_privacy_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


