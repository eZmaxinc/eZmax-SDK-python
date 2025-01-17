# NotificationsectionGetNotificationtestsV1Response

Response for GET /1/object/notificationsection/{pkiNotificationsectionID}/getNotificationtests

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**NotificationsectionGetNotificationtestsV1ResponseMPayload**](NotificationsectionGetNotificationtestsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.notificationsection_get_notificationtests_v1_response import NotificationsectionGetNotificationtestsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsectionGetNotificationtestsV1Response from a JSON string
notificationsection_get_notificationtests_v1_response_instance = NotificationsectionGetNotificationtestsV1Response.from_json(json)
# print the JSON string representation of the object
print(NotificationsectionGetNotificationtestsV1Response.to_json())

# convert the object into a dict
notificationsection_get_notificationtests_v1_response_dict = notificationsection_get_notificationtests_v1_response_instance.to_dict()
# create an instance of NotificationsectionGetNotificationtestsV1Response from a dict
notificationsection_get_notificationtests_v1_response_from_dict = NotificationsectionGetNotificationtestsV1Response.from_dict(notificationsection_get_notificationtests_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


