# CustomNotificationsubsectiongetnotificationtestsResponse

A Notificationsubsection Object in the context of getNotificationtests

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_notificationsubsection_id** | **int** | The unique ID of the Notificationsubsection | 
**fki_notificationsection_id** | **int** | The unique ID of the Notificationsection | 
**obj_notificationsubsection_name** | [**MultilingualNotificationsubsectionName**](MultilingualNotificationsubsectionName.md) |  | [optional] 
**s_notificationsection_name_x** | **str** | The name of the Notificationsection in the language of the requester | [optional] 
**s_notificationsubsection_name_x** | **str** | The name of the Notificationsubsection in the language of the requester | 
**a_obj_notificationtest** | [**List[CustomNotificationtestgetnotificationtestsResponse]**](CustomNotificationtestgetnotificationtestsResponse.md) |  | 

## Example

```python
from eZmaxApi.models.custom_notificationsubsectiongetnotificationtests_response import CustomNotificationsubsectiongetnotificationtestsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomNotificationsubsectiongetnotificationtestsResponse from a JSON string
custom_notificationsubsectiongetnotificationtests_response_instance = CustomNotificationsubsectiongetnotificationtestsResponse.from_json(json)
# print the JSON string representation of the object
print CustomNotificationsubsectiongetnotificationtestsResponse.to_json()

# convert the object into a dict
custom_notificationsubsectiongetnotificationtests_response_dict = custom_notificationsubsectiongetnotificationtests_response_instance.to_dict()
# create an instance of CustomNotificationsubsectiongetnotificationtestsResponse from a dict
custom_notificationsubsectiongetnotificationtests_response_form_dict = custom_notificationsubsectiongetnotificationtests_response.from_dict(custom_notificationsubsectiongetnotificationtests_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


