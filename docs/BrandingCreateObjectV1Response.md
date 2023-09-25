# BrandingCreateObjectV1Response

Response for POST /1/object/branding

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BrandingCreateObjectV1ResponseMPayload**](BrandingCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.branding_create_object_v1_response import BrandingCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingCreateObjectV1Response from a JSON string
branding_create_object_v1_response_instance = BrandingCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print BrandingCreateObjectV1Response.to_json()

# convert the object into a dict
branding_create_object_v1_response_dict = branding_create_object_v1_response_instance.to_dict()
# create an instance of BrandingCreateObjectV1Response from a dict
branding_create_object_v1_response_form_dict = branding_create_object_v1_response.from_dict(branding_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


