# DiscussionRequestCompound

A Discussion Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_discussion_id** | **int** | The unique ID of the Discussion | [optional] 
**s_discussion_description** | **str** | The description of the Discussion | 
**b_discussion_closed** | **bool** | Whether if it&#39;s an closed | [optional] 

## Example

```python
from eZmaxApi.models.discussion_request_compound import DiscussionRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionRequestCompound from a JSON string
discussion_request_compound_instance = DiscussionRequestCompound.from_json(json)
# print the JSON string representation of the object
print DiscussionRequestCompound.to_json()

# convert the object into a dict
discussion_request_compound_dict = discussion_request_compound_instance.to_dict()
# create an instance of DiscussionRequestCompound from a dict
discussion_request_compound_form_dict = discussion_request_compound.from_dict(discussion_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


