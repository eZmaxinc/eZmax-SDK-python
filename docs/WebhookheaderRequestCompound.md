# WebhookheaderRequestCompound

A Webhookheader Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_webhookheader_id** | **int** | The unique ID of the Webhookheader | [optional] 
**s_webhookheader_name** | **str** | The Name of the Webhookheader | 
**s_webhookheader_value** | **str** | The Value of the Webhookheader | 

## Example

```python
from eZmaxApi.models.webhookheader_request_compound import WebhookheaderRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookheaderRequestCompound from a JSON string
webhookheader_request_compound_instance = WebhookheaderRequestCompound.from_json(json)
# print the JSON string representation of the object
print(WebhookheaderRequestCompound.to_json())

# convert the object into a dict
webhookheader_request_compound_dict = webhookheader_request_compound_instance.to_dict()
# create an instance of WebhookheaderRequestCompound from a dict
webhookheader_request_compound_form_dict = webhookheader_request_compound.from_dict(webhookheader_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


