# CustomWordPositionOccurenceResponse

A Word Position Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_page** | **int** | The page where the word occurence was found | [optional] 
**i_x** | **int** | The X coordinate (Horizontal) where the Word occurence was found.  Coordinate is calculated at 100dpi (dot per inch). | [optional] 
**i_y** | **int** | The Y coordinate (Vertical) where the Word occurence was found.  Coordinate is calculated at 100dpi (dot per inch). | [optional] 

## Example

```python
from eZmaxApi.models.custom_word_position_occurence_response import CustomWordPositionOccurenceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomWordPositionOccurenceResponse from a JSON string
custom_word_position_occurence_response_instance = CustomWordPositionOccurenceResponse.from_json(json)
# print the JSON string representation of the object
print CustomWordPositionOccurenceResponse.to_json()

# convert the object into a dict
custom_word_position_occurence_response_dict = custom_word_position_occurence_response_instance.to_dict()
# create an instance of CustomWordPositionOccurenceResponse from a dict
custom_word_position_occurence_response_form_dict = custom_word_position_occurence_response.from_dict(custom_word_position_occurence_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


