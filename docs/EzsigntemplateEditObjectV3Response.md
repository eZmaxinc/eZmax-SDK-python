# EzsigntemplateEditObjectV3Response

Response for PUT /3/object/ezsigntemplate/{pkiEzsigntemplateID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplate_edit_object_v3_response import EzsigntemplateEditObjectV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateEditObjectV3Response from a JSON string
ezsigntemplate_edit_object_v3_response_instance = EzsigntemplateEditObjectV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateEditObjectV3Response.to_json())

# convert the object into a dict
ezsigntemplate_edit_object_v3_response_dict = ezsigntemplate_edit_object_v3_response_instance.to_dict()
# create an instance of EzsigntemplateEditObjectV3Response from a dict
ezsigntemplate_edit_object_v3_response_from_dict = EzsigntemplateEditObjectV3Response.from_dict(ezsigntemplate_edit_object_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


