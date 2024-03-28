# MultilingualVersionhistoryDetail

Detail of the Versionhistory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**t_versionhistory_detail1** | **str** | Detail of the Versionhistory in French | [optional] 
**t_versionhistory_detail2** | **str** | Detail of the Versionhistory in English | [optional] 

## Example

```python
from eZmaxApi.models.multilingual_versionhistory_detail import MultilingualVersionhistoryDetail

# TODO update the JSON string below
json = "{}"
# create an instance of MultilingualVersionhistoryDetail from a JSON string
multilingual_versionhistory_detail_instance = MultilingualVersionhistoryDetail.from_json(json)
# print the JSON string representation of the object
print(MultilingualVersionhistoryDetail.to_json())

# convert the object into a dict
multilingual_versionhistory_detail_dict = multilingual_versionhistory_detail_instance.to_dict()
# create an instance of MultilingualVersionhistoryDetail from a dict
multilingual_versionhistory_detail_form_dict = multilingual_versionhistory_detail.from_dict(multilingual_versionhistory_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


