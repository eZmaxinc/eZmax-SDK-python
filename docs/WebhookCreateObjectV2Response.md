# WebhookCreateObjectV2Response

Response for POST /2/object/webhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**WebhookCreateObjectV2ResponseMPayload**](WebhookCreateObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_create_object_v2_response import WebhookCreateObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCreateObjectV2Response from a JSON string
webhook_create_object_v2_response_instance = WebhookCreateObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(WebhookCreateObjectV2Response.to_json())

# convert the object into a dict
webhook_create_object_v2_response_dict = webhook_create_object_v2_response_instance.to_dict()
# create an instance of WebhookCreateObjectV2Response from a dict
webhook_create_object_v2_response_from_dict = WebhookCreateObjectV2Response.from_dict(webhook_create_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


