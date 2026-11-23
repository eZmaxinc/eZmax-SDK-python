# EzmaxpartnerproductstageSubscribeV1Response

Response for POST /1/object/ezmaxpartnerproductstage/{pkiEzmaxpartnerproductstageID}/subscribe

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezmaxpartnerproductstage_subscribe_v1_response import EzmaxpartnerproductstageSubscribeV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxpartnerproductstageSubscribeV1Response from a JSON string
ezmaxpartnerproductstage_subscribe_v1_response_instance = EzmaxpartnerproductstageSubscribeV1Response.from_json(json)
# print the JSON string representation of the object
print(EzmaxpartnerproductstageSubscribeV1Response.to_json())

# convert the object into a dict
ezmaxpartnerproductstage_subscribe_v1_response_dict = ezmaxpartnerproductstage_subscribe_v1_response_instance.to_dict()
# create an instance of EzmaxpartnerproductstageSubscribeV1Response from a dict
ezmaxpartnerproductstage_subscribe_v1_response_from_dict = EzmaxpartnerproductstageSubscribeV1Response.from_dict(ezmaxpartnerproductstage_subscribe_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


