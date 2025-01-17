# DiscussionmembershipDeleteObjectV1Response

Response for DELETE /1/object/discussionmembership/{pkiDiscussionmembershipID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.discussionmembership_delete_object_v1_response import DiscussionmembershipDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionmembershipDeleteObjectV1Response from a JSON string
discussionmembership_delete_object_v1_response_instance = DiscussionmembershipDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(DiscussionmembershipDeleteObjectV1Response.to_json())

# convert the object into a dict
discussionmembership_delete_object_v1_response_dict = discussionmembership_delete_object_v1_response_instance.to_dict()
# create an instance of DiscussionmembershipDeleteObjectV1Response from a dict
discussionmembership_delete_object_v1_response_from_dict = DiscussionmembershipDeleteObjectV1Response.from_dict(discussionmembership_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


