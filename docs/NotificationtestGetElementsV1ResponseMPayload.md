# NotificationtestGetElementsV1ResponseMPayload

Payload for GET /1/object/notificationtest/{pkiNotificationtestID}/getElements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_notificationtest_id** | **int** | The unique ID of the Notificationtest | 
**s_notificationtest_function** | **str** | The function name of the Notificationtest | 
**a_s_variableobject_property** | **List[str]** |  | 
**a_obj_variableobject** | **List[Dict[str, object]]** |  | 

## Example

```python
from eZmaxApi.models.notificationtest_get_elements_v1_response_m_payload import NotificationtestGetElementsV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationtestGetElementsV1ResponseMPayload from a JSON string
notificationtest_get_elements_v1_response_m_payload_instance = NotificationtestGetElementsV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(NotificationtestGetElementsV1ResponseMPayload.to_json())

# convert the object into a dict
notificationtest_get_elements_v1_response_m_payload_dict = notificationtest_get_elements_v1_response_m_payload_instance.to_dict()
# create an instance of NotificationtestGetElementsV1ResponseMPayload from a dict
notificationtest_get_elements_v1_response_m_payload_form_dict = notificationtest_get_elements_v1_response_m_payload.from_dict(notificationtest_get_elements_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


