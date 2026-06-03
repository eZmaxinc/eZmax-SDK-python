# EzmaxpartnerGetObjectV2Response

Response for GET /1/object/ezmaxpartner/{pkiEzmaxpartnerID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzmaxpartnerGetObjectV2ResponseMPayload**](EzmaxpartnerGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezmaxpartner_get_object_v2_response import EzmaxpartnerGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxpartnerGetObjectV2Response from a JSON string
ezmaxpartner_get_object_v2_response_instance = EzmaxpartnerGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzmaxpartnerGetObjectV2Response.to_json())

# convert the object into a dict
ezmaxpartner_get_object_v2_response_dict = ezmaxpartner_get_object_v2_response_instance.to_dict()
# create an instance of EzmaxpartnerGetObjectV2Response from a dict
ezmaxpartner_get_object_v2_response_from_dict = EzmaxpartnerGetObjectV2Response.from_dict(ezmaxpartner_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


