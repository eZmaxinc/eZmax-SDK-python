# CustomNotificationtestgetnotificationtestsResponse

A Notificationtest Object in the context of getNotificationtests

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
print(CustomNotificationtestgetnotificationtestsResponse.to_json())

# convert the object into a dict
custom_notificationtestgetnotificationtests_response_dict = custom_notificationtestgetnotificationtests_response_instance.to_dict()
# create an instance of CustomNotificationtestgetnotificationtestsResponse from a dict
custom_notificationtestgetnotificationtests_response_from_dict = CustomNotificationtestgetnotificationtestsResponse.from_dict(custom_notificationtestgetnotificationtests_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


