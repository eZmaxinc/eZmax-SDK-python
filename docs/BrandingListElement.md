# BrandingListElement

A Branding List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_branding_id** | **int** | The unique ID of the Branding | 
**s_branding_description_x** | **str** | The Description of the Branding in the language of the requester | 
**i_branding_colortext** | **int** | The color of the text. This is a RGB color converted into integer | 
**i_branding_colortextlinkbox** | **int** | The color of the text in the link box. This is a RGB color converted into integer | 
**i_branding_colortextbutton** | **int** | The color of the text in the button. This is a RGB color converted into integer | 
**i_branding_colorbackground** | **int** | The color of the background. This is a RGB color converted into integer | 
**i_branding_colorbackgroundbutton** | **int** | The color of the background of the button. This is a RGB color converted into integer | 
**i_branding_colorbackgroundsmallbox** | **int** | The color of the background of the small box. This is a RGB color converted into integer | 
**b_branding_isactive** | **bool** | Whether the Branding is active or not | 

## Example

```python
from eZmaxApi.models.branding_list_element import BrandingListElement

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingListElement from a JSON string
branding_list_element_instance = BrandingListElement.from_json(json)
# print the JSON string representation of the object
print BrandingListElement.to_json()

# convert the object into a dict
branding_list_element_dict = branding_list_element_instance.to_dict()
# create an instance of BrandingListElement from a dict
branding_list_element_form_dict = branding_list_element.from_dict(branding_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


