# DiscussionDeleteObjectV1Response

Response for DELETE /1/object/discussion/{pkiDiscussionID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.discussion_delete_object_v1_response import DiscussionDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionDeleteObjectV1Response from a JSON string
discussion_delete_object_v1_response_instance = DiscussionDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(DiscussionDeleteObjectV1Response.to_json())

# convert the object into a dict
discussion_delete_object_v1_response_dict = discussion_delete_object_v1_response_instance.to_dict()
# create an instance of DiscussionDeleteObjectV1Response from a dict
discussion_delete_object_v1_response_from_dict = DiscussionDeleteObjectV1Response.from_dict(discussion_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


