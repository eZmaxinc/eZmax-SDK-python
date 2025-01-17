# DiscussionResponseCompound

A Discussion Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_discussionmembership** | [**List[DiscussionmembershipResponseCompound]**](DiscussionmembershipResponseCompound.md) |  | 
**a_obj_discussionmessage** | [**List[DiscussionmessageResponseCompound]**](DiscussionmessageResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.discussion_response_compound import DiscussionResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionResponseCompound from a JSON string
discussion_response_compound_instance = DiscussionResponseCompound.from_json(json)
# print the JSON string representation of the object
print(DiscussionResponseCompound.to_json())

# convert the object into a dict
discussion_response_compound_dict = discussion_response_compound_instance.to_dict()
# create an instance of DiscussionResponseCompound from a dict
discussion_response_compound_from_dict = DiscussionResponseCompound.from_dict(discussion_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


