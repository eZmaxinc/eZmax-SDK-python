# EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Response

Response for POST /1/object/ezsigntemplatepublic/getEzsigntemplatepublicDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1ResponseMPayload**](EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepublic_get_ezsigntemplatepublic_details_v1_response import EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Response from a JSON string
ezsigntemplatepublic_get_ezsigntemplatepublic_details_v1_response_instance = EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Response.to_json())

# convert the object into a dict
ezsigntemplatepublic_get_ezsigntemplatepublic_details_v1_response_dict = ezsigntemplatepublic_get_ezsigntemplatepublic_details_v1_response_instance.to_dict()
# create an instance of EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Response from a dict
ezsigntemplatepublic_get_ezsigntemplatepublic_details_v1_response_from_dict = EzsigntemplatepublicGetEzsigntemplatepublicDetailsV1Response.from_dict(ezsigntemplatepublic_get_ezsigntemplatepublic_details_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


