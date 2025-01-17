# WebhookGetListV1Response

Response for GET /1/object/webhook/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**WebhookGetListV1ResponseMPayload**](WebhookGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.webhook_get_list_v1_response import WebhookGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookGetListV1Response from a JSON string
webhook_get_list_v1_response_instance = WebhookGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(WebhookGetListV1Response.to_json())

# convert the object into a dict
webhook_get_list_v1_response_dict = webhook_get_list_v1_response_instance.to_dict()
# create an instance of WebhookGetListV1Response from a dict
webhook_get_list_v1_response_from_dict = WebhookGetListV1Response.from_dict(webhook_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


