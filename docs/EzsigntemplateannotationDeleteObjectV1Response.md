# EzsigntemplateannotationDeleteObjectV1Response

Response for DELETE /1/object/ezsigntemplateannotation/{pkiEzsigntemplateannotationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplateannotation_delete_object_v1_response import EzsigntemplateannotationDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateannotationDeleteObjectV1Response from a JSON string
ezsigntemplateannotation_delete_object_v1_response_instance = EzsigntemplateannotationDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateannotationDeleteObjectV1Response.to_json())

# convert the object into a dict
ezsigntemplateannotation_delete_object_v1_response_dict = ezsigntemplateannotation_delete_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplateannotationDeleteObjectV1Response from a dict
ezsigntemplateannotation_delete_object_v1_response_from_dict = EzsigntemplateannotationDeleteObjectV1Response.from_dict(ezsigntemplateannotation_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


