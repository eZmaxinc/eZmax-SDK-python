# WebhookCreateObjectV1Response

Response for POST /1/object/webhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**WebhookCreateObjectV1ResponseMPayload**](WebhookCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_create_object_v1_response import WebhookCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCreateObjectV1Response from a JSON string
webhook_create_object_v1_response_instance = WebhookCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print WebhookCreateObjectV1Response.to_json()

# convert the object into a dict
webhook_create_object_v1_response_dict = webhook_create_object_v1_response_instance.to_dict()
# create an instance of WebhookCreateObjectV1Response from a dict
webhook_create_object_v1_response_form_dict = webhook_create_object_v1_response.from_dict(webhook_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


