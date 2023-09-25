# NotificationsectionGetNotificationtestsV1ResponseMPayload

Payload for GET /1/object/notificationsection/{pkiNotificationsectionID}/getNotificationtests

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_notificationsubsection** | [**List[CustomNotificationsubsectiongetnotificationtestsResponse]**](CustomNotificationsubsectiongetnotificationtestsResponse.md) |  | 

## Example

```python
from eZmaxApi.models.notificationsection_get_notificationtests_v1_response_m_payload import NotificationsectionGetNotificationtestsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsectionGetNotificationtestsV1ResponseMPayload from a JSON string
notificationsection_get_notificationtests_v1_response_m_payload_instance = NotificationsectionGetNotificationtestsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print NotificationsectionGetNotificationtestsV1ResponseMPayload.to_json()

# convert the object into a dict
notificationsection_get_notificationtests_v1_response_m_payload_dict = notificationsection_get_notificationtests_v1_response_m_payload_instance.to_dict()
# create an instance of NotificationsectionGetNotificationtestsV1ResponseMPayload from a dict
notificationsection_get_notificationtests_v1_response_m_payload_form_dict = notificationsection_get_notificationtests_v1_response_m_payload.from_dict(notificationsection_get_notificationtests_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


