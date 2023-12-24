# NotificationsubsectionResponse

A Notificationsubsection Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_notificationsubsection_id** | **int** | The unique ID of the Notificationsubsection | 
**fki_notificationsection_id** | **int** | The unique ID of the Notificationsection | 
**obj_notificationsubsection_name** | [**MultilingualNotificationsubsectionName**](MultilingualNotificationsubsectionName.md) |  | [optional] 
**s_notificationsection_name_x** | **str** | The name of the Notificationsection in the language of the requester | [optional] 
**s_notificationsubsection_name_x** | **str** | The name of the Notificationsubsection in the language of the requester | 

## Example

```python
from eZmaxApi.models.notificationsubsection_response import NotificationsubsectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsubsectionResponse from a JSON string
notificationsubsection_response_instance = NotificationsubsectionResponse.from_json(json)
# print the JSON string representation of the object
print NotificationsubsectionResponse.to_json()

# convert the object into a dict
notificationsubsection_response_dict = notificationsubsection_response_instance.to_dict()
# create an instance of NotificationsubsectionResponse from a dict
notificationsubsection_response_form_dict = notificationsubsection_response.from_dict(notificationsubsection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


