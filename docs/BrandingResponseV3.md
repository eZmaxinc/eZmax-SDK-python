# BrandingResponseV3

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
**e_branding_alignlogo** | [**FieldEBrandingAlignlogo**](FieldEBrandingAlignlogo.md) |  | 
**i_branding_color** | **int** | The primary color. This is a RGB color converted into integer | 
**b_branding_isactive** | **bool** | Whether the Branding is active or not | 

## Example

```python
from eZmaxApi.models.branding_response_v3 import BrandingResponseV3

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingResponseV3 from a JSON string
branding_response_v3_instance = BrandingResponseV3.from_json(json)
# print the JSON string representation of the object
print(BrandingResponseV3.to_json())

# convert the object into a dict
branding_response_v3_dict = branding_response_v3_instance.to_dict()
# create an instance of BrandingResponseV3 from a dict
branding_response_v3_from_dict = BrandingResponseV3.from_dict(branding_response_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


