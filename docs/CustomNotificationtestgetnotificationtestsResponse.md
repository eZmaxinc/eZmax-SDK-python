# CustomNotificationtestgetnotificationtestsResponse

A Notificationtest Object in the context of getNotificationtests

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_notificationtest_id** | **int** | The unique ID of the Notificationtest | 
**obj_notificationtest_name** | [**MultilingualNotificationtestName**](MultilingualNotificationtestName.md) |  | 
**fki_notificationsubsection_id** | **int** | The unique ID of the Notificationsubsection | 
**s_notificationtest_function** | **str** | The function name of the Notificationtest | 
**s_notificationtest_name_x** | **str** | The name of the Notificationtest in the language of the requester | 
**e_notificationpreference_status** | [**FieldENotificationpreferenceStatus**](FieldENotificationpreferenceStatus.md) |  | 
**i_notificationtest** | **int** | The number of elements returned by the Notificationtest | 

## Example

```python
from eZmaxApi.models.custom_notificationtestgetnotificationtests_response import CustomNotificationtestgetnotificationtestsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomNotificationtestgetnotificationtestsResponse from a JSON string
custom_notificationtestgetnotificationtests_response_instance = CustomNotificationtestgetnotificationtestsResponse.from_json(json)
# print the JSON string representation of the object
print CustomNotificationtestgetnotificationtestsResponse.to_json()

# convert the object into a dict
custom_notificationtestgetnotificationtests_response_dict = custom_notificationtestgetnotificationtests_response_instance.to_dict()
# create an instance of CustomNotificationtestgetnotificationtestsResponse from a dict
custom_notificationtestgetnotificationtests_response_form_dict = custom_notificationtestgetnotificationtests_response.from_dict(custom_notificationtestgetnotificationtests_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


