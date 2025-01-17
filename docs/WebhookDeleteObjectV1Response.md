# WebhookDeleteObjectV1Response

Response for DELETE /1/object/webhook/{pkiWebhookID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.webhook_delete_object_v1_response import WebhookDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeleteObjectV1Response from a JSON string
webhook_delete_object_v1_response_instance = WebhookDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(WebhookDeleteObjectV1Response.to_json())

# convert the object into a dict
webhook_delete_object_v1_response_dict = webhook_delete_object_v1_response_instance.to_dict()
# create an instance of WebhookDeleteObjectV1Response from a dict
webhook_delete_object_v1_response_from_dict = WebhookDeleteObjectV1Response.from_dict(webhook_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


