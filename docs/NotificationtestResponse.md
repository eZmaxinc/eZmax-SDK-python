# NotificationtestResponse

A Notificationtest Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_notificationtest_id** | **int** | The unique ID of the Notificationtest | 
**obj_notificationtest_name** | [**MultilingualNotificationtestName**](MultilingualNotificationtestName.md) |  | 
**fki_notificationsubsection_id** | **int** | The unique ID of the Notificationsubsection | 
**s_notificationtest_function** | **str** | The function name of the Notificationtest | 
**s_notificationtest_name_x** | **str** | The name of the Notificationtest in the language of the requester | 

## Example

```python
from eZmaxApi.models.notificationtest_response import NotificationtestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationtestResponse from a JSON string
notificationtest_response_instance = NotificationtestResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationtestResponse.to_json())

# convert the object into a dict
notificationtest_response_dict = notificationtest_response_instance.to_dict()
# create an instance of NotificationtestResponse from a dict
notificationtest_response_form_dict = notificationtest_response.from_dict(notificationtest_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


