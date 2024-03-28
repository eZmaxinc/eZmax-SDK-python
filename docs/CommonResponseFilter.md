# CommonResponseFilter

Definition of Filters for getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_auto_type** | **Dict[str, str]** | List of filters that can be used in *sFilter* (Automatic types) | [optional] 
**a_auto_type_having** | **Dict[str, str]** | List of computed filters that can be used in *sFilter* (Automatic types) | [optional] 
**a_enum** | **Dict[str, Dict[str, str]]** | List of filters that can be used in *sFilter* (Enum types) | [optional] 

## Example

```python
from eZmaxApi.models.common_response_filter import CommonResponseFilter

# TODO update the JSON string below
json = "{}"
# create an instance of CommonResponseFilter from a JSON string
common_response_filter_instance = CommonResponseFilter.from_json(json)
# print the JSON string representation of the object
print(CommonResponseFilter.to_json())

# convert the object into a dict
common_response_filter_dict = common_response_filter_instance.to_dict()
# create an instance of CommonResponseFilter from a dict
common_response_filter_form_dict = common_response_filter.from_dict(common_response_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


