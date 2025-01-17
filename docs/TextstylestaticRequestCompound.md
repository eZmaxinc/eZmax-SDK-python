# TextstylestaticRequestCompound

A Textstylestatic Object and children

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
from eZmaxApi.models.textstylestatic_request_compound import TextstylestaticRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of TextstylestaticRequestCompound from a JSON string
textstylestatic_request_compound_instance = TextstylestaticRequestCompound.from_json(json)
# print the JSON string representation of the object
print(TextstylestaticRequestCompound.to_json())

# convert the object into a dict
textstylestatic_request_compound_dict = textstylestatic_request_compound_instance.to_dict()
# create an instance of TextstylestaticRequestCompound from a dict
textstylestatic_request_compound_from_dict = TextstylestaticRequestCompound.from_dict(textstylestatic_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


