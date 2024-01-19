# DiscussionCreateObjectV1Request

Request for POST /1/object/discussion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_discussion** | [**List[DiscussionRequestCompound]**](DiscussionRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.discussion_create_object_v1_request import DiscussionCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionCreateObjectV1Request from a JSON string
discussion_create_object_v1_request_instance = DiscussionCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print DiscussionCreateObjectV1Request.to_json()

# convert the object into a dict
discussion_create_object_v1_request_dict = discussion_create_object_v1_request_instance.to_dict()
# create an instance of DiscussionCreateObjectV1Request from a dict
discussion_create_object_v1_request_form_dict = discussion_create_object_v1_request.from_dict(discussion_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


