# BrandingCreateObjectV2ResponseMPayload

Payload for POST /2/object/branding

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_branding_id** | **List[int]** | An array of unique IDs representing the object that were requested to be created.  They are returned in the same order as the array containing the objects to be created that was sent in the request. | 

## Example

```python
from eZmaxApi.models.branding_create_object_v2_response_m_payload import BrandingCreateObjectV2ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingCreateObjectV2ResponseMPayload from a JSON string
branding_create_object_v2_response_m_payload_instance = BrandingCreateObjectV2ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(BrandingCreateObjectV2ResponseMPayload.to_json())

# convert the object into a dict
branding_create_object_v2_response_m_payload_dict = branding_create_object_v2_response_m_payload_instance.to_dict()
# create an instance of BrandingCreateObjectV2ResponseMPayload from a dict
branding_create_object_v2_response_m_payload_from_dict = BrandingCreateObjectV2ResponseMPayload.from_dict(branding_create_object_v2_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


