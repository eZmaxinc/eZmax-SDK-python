# DisclosureGetListV1Response

Response for GET /1/object/disclosure/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**DisclosureGetListV1ResponseMPayload**](DisclosureGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.disclosure_get_list_v1_response import DisclosureGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DisclosureGetListV1Response from a JSON string
disclosure_get_list_v1_response_instance = DisclosureGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(DisclosureGetListV1Response.to_json())

# convert the object into a dict
disclosure_get_list_v1_response_dict = disclosure_get_list_v1_response_instance.to_dict()
# create an instance of DisclosureGetListV1Response from a dict
disclosure_get_list_v1_response_from_dict = DisclosureGetListV1Response.from_dict(disclosure_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


