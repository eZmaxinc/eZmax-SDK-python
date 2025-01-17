# BrandingGetObjectV3Response

Response for GET /3/object/branding/{pkiBrandingID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BrandingGetObjectV3ResponseMPayload**](BrandingGetObjectV3ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.branding_get_object_v3_response import BrandingGetObjectV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingGetObjectV3Response from a JSON string
branding_get_object_v3_response_instance = BrandingGetObjectV3Response.from_json(json)
# print the JSON string representation of the object
print(BrandingGetObjectV3Response.to_json())

# convert the object into a dict
branding_get_object_v3_response_dict = branding_get_object_v3_response_instance.to_dict()
# create an instance of BrandingGetObjectV3Response from a dict
branding_get_object_v3_response_from_dict = BrandingGetObjectV3Response.from_dict(branding_get_object_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


