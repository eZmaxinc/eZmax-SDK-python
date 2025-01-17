# BrandingGetListV1Response

Response for GET /1/object/branding/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**BrandingGetListV1ResponseMPayload**](BrandingGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.branding_get_list_v1_response import BrandingGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of BrandingGetListV1Response from a JSON string
branding_get_list_v1_response_instance = BrandingGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(BrandingGetListV1Response.to_json())

# convert the object into a dict
branding_get_list_v1_response_dict = branding_get_list_v1_response_instance.to_dict()
# create an instance of BrandingGetListV1Response from a dict
branding_get_list_v1_response_from_dict = BrandingGetListV1Response.from_dict(branding_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


