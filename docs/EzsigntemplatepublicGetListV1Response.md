# EzsigntemplatepublicGetListV1Response

Response for GET /1/object/ezsigntemplatepublic/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatepublicGetListV1ResponseMPayload**](EzsigntemplatepublicGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepublic_get_list_v1_response import EzsigntemplatepublicGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepublicGetListV1Response from a JSON string
ezsigntemplatepublic_get_list_v1_response_instance = EzsigntemplatepublicGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepublicGetListV1Response.to_json())

# convert the object into a dict
ezsigntemplatepublic_get_list_v1_response_dict = ezsigntemplatepublic_get_list_v1_response_instance.to_dict()
# create an instance of EzsigntemplatepublicGetListV1Response from a dict
ezsigntemplatepublic_get_list_v1_response_from_dict = EzsigntemplatepublicGetListV1Response.from_dict(ezsigntemplatepublic_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


