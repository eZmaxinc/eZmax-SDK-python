# CustomWordPositionWordResponse

A Word Position Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_word** | **str** | The searched word | 
**a_obj_word_position_occurence** | [**List[CustomWordPositionOccurenceResponse]**](CustomWordPositionOccurenceResponse.md) | The found occurences for the seached word | 

## Example

```python
from eZmaxApi.models.custom_word_position_word_response import CustomWordPositionWordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomWordPositionWordResponse from a JSON string
custom_word_position_word_response_instance = CustomWordPositionWordResponse.from_json(json)
# print the JSON string representation of the object
print(CustomWordPositionWordResponse.to_json())

# convert the object into a dict
custom_word_position_word_response_dict = custom_word_position_word_response_instance.to_dict()
# create an instance of CustomWordPositionWordResponse from a dict
custom_word_position_word_response_form_dict = custom_word_position_word_response.from_dict(custom_word_position_word_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


