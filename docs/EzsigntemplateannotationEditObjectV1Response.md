# EzsigntemplateannotationEditObjectV1Response

Response for PUT /1/object/ezsigntemplateannotation/{pkiEzsigntemplateannotationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplateannotation_edit_object_v1_response import EzsigntemplateannotationEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateannotationEditObjectV1Response from a JSON string
ezsigntemplateannotation_edit_object_v1_response_instance = EzsigntemplateannotationEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateannotationEditObjectV1Response.to_json())

# convert the object into a dict
ezsigntemplateannotation_edit_object_v1_response_dict = ezsigntemplateannotation_edit_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplateannotationEditObjectV1Response from a dict
ezsigntemplateannotation_edit_object_v1_response_from_dict = EzsigntemplateannotationEditObjectV1Response.from_dict(ezsigntemplateannotation_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


