# WebhookheaderRequest

A webhookheader object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_webhookheader_id** | **int** | The unique ID of the Webhookheader | [optional] 
**s_webhookheader_name** | **str** | The Name of the Webhookheader | 
**s_webhookheader_value** | **str** | The Value of the Webhookheader | 

## Example

```python
from eZmaxApi.models.webhookheader_request import WebhookheaderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookheaderRequest from a JSON string
webhookheader_request_instance = WebhookheaderRequest.from_json(json)
# print the JSON string representation of the object
print(WebhookheaderRequest.to_json())

# convert the object into a dict
webhookheader_request_dict = webhookheader_request_instance.to_dict()
# create an instance of WebhookheaderRequest from a dict
webhookheader_request_from_dict = WebhookheaderRequest.from_dict(webhookheader_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


