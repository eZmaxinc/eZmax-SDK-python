# CommonWebhook

This is the base Webhook object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_webhook** | [**CustomWebhookResponse**](CustomWebhookResponse.md) |  | 
**a_obj_attempt** | [**List[AttemptResponseCompound]**](AttemptResponseCompound.md) | An array containing details of previous attempts that were made to deliver the message. The array is empty if it&#39;s the first attempt. | 

## Example

```python
from eZmaxApi.models.common_webhook import CommonWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of CommonWebhook from a JSON string
common_webhook_instance = CommonWebhook.from_json(json)
# print the JSON string representation of the object
print CommonWebhook.to_json()

# convert the object into a dict
common_webhook_dict = common_webhook_instance.to_dict()
# create an instance of CommonWebhook from a dict
common_webhook_form_dict = common_webhook.from_dict(common_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


