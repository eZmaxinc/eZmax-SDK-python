# CustomNotificationtestgetelementsResponse

Element Object in the context of Notificationtest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_notificationtest_id** | **int** | The unique ID of the Notificationtest | 
**s_notificationtest_function** | **str** | The function name of the Notificationtest | 
**a_s_variableobject_property** | **List[str]** |  | 
**a_obj_variableobject** | **List[Dict[str, object]]** |  | 

## Example

```python
from eZmaxApi.models.custom_notificationtestgetelements_response import CustomNotificationtestgetelementsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomNotificationtestgetelementsResponse from a JSON string
custom_notificationtestgetelements_response_instance = CustomNotificationtestgetelementsResponse.from_json(json)
# print the JSON string representation of the object
print(CustomNotificationtestgetelementsResponse.to_json())

# convert the object into a dict
custom_notificationtestgetelements_response_dict = custom_notificationtestgetelements_response_instance.to_dict()
# create an instance of CustomNotificationtestgetelementsResponse from a dict
custom_notificationtestgetelements_response_from_dict = CustomNotificationtestgetelementsResponse.from_dict(custom_notificationtestgetelements_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


