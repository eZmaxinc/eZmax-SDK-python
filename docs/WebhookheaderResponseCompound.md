# WebhookheaderResponseCompound

A Webhookheader Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_webhookheader_id** | **int** | The unique ID of the Webhookheader | 
**fki_webhook_id** | **int** | The unique ID of the Webhook | 
**s_webhookheader_name** | **str** | The Name of the Webhookheader | 
**s_webhookheader_value** | **str** | The Value of the Webhookheader | 

## Example

```python
from eZmaxApi.models.webhookheader_response_compound import WebhookheaderResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookheaderResponseCompound from a JSON string
webhookheader_response_compound_instance = WebhookheaderResponseCompound.from_json(json)
# print the JSON string representation of the object
print(WebhookheaderResponseCompound.to_json())

# convert the object into a dict
webhookheader_response_compound_dict = webhookheader_response_compound_instance.to_dict()
# create an instance of WebhookheaderResponseCompound from a dict
webhookheader_response_compound_form_dict = webhookheader_response_compound.from_dict(webhookheader_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


