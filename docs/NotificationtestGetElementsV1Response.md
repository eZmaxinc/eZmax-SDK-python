# NotificationtestGetElementsV1Response

Response for GET /1/object/notificationtest/{pkiNotificationtestID}/getElements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**NotificationtestGetElementsV1ResponseMPayload**](NotificationtestGetElementsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.notificationtest_get_elements_v1_response import NotificationtestGetElementsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationtestGetElementsV1Response from a JSON string
notificationtest_get_elements_v1_response_instance = NotificationtestGetElementsV1Response.from_json(json)
# print the JSON string representation of the object
print NotificationtestGetElementsV1Response.to_json()

# convert the object into a dict
notificationtest_get_elements_v1_response_dict = notificationtest_get_elements_v1_response_instance.to_dict()
# create an instance of NotificationtestGetElementsV1Response from a dict
notificationtest_get_elements_v1_response_form_dict = notificationtest_get_elements_v1_response.from_dict(notificationtest_get_elements_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


