# EzsigntemplateDeleteObjectV1Response

Response for DELETE /1/object/ezsigntemplate/{pkiEzsigntemplateID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplate_delete_object_v1_response import EzsigntemplateDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateDeleteObjectV1Response from a JSON string
ezsigntemplate_delete_object_v1_response_instance = EzsigntemplateDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateDeleteObjectV1Response.to_json())

# convert the object into a dict
ezsigntemplate_delete_object_v1_response_dict = ezsigntemplate_delete_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplateDeleteObjectV1Response from a dict
ezsigntemplate_delete_object_v1_response_from_dict = EzsigntemplateDeleteObjectV1Response.from_dict(ezsigntemplate_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


