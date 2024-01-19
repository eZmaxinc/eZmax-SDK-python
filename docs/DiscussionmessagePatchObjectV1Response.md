# DiscussionmessagePatchObjectV1Response

Response for PATCH /1/object/discussionmessage/{pkiDiscussionmessageID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.discussionmessage_patch_object_v1_response import DiscussionmessagePatchObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionmessagePatchObjectV1Response from a JSON string
discussionmessage_patch_object_v1_response_instance = DiscussionmessagePatchObjectV1Response.from_json(json)
# print the JSON string representation of the object
print DiscussionmessagePatchObjectV1Response.to_json()

# convert the object into a dict
discussionmessage_patch_object_v1_response_dict = discussionmessage_patch_object_v1_response_instance.to_dict()
# create an instance of DiscussionmessagePatchObjectV1Response from a dict
discussionmessage_patch_object_v1_response_form_dict = discussionmessage_patch_object_v1_response.from_dict(discussionmessage_patch_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


