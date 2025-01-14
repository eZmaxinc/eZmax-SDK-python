# TextstylestaticRequest

A Textstylestatic Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_font_id** | **int** | The unique ID of the Font | 
**b_textstylestatic_bold** | **bool** | Whether the Textstylestatic is Bold or not | 
**b_textstylestatic_underline** | **bool** | Whether the Textstylestatic is Underline or not | 
**b_textstylestatic_italic** | **bool** | Whether the Textstylestatic is Italic or not | 
**b_textstylestatic_strikethrough** | **bool** | Whether the Textstylestatic is Strikethrough or not | 
**i_textstylestatic_fontcolor** | **int** | The int32 representation of the Fontcolor. For example, RGB color #39435B would be 3752795 | 
**i_textstylestatic_size** | **int** | The Size for the Font of the Textstylestatic | 

## Example

```python
from eZmaxApi.models.textstylestatic_request import TextstylestaticRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TextstylestaticRequest from a JSON string
textstylestatic_request_instance = TextstylestaticRequest.from_json(json)
# print the JSON string representation of the object
print(TextstylestaticRequest.to_json())

# convert the object into a dict
textstylestatic_request_dict = textstylestatic_request_instance.to_dict()
# create an instance of TextstylestaticRequest from a dict
textstylestatic_request_from_dict = TextstylestaticRequest.from_dict(textstylestatic_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


