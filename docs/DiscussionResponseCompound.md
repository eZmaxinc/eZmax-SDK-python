# DiscussionResponseCompound

A Discussion Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_discussion_id** | **int** | The unique ID of the Discussion | 
**s_discussion_description** | **str** | The description of the Discussion | 
**b_discussion_closed** | **bool** | Whether if it&#39;s an closed | 
**dt_discussion_lastread** | **str** | The date the Discussion was last read | [optional] 
**i_discussionmessage_count** | **int** | The count of Attachment. | 
**i_discussionmessage_countunread** | **int** | The count of Attachment. | 
**obj_discussionconfiguration** | [**CustomDiscussionconfigurationResponse**](CustomDiscussionconfigurationResponse.md) |  | [optional] 
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
print DiscussionResponseCompound.to_json()

# convert the object into a dict
discussion_response_compound_dict = discussion_response_compound_instance.to_dict()
# create an instance of DiscussionResponseCompound from a dict
discussion_response_compound_form_dict = discussion_response_compound.from_dict(discussion_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


