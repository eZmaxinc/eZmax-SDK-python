# AttachmentPrivacyV1Request

Request for POST /1/object/attachment/{pkiAttachmentID}/privacy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_attachment_privacy** | [**FieldEAttachmentPrivacy**](FieldEAttachmentPrivacy.md) |  | 
**fki_user_id_specific** | **int** | The unique ID of the User | [optional] 

## Example

```python
from eZmaxApi.models.attachment_privacy_v1_request import AttachmentPrivacyV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentPrivacyV1Request from a JSON string
attachment_privacy_v1_request_instance = AttachmentPrivacyV1Request.from_json(json)
# print the JSON string representation of the object
print(AttachmentPrivacyV1Request.to_json())

# convert the object into a dict
attachment_privacy_v1_request_dict = attachment_privacy_v1_request_instance.to_dict()
# create an instance of AttachmentPrivacyV1Request from a dict
attachment_privacy_v1_request_from_dict = AttachmentPrivacyV1Request.from_dict(attachment_privacy_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


