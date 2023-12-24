# WebhookCreateObjectV1Request

Request for POST /1/object/webhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_webhook** | [**List[WebhookRequestCompound]**](WebhookRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_create_object_v1_request import WebhookCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCreateObjectV1Request from a JSON string
webhook_create_object_v1_request_instance = WebhookCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print WebhookCreateObjectV1Request.to_json()

# convert the object into a dict
webhook_create_object_v1_request_dict = webhook_create_object_v1_request_instance.to_dict()
# create an instance of WebhookCreateObjectV1Request from a dict
webhook_create_object_v1_request_form_dict = webhook_create_object_v1_request.from_dict(webhook_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


