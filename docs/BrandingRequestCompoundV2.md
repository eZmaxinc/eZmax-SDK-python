# BrandingRequestCompoundV2

A Branding Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_branding_id** | **int** | The unique ID of the Branding | [optional] 
**obj_branding_description** | [**MultilingualBrandingDescription**](MultilingualBrandingDescription.md) |  | 
**e_branding_logo** | [**FieldEBrandingLogo**](FieldEBrandingLogo.md) |  | 
**e_branding_alignlogo** | [**FieldEBrandingAlignlogo**](FieldEBrandingAlignlogo.md) |  | [optional] 
**s_branding_base64** | **bytearray** | The Base64 encoded binary content of the branding logo. This need to match image type selected in eBrandingLogo if you supply an image. If you select &#39;Default&#39;, the logo will be deleted and the default one will be used. | [optional] 
**i_branding_color** | **int** | The primary color. This is a RGB color converted into integer | 
**s_branding_name** | **str** | The name of the Branding  This value will only be set if you wish to overwrite the default name. If you want to keep the default name, leave this property empty | [optional] 
**s_email_address** | **str** | The email address. | [optional] 
**b_branding_isactive** | **bool** | Whether the Branding is active or not | 

## Example

```python
from eZmaxApi.models.branding_request_compound_v2 import BrandingRequestCompoundV2

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingRequestCompoundV2 from a JSON string
branding_request_compound_v2_instance = BrandingRequestCompoundV2.from_json(json)
# print the JSON string representation of the object
print(BrandingRequestCompoundV2.to_json())

# convert the object into a dict
branding_request_compound_v2_dict = branding_request_compound_v2_instance.to_dict()
# create an instance of BrandingRequestCompoundV2 from a dict
branding_request_compound_v2_from_dict = BrandingRequestCompoundV2.from_dict(branding_request_compound_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


