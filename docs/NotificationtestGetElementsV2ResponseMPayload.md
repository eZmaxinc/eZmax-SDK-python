# NotificationtestGetElementsV2ResponseMPayload

Payload for GET /2/object/notificationtest/{pkiNotificationtestID}/getElements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_notificationtest** | [**CustomNotificationtestgetelementsResponse**](CustomNotificationtestgetelementsResponse.md) |  | 

## Example

```python
from eZmaxApi.models.notificationtest_get_elements_v2_response_m_payload import NotificationtestGetElementsV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationtestGetElementsV2ResponseMPayload from a JSON string
notificationtest_get_elements_v2_response_m_payload_instance = NotificationtestGetElementsV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(NotificationtestGetElementsV2ResponseMPayload.to_json())

# convert the object into a dict
notificationtest_get_elements_v2_response_m_payload_dict = notificationtest_get_elements_v2_response_m_payload_instance.to_dict()
# create an instance of NotificationtestGetElementsV2ResponseMPayload from a dict
notificationtest_get_elements_v2_response_m_payload_from_dict = NotificationtestGetElementsV2ResponseMPayload.from_dict(notificationtest_get_elements_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


