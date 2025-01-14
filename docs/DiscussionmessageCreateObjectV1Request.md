# DiscussionmessageCreateObjectV1Request

Request for POST /1/object/discussionmessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_discussionmessage** | [**List[DiscussionmessageRequestCompound]**](DiscussionmessageRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.discussionmessage_create_object_v1_request import DiscussionmessageCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionmessageCreateObjectV1Request from a JSON string
discussionmessage_create_object_v1_request_instance = DiscussionmessageCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(DiscussionmessageCreateObjectV1Request.to_json())

# convert the object into a dict
discussionmessage_create_object_v1_request_dict = discussionmessage_create_object_v1_request_instance.to_dict()
# create an instance of DiscussionmessageCreateObjectV1Request from a dict
discussionmessage_create_object_v1_request_from_dict = DiscussionmessageCreateObjectV1Request.from_dict(discussionmessage_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


