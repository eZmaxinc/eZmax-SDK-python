# DiscussionPatchObjectV1Response

Response for PATCH /1/object/discussion/{pkiDiscussionID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.discussion_patch_object_v1_response import DiscussionPatchObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionPatchObjectV1Response from a JSON string
discussion_patch_object_v1_response_instance = DiscussionPatchObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(DiscussionPatchObjectV1Response.to_json())

# convert the object into a dict
discussion_patch_object_v1_response_dict = discussion_patch_object_v1_response_instance.to_dict()
# create an instance of DiscussionPatchObjectV1Response from a dict
discussion_patch_object_v1_response_from_dict = DiscussionPatchObjectV1Response.from_dict(discussion_patch_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


