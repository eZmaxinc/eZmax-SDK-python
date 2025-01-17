# BrandingResponseCompoundV3

A Branding Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_branding_logourl** | **str** | The url of the picture used as logo in the Branding | [optional] 
**s_branding_logoemailurl** | **str** | The url of the picture used in email as logo in the Branding | [optional] 
**s_branding_logointerfaceurl** | **str** | The url of the picture used as logo in the Branding | [optional] 

## Example

```python
from eZmaxApi.models.branding_response_compound_v3 import BrandingResponseCompoundV3

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingResponseCompoundV3 from a JSON string
branding_response_compound_v3_instance = BrandingResponseCompoundV3.from_json(json)
# print the JSON string representation of the object
print(BrandingResponseCompoundV3.to_json())

# convert the object into a dict
branding_response_compound_v3_dict = branding_response_compound_v3_instance.to_dict()
# create an instance of BrandingResponseCompoundV3 from a dict
branding_response_compound_v3_from_dict = BrandingResponseCompoundV3.from_dict(branding_response_compound_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


