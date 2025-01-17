# WebhookRequestCompound

A Webhook Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_webhookheader** | [**List[WebhookheaderRequestCompound]**](WebhookheaderRequestCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.webhook_request_compound import WebhookRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRequestCompound from a JSON string
webhook_request_compound_instance = WebhookRequestCompound.from_json(json)
# print the JSON string representation of the object
print(WebhookRequestCompound.to_json())

# convert the object into a dict
webhook_request_compound_dict = webhook_request_compound_instance.to_dict()
# create an instance of WebhookRequestCompound from a dict
webhook_request_compound_from_dict = WebhookRequestCompound.from_dict(webhook_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


