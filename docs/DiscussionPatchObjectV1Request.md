# DiscussionPatchObjectV1Request

Request for PATCH /1/object/discussion/{pkiDiscussionID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_discussion** | [**DiscussionRequestPatch**](DiscussionRequestPatch.md) |  | 

## Example

```python
from eZmaxApi.models.discussion_patch_object_v1_request import DiscussionPatchObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionPatchObjectV1Request from a JSON string
discussion_patch_object_v1_request_instance = DiscussionPatchObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(DiscussionPatchObjectV1Request.to_json())

# convert the object into a dict
discussion_patch_object_v1_request_dict = discussion_patch_object_v1_request_instance.to_dict()
# create an instance of DiscussionPatchObjectV1Request from a dict
discussion_patch_object_v1_request_from_dict = DiscussionPatchObjectV1Request.from_dict(discussion_patch_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


