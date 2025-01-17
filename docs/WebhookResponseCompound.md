# WebhookResponseCompound

A Webhook Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_webhook_event** | **str** | The concatenated string to describe the Webhook event | [optional] 
**a_obj_webhookheader** | [**List[WebhookheaderResponseCompound]**](WebhookheaderResponseCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.webhook_response_compound import WebhookResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookResponseCompound from a JSON string
webhook_response_compound_instance = WebhookResponseCompound.from_json(json)
# print the JSON string representation of the object
print(WebhookResponseCompound.to_json())

# convert the object into a dict
webhook_response_compound_dict = webhook_response_compound_instance.to_dict()
# create an instance of WebhookResponseCompound from a dict
webhook_response_compound_from_dict = WebhookResponseCompound.from_dict(webhook_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


