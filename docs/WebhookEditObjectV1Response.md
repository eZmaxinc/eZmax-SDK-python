# WebhookEditObjectV1Response

Response for PUT /1/object/webhook/{pkiWebhookID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from eZmaxApi.models.webhook_edit_object_v1_response import WebhookEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEditObjectV1Response from a JSON string
webhook_edit_object_v1_response_instance = WebhookEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(WebhookEditObjectV1Response.to_json())

# convert the object into a dict
webhook_edit_object_v1_response_dict = webhook_edit_object_v1_response_instance.to_dict()
# create an instance of WebhookEditObjectV1Response from a dict
webhook_edit_object_v1_response_from_dict = WebhookEditObjectV1Response.from_dict(webhook_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


