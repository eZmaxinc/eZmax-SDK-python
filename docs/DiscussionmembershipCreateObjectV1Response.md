# DiscussionmembershipCreateObjectV1Response

Response for POST /1/object/discussionmembership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DiscussionmembershipCreateObjectV1ResponseMPayload**](DiscussionmembershipCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.discussionmembership_create_object_v1_response import DiscussionmembershipCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionmembershipCreateObjectV1Response from a JSON string
discussionmembership_create_object_v1_response_instance = DiscussionmembershipCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(DiscussionmembershipCreateObjectV1Response.to_json())

# convert the object into a dict
discussionmembership_create_object_v1_response_dict = discussionmembership_create_object_v1_response_instance.to_dict()
# create an instance of DiscussionmembershipCreateObjectV1Response from a dict
discussionmembership_create_object_v1_response_from_dict = DiscussionmembershipCreateObjectV1Response.from_dict(discussionmembership_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


