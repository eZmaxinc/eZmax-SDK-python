# DiscussionGetObjectV2Response

Response for GET /2/object/discussion/{pkiDiscussionID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**DiscussionGetObjectV2ResponseMPayload**](DiscussionGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.discussion_get_object_v2_response import DiscussionGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionGetObjectV2Response from a JSON string
discussion_get_object_v2_response_instance = DiscussionGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(DiscussionGetObjectV2Response.to_json())

# convert the object into a dict
discussion_get_object_v2_response_dict = discussion_get_object_v2_response_instance.to_dict()
# create an instance of DiscussionGetObjectV2Response from a dict
discussion_get_object_v2_response_from_dict = DiscussionGetObjectV2Response.from_dict(discussion_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


