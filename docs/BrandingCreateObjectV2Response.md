# BrandingCreateObjectV2Response

Response for POST /2/object/branding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**BrandingCreateObjectV2ResponseMPayload**](BrandingCreateObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.branding_create_object_v2_response import BrandingCreateObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingCreateObjectV2Response from a JSON string
branding_create_object_v2_response_instance = BrandingCreateObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(BrandingCreateObjectV2Response.to_json())

# convert the object into a dict
branding_create_object_v2_response_dict = branding_create_object_v2_response_instance.to_dict()
# create an instance of BrandingCreateObjectV2Response from a dict
branding_create_object_v2_response_from_dict = BrandingCreateObjectV2Response.from_dict(branding_create_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


