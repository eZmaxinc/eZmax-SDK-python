# DiscussionUpdateDiscussionreadstatusV1Request

Request for POST /1/object/discussion/{pkiDiscussionID}/updateDiscussionreadstatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dt_discussionreadstatus_date** | **str** | The date of the last discussion message read | [optional] 

## Example

```python
from eZmaxApi.models.discussion_update_discussionreadstatus_v1_request import DiscussionUpdateDiscussionreadstatusV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionUpdateDiscussionreadstatusV1Request from a JSON string
discussion_update_discussionreadstatus_v1_request_instance = DiscussionUpdateDiscussionreadstatusV1Request.from_json(json)
# print the JSON string representation of the object
print(DiscussionUpdateDiscussionreadstatusV1Request.to_json())

# convert the object into a dict
discussion_update_discussionreadstatus_v1_request_dict = discussion_update_discussionreadstatus_v1_request_instance.to_dict()
# create an instance of DiscussionUpdateDiscussionreadstatusV1Request from a dict
discussion_update_discussionreadstatus_v1_request_from_dict = DiscussionUpdateDiscussionreadstatusV1Request.from_dict(discussion_update_discussionreadstatus_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


