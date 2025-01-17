# WebhookGetObjectV2Response

Response for GET /2/object/webhook/{pkiWebhookID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**WebhookGetObjectV2ResponseMPayload**](WebhookGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_get_object_v2_response import WebhookGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookGetObjectV2Response from a JSON string
webhook_get_object_v2_response_instance = WebhookGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(WebhookGetObjectV2Response.to_json())

# convert the object into a dict
webhook_get_object_v2_response_dict = webhook_get_object_v2_response_instance.to_dict()
# create an instance of WebhookGetObjectV2Response from a dict
webhook_get_object_v2_response_from_dict = WebhookGetObjectV2Response.from_dict(webhook_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


