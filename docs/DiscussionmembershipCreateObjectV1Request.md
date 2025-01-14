# DiscussionmembershipCreateObjectV1Request

Request for POST /1/object/discussionmembership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_discussionmembership** | [**List[DiscussionmembershipRequestCompound]**](DiscussionmembershipRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.discussionmembership_create_object_v1_request import DiscussionmembershipCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionmembershipCreateObjectV1Request from a JSON string
discussionmembership_create_object_v1_request_instance = DiscussionmembershipCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(DiscussionmembershipCreateObjectV1Request.to_json())

# convert the object into a dict
discussionmembership_create_object_v1_request_dict = discussionmembership_create_object_v1_request_instance.to_dict()
# create an instance of DiscussionmembershipCreateObjectV1Request from a dict
discussionmembership_create_object_v1_request_from_dict = DiscussionmembershipCreateObjectV1Request.from_dict(discussionmembership_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


