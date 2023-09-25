# WebhookCreateObjectV1ResponseMPayload

Payload for POST /1/object/webhook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_webhook_id** | **List[int]** | An array of unique IDs representing the object that were requested to be created.  They are returned in the same order as the array containing the objects to be created that was sent in the request. | 

## Example

```python
from eZmaxApi.models.webhook_create_object_v1_response_m_payload import WebhookCreateObjectV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCreateObjectV1ResponseMPayload from a JSON string
webhook_create_object_v1_response_m_payload_instance = WebhookCreateObjectV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print WebhookCreateObjectV1ResponseMPayload.to_json()

# convert the object into a dict
webhook_create_object_v1_response_m_payload_dict = webhook_create_object_v1_response_m_payload_instance.to_dict()
# create an instance of WebhookCreateObjectV1ResponseMPayload from a dict
webhook_create_object_v1_response_m_payload_form_dict = webhook_create_object_v1_response_m_payload.from_dict(webhook_create_object_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


