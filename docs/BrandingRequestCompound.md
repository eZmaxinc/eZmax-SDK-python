# BrandingRequestCompound

A Branding Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_branding_id** | **int** | The unique ID of the Branding | [optional] 
**obj_branding_description** | [**MultilingualBrandingDescription**](MultilingualBrandingDescription.md) |  | 
**e_branding_logo** | [**FieldEBrandingLogo**](FieldEBrandingLogo.md) |  | 
**s_branding_base64** | **bytearray** | The Base64 encoded binary content of the branding logo. This need to match image type selected in eBrandingLogo if you supply an image. If you select &#39;Default&#39;, the logo will be deleted and the default one will be used. | [optional] 
**i_branding_colortext** | **int** | The color of the text. This is a RGB color converted into integer | 
**i_branding_colortextlinkbox** | **int** | The color of the text in the link box. This is a RGB color converted into integer | 
**i_branding_colortextbutton** | **int** | The color of the text in the button. This is a RGB color converted into integer | 
**i_branding_colorbackground** | **int** | The color of the background. This is a RGB color converted into integer | 
**i_branding_colorbackgroundbutton** | **int** | The color of the background of the button. This is a RGB color converted into integer | 
**i_branding_colorbackgroundsmallbox** | **int** | The color of the background of the small box. This is a RGB color converted into integer | 
**s_branding_name** | **str** | The name of the Branding  This value will only be set if you wish to overwrite the default name. If you want to keep the default name, leave this property empty | [optional] 
**s_email_address** | **str** | The email address. | [optional] 
**b_branding_isactive** | **bool** | Whether the Branding is active or not | 

## Example

```python
from eZmaxApi.models.branding_request_compound import BrandingRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingRequestCompound from a JSON string
branding_request_compound_instance = BrandingRequestCompound.from_json(json)
# print the JSON string representation of the object
print BrandingRequestCompound.to_json()

# convert the object into a dict
branding_request_compound_dict = branding_request_compound_instance.to_dict()
# create an instance of BrandingRequestCompound from a dict
branding_request_compound_form_dict = branding_request_compound.from_dict(branding_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


