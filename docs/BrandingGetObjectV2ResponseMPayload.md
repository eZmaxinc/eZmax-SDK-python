# BrandingGetObjectV2ResponseMPayload

Payload for GET /2/object/branding/{pkiBrandingID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_branding** | [**BrandingResponseCompound**](BrandingResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.branding_get_object_v2_response_m_payload import BrandingGetObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingGetObjectV2ResponseMPayload from a JSON string
branding_get_object_v2_response_m_payload_instance = BrandingGetObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print BrandingGetObjectV2ResponseMPayload.to_json()

# convert the object into a dict
branding_get_object_v2_response_m_payload_dict = branding_get_object_v2_response_m_payload_instance.to_dict()
# create an instance of BrandingGetObjectV2ResponseMPayload from a dict
branding_get_object_v2_response_m_payload_form_dict = branding_get_object_v2_response_m_payload.from_dict(branding_get_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


