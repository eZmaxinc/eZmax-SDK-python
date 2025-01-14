# BrandingGetObjectV3ResponseMPayload

Payload for GET /3/object/branding/{pkiBrandingID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_branding** | [**BrandingResponseCompoundV3**](BrandingResponseCompoundV3.md) |  | 

## Example

```python
from eZmaxApi.models.branding_get_object_v3_response_m_payload import BrandingGetObjectV3ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingGetObjectV3ResponseMPayload from a JSON string
branding_get_object_v3_response_m_payload_instance = BrandingGetObjectV3ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(BrandingGetObjectV3ResponseMPayload.to_json())

# convert the object into a dict
branding_get_object_v3_response_m_payload_dict = branding_get_object_v3_response_m_payload_instance.to_dict()
# create an instance of BrandingGetObjectV3ResponseMPayload from a dict
branding_get_object_v3_response_m_payload_from_dict = BrandingGetObjectV3ResponseMPayload.from_dict(branding_get_object_v3_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


