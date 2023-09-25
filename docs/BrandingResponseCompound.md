# BrandingResponseCompound

A Branding Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_branding_id** | **int** | The unique ID of the Branding | 
**fki_email_id** | **int** | The unique ID of the Email | [optional] 
**obj_branding_description** | [**MultilingualBrandingDescription**](MultilingualBrandingDescription.md) |  | 
**s_branding_description_x** | **str** | The Description of the Branding in the language of the requester | 
**s_branding_name** | **str** | The name of the Branding  This value will only be set if you wish to overwrite the default name. If you want to keep the default name, leave this property empty | [optional] 
**s_email_address** | **str** | The email address. | [optional] 
**e_branding_logo** | [**FieldEBrandingLogo**](FieldEBrandingLogo.md) |  | 
**i_branding_colortext** | **int** | The color of the text. This is a RGB color converted into integer | 
**i_branding_colortextlinkbox** | **int** | The color of the text in the link box. This is a RGB color converted into integer | 
**i_branding_colortextbutton** | **int** | The color of the text in the button. This is a RGB color converted into integer | 
**i_branding_colorbackground** | **int** | The color of the background. This is a RGB color converted into integer | 
**i_branding_colorbackgroundbutton** | **int** | The color of the background of the button. This is a RGB color converted into integer | 
**i_branding_colorbackgroundsmallbox** | **int** | The color of the background of the small box. This is a RGB color converted into integer | 
**b_branding_isactive** | **bool** | Whether the Branding is active or not | 
**s_branding_logourl** | **str** | The url of the picture used as logo in the Branding | [optional] 

## Example

```python
from eZmaxApi.models.branding_response_compound import BrandingResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingResponseCompound from a JSON string
branding_response_compound_instance = BrandingResponseCompound.from_json(json)
# print the JSON string representation of the object
print BrandingResponseCompound.to_json()

# convert the object into a dict
branding_response_compound_dict = branding_response_compound_instance.to_dict()
# create an instance of BrandingResponseCompound from a dict
branding_response_compound_form_dict = branding_response_compound.from_dict(branding_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


