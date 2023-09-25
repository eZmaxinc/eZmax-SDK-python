# TextstylestaticResponse

A Textstylestatic Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_textstylestatic_id** | **int** | The unique ID of the Textstylestatic | [optional] 
**fki_font_id** | **int** | The unique ID of the Font | 
**b_textstylestatic_bold** | **bool** | Whether the Textstylestatic is Bold or not | 
**b_textstylestatic_underline** | **bool** | Whether the Textstylestatic is Underline or not | 
**b_textstylestatic_italic** | **bool** | Whether the Textstylestatic is Italic or not | 
**b_textstylestatic_strikethrough** | **bool** | Whether the Textstylestatic is Strikethrough or not | 
**i_textstylestatic_fontcolor** | **int** | The int32 representation of the Fontcolor. For example, RGB color #39435B would be 3752795 | 
**i_textstylestatic_size** | **int** | The Size for the Font of the Textstylestatic | 

## Example

```python
from eZmaxApi.models.textstylestatic_response import TextstylestaticResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TextstylestaticResponse from a JSON string
textstylestatic_response_instance = TextstylestaticResponse.from_json(json)
# print the JSON string representation of the object
print TextstylestaticResponse.to_json()

# convert the object into a dict
textstylestatic_response_dict = textstylestatic_response_instance.to_dict()
# create an instance of TextstylestaticResponse from a dict
textstylestatic_response_form_dict = textstylestatic_response.from_dict(textstylestatic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


