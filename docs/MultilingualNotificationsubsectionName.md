# MultilingualNotificationsubsectionName

Name of the Notificationsubsection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_notificationsubsection_name1** | **str** | The name of the Notificationsubsection in French | [optional] 
**s_notificationsubsection_name2** | **str** | The name of the Notificationsubsection in English | [optional] 

## Example

```python
from eZmaxApi.models.multilingual_notificationsubsection_name import MultilingualNotificationsubsectionName

# TODO update the JSON string below
json = "{}"
# create an instance of MultilingualNotificationsubsectionName from a JSON string
multilingual_notificationsubsection_name_instance = MultilingualNotificationsubsectionName.from_json(json)
# print the JSON string representation of the object
print(MultilingualNotificationsubsectionName.to_json())

# convert the object into a dict
multilingual_notificationsubsection_name_dict = multilingual_notificationsubsection_name_instance.to_dict()
# create an instance of MultilingualNotificationsubsectionName from a dict
multilingual_notificationsubsection_name_form_dict = multilingual_notificationsubsection_name.from_dict(multilingual_notificationsubsection_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


