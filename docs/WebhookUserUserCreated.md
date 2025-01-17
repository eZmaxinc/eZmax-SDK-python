# WebhookUserUserCreated

This is the base Webhook object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_user** | [**UserResponse**](UserResponse.md) | A User Object and children to create a complete structure | 

## Example

```python
from eZmaxApi.models.webhook_user_user_created import WebhookUserUserCreated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookUserUserCreated from a JSON string
webhook_user_user_created_instance = WebhookUserUserCreated.from_json(json)
# print the JSON string representation of the object
print(WebhookUserUserCreated.to_json())

# convert the object into a dict
webhook_user_user_created_dict = webhook_user_user_created_instance.to_dict()
# create an instance of WebhookUserUserCreated from a dict
webhook_user_user_created_from_dict = WebhookUserUserCreated.from_dict(webhook_user_user_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


