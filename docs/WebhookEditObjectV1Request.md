# WebhookEditObjectV1Request

Request for PUT /1/object/webhook/{pkiWebhookID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_webhook** | [**WebhookRequestCompound**](WebhookRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_edit_object_v1_request import WebhookEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookEditObjectV1Request from a JSON string
webhook_edit_object_v1_request_instance = WebhookEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print WebhookEditObjectV1Request.to_json()

# convert the object into a dict
webhook_edit_object_v1_request_dict = webhook_edit_object_v1_request_instance.to_dict()
# create an instance of WebhookEditObjectV1Request from a dict
webhook_edit_object_v1_request_form_dict = webhook_edit_object_v1_request.from_dict(webhook_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


