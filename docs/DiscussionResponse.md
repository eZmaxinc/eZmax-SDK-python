# DiscussionResponse

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

## Example

```python
from eZmaxApi.models.discussion_response import DiscussionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionResponse from a JSON string
discussion_response_instance = DiscussionResponse.from_json(json)
# print the JSON string representation of the object
print(DiscussionResponse.to_json())

# convert the object into a dict
discussion_response_dict = discussion_response_instance.to_dict()
# create an instance of DiscussionResponse from a dict
discussion_response_form_dict = discussion_response.from_dict(discussion_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


