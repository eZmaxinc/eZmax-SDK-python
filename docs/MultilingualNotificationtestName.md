# MultilingualNotificationtestName

Name of the Notificationtest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_notificationtest_name1** | **str** | The name of the Notificationtest in French | [optional] 
**s_notificationtest_name2** | **str** | The name of the Notificationtest in English | [optional] 

## Example

```python
from eZmaxApi.models.multilingual_notificationtest_name import MultilingualNotificationtestName

# TODO update the JSON string below
json = "{}"
# create an instance of MultilingualNotificationtestName from a JSON string
multilingual_notificationtest_name_instance = MultilingualNotificationtestName.from_json(json)
# print the JSON string representation of the object
print MultilingualNotificationtestName.to_json()

# convert the object into a dict
multilingual_notificationtest_name_dict = multilingual_notificationtest_name_instance.to_dict()
# create an instance of MultilingualNotificationtestName from a dict
multilingual_notificationtest_name_form_dict = multilingual_notificationtest_name.from_dict(multilingual_notificationtest_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


