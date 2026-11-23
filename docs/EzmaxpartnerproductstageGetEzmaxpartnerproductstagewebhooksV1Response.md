# EzmaxpartnerproductstageGetEzmaxpartnerproductstagewebhooksV1Response

Response for GET /1/object/ezmaxpartnerproductstage/{pkiEzmaxpartnerproductstageID}/getEzmaxpartnerproductstagewebhooks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzmaxpartnerproductstageGetEzmaxpartnerproductstagewebhooksV1ResponseMPayload**](EzmaxpartnerproductstageGetEzmaxpartnerproductstagewebhooksV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezmaxpartnerproductstage_get_ezmaxpartnerproductstagewebhooks_v1_response import EzmaxpartnerproductstageGetEzmaxpartnerproductstagewebhooksV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxpartnerproductstageGetEzmaxpartnerproductstagewebhooksV1Response from a JSON string
ezmaxpartnerproductstage_get_ezmaxpartnerproductstagewebhooks_v1_response_instance = EzmaxpartnerproductstageGetEzmaxpartnerproductstagewebhooksV1Response.from_json(json)
# print the JSON string representation of the object
print(EzmaxpartnerproductstageGetEzmaxpartnerproductstagewebhooksV1Response.to_json())

# convert the object into a dict
ezmaxpartnerproductstage_get_ezmaxpartnerproductstagewebhooks_v1_response_dict = ezmaxpartnerproductstage_get_ezmaxpartnerproductstagewebhooks_v1_response_instance.to_dict()
# create an instance of EzmaxpartnerproductstageGetEzmaxpartnerproductstagewebhooksV1Response from a dict
ezmaxpartnerproductstage_get_ezmaxpartnerproductstagewebhooks_v1_response_from_dict = EzmaxpartnerproductstageGetEzmaxpartnerproductstagewebhooksV1Response.from_dict(ezmaxpartnerproductstage_get_ezmaxpartnerproductstagewebhooks_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


