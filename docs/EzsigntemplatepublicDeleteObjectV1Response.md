# EzsigntemplatepublicDeleteObjectV1Response

Response for DELETE /1/object/ezsigntemplatepublic/{pkiEzsigntemplatepublicID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplatepublic_delete_object_v1_response import EzsigntemplatepublicDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepublicDeleteObjectV1Response from a JSON string
ezsigntemplatepublic_delete_object_v1_response_instance = EzsigntemplatepublicDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepublicDeleteObjectV1Response.to_json())

# convert the object into a dict
ezsigntemplatepublic_delete_object_v1_response_dict = ezsigntemplatepublic_delete_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplatepublicDeleteObjectV1Response from a dict
ezsigntemplatepublic_delete_object_v1_response_from_dict = EzsigntemplatepublicDeleteObjectV1Response.from_dict(ezsigntemplatepublic_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


