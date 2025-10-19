# NotificationtestGetElementsV2Response

Response for GET /2/object/notificationtest/{pkiNotificationtestID}/getElements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**NotificationtestGetElementsV2ResponseMPayload**](NotificationtestGetElementsV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.notificationtest_get_elements_v2_response import NotificationtestGetElementsV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationtestGetElementsV2Response from a JSON string
notificationtest_get_elements_v2_response_instance = NotificationtestGetElementsV2Response.from_json(json)
# print the JSON string representation of the object
print(NotificationtestGetElementsV2Response.to_json())

# convert the object into a dict
notificationtest_get_elements_v2_response_dict = notificationtest_get_elements_v2_response_instance.to_dict()
# create an instance of NotificationtestGetElementsV2Response from a dict
notificationtest_get_elements_v2_response_from_dict = NotificationtestGetElementsV2Response.from_dict(notificationtest_get_elements_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


