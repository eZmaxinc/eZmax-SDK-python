# CustomWebhooklogResponse

A custom Webhooklog object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dt_webhooklog_date** | **str** | The date and time at which the Webhooklog happened. | 
**t_webhooklog_json** | **str** | The Json containing the Webhook call and return | 

## Example

```python
from eZmaxApi.models.custom_webhooklog_response import CustomWebhooklogResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomWebhooklogResponse from a JSON string
custom_webhooklog_response_instance = CustomWebhooklogResponse.from_json(json)
# print the JSON string representation of the object
print(CustomWebhooklogResponse.to_json())

# convert the object into a dict
custom_webhooklog_response_dict = custom_webhooklog_response_instance.to_dict()
# create an instance of CustomWebhooklogResponse from a dict
custom_webhooklog_response_from_dict = CustomWebhooklogResponse.from_dict(custom_webhooklog_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


