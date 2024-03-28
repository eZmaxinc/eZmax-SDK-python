# DiscussionmessagePatchObjectV1Request

Request for PATCH /1/object/discussionmessage/{pkiDiscussionmessageID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_discussionmessage** | [**DiscussionmessageRequestPatch**](DiscussionmessageRequestPatch.md) |  | 

## Example

```python
from eZmaxApi.models.discussionmessage_patch_object_v1_request import DiscussionmessagePatchObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionmessagePatchObjectV1Request from a JSON string
discussionmessage_patch_object_v1_request_instance = DiscussionmessagePatchObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(DiscussionmessagePatchObjectV1Request.to_json())

# convert the object into a dict
discussionmessage_patch_object_v1_request_dict = discussionmessage_patch_object_v1_request_instance.to_dict()
# create an instance of DiscussionmessagePatchObjectV1Request from a dict
discussionmessage_patch_object_v1_request_form_dict = discussionmessage_patch_object_v1_request.from_dict(discussionmessage_patch_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


