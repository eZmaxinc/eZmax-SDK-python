# InscriptiontempGetListV1Response

Response for GET /1/object/inscriptiontemp/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**InscriptiontempGetListV1ResponseMPayload**](InscriptiontempGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptiontemp_get_list_v1_response import InscriptiontempGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptiontempGetListV1Response from a JSON string
inscriptiontemp_get_list_v1_response_instance = InscriptiontempGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(InscriptiontempGetListV1Response.to_json())

# convert the object into a dict
inscriptiontemp_get_list_v1_response_dict = inscriptiontemp_get_list_v1_response_instance.to_dict()
# create an instance of InscriptiontempGetListV1Response from a dict
inscriptiontemp_get_list_v1_response_from_dict = InscriptiontempGetListV1Response.from_dict(inscriptiontemp_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


