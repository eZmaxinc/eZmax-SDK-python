# BrandingEditObjectV1Response

Response for PUT /1/object/branding/{pkiBrandingID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.branding_edit_object_v1_response import BrandingEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingEditObjectV1Response from a JSON string
branding_edit_object_v1_response_instance = BrandingEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print BrandingEditObjectV1Response.to_json()

# convert the object into a dict
branding_edit_object_v1_response_dict = branding_edit_object_v1_response_instance.to_dict()
# create an instance of BrandingEditObjectV1Response from a dict
branding_edit_object_v1_response_form_dict = branding_edit_object_v1_response.from_dict(branding_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


