# InscriptionGetObjectV2Response

Response for GET /2/object/inscription/{pkiInscriptionID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InscriptionGetObjectV2ResponseMPayload**](InscriptionGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.inscription_get_object_v2_response import InscriptionGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptionGetObjectV2Response from a JSON string
inscription_get_object_v2_response_instance = InscriptionGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(InscriptionGetObjectV2Response.to_json())

# convert the object into a dict
inscription_get_object_v2_response_dict = inscription_get_object_v2_response_instance.to_dict()
# create an instance of InscriptionGetObjectV2Response from a dict
inscription_get_object_v2_response_from_dict = InscriptionGetObjectV2Response.from_dict(inscription_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


