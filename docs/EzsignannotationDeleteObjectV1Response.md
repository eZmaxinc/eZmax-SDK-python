# EzsignannotationDeleteObjectV1Response

Response for DELETE /1/object/ezsignannotation/{pkiEzsignannotationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignannotation_delete_object_v1_response import EzsignannotationDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignannotationDeleteObjectV1Response from a JSON string
ezsignannotation_delete_object_v1_response_instance = EzsignannotationDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignannotationDeleteObjectV1Response.to_json())

# convert the object into a dict
ezsignannotation_delete_object_v1_response_dict = ezsignannotation_delete_object_v1_response_instance.to_dict()
# create an instance of EzsignannotationDeleteObjectV1Response from a dict
ezsignannotation_delete_object_v1_response_from_dict = EzsignannotationDeleteObjectV1Response.from_dict(ezsignannotation_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


