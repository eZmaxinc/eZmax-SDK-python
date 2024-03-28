# DiscussionRequestPatch

A Discussion Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_discussion_description** | **str** | The description of the Discussion | [optional] 
**b_discussion_closed** | **bool** | Whether if it&#39;s an closed | [optional] 

## Example

```python
from eZmaxApi.models.discussion_request_patch import DiscussionRequestPatch

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionRequestPatch from a JSON string
discussion_request_patch_instance = DiscussionRequestPatch.from_json(json)
# print the JSON string representation of the object
print(DiscussionRequestPatch.to_json())

# convert the object into a dict
discussion_request_patch_dict = discussion_request_patch_instance.to_dict()
# create an instance of DiscussionRequestPatch from a dict
discussion_request_patch_form_dict = discussion_request_patch.from_dict(discussion_request_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


