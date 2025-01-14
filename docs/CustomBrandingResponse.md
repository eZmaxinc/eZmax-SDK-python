# CustomBrandingResponse

A Custom Branding Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_branding_color** | **int** | The primary color. This is a RGB color converted into integer | 
**s_branding_logointerfaceurl** | **str** | The url of the picture used as logo in the Branding | 

## Example

```python
from eZmaxApi.models.custom_branding_response import CustomBrandingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomBrandingResponse from a JSON string
custom_branding_response_instance = CustomBrandingResponse.from_json(json)
# print the JSON string representation of the object
print(CustomBrandingResponse.to_json())

# convert the object into a dict
custom_branding_response_dict = custom_branding_response_instance.to_dict()
# create an instance of CustomBrandingResponse from a dict
custom_branding_response_from_dict = CustomBrandingResponse.from_dict(custom_branding_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


