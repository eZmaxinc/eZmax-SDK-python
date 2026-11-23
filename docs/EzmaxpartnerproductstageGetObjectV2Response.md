# EzmaxpartnerproductstageGetObjectV2Response

Response for GET /2/object/ezmaxpartnerproductstage/{pkiEzmaxpartnerproductstageID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzmaxpartnerproductstageGetObjectV2ResponseMPayload**](EzmaxpartnerproductstageGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezmaxpartnerproductstage_get_object_v2_response import EzmaxpartnerproductstageGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxpartnerproductstageGetObjectV2Response from a JSON string
ezmaxpartnerproductstage_get_object_v2_response_instance = EzmaxpartnerproductstageGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzmaxpartnerproductstageGetObjectV2Response.to_json())

# convert the object into a dict
ezmaxpartnerproductstage_get_object_v2_response_dict = ezmaxpartnerproductstage_get_object_v2_response_instance.to_dict()
# create an instance of EzmaxpartnerproductstageGetObjectV2Response from a dict
ezmaxpartnerproductstage_get_object_v2_response_from_dict = EzmaxpartnerproductstageGetObjectV2Response.from_dict(ezmaxpartnerproductstage_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


