# EzmaxpartnerproductstageGetListV1Response

Response for GET /1/object/ezmaxpartnerproductstage/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzmaxpartnerproductstageGetListV1ResponseMPayload**](EzmaxpartnerproductstageGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezmaxpartnerproductstage_get_list_v1_response import EzmaxpartnerproductstageGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxpartnerproductstageGetListV1Response from a JSON string
ezmaxpartnerproductstage_get_list_v1_response_instance = EzmaxpartnerproductstageGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(EzmaxpartnerproductstageGetListV1Response.to_json())

# convert the object into a dict
ezmaxpartnerproductstage_get_list_v1_response_dict = ezmaxpartnerproductstage_get_list_v1_response_instance.to_dict()
# create an instance of EzmaxpartnerproductstageGetListV1Response from a dict
ezmaxpartnerproductstage_get_list_v1_response_from_dict = EzmaxpartnerproductstageGetListV1Response.from_dict(ezmaxpartnerproductstage_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


