# WebhookCreateObjectV2Request

Request for POST /2/object/webhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_webhook** | [**List[WebhookRequestCompound]**](WebhookRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_create_object_v2_request import WebhookCreateObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCreateObjectV2Request from a JSON string
webhook_create_object_v2_request_instance = WebhookCreateObjectV2Request.from_json(json)
# print the JSON string representation of the object
print(WebhookCreateObjectV2Request.to_json())

# convert the object into a dict
webhook_create_object_v2_request_dict = webhook_create_object_v2_request_instance.to_dict()
# create an instance of WebhookCreateObjectV2Request from a dict
webhook_create_object_v2_request_from_dict = WebhookCreateObjectV2Request.from_dict(webhook_create_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


