# EzsigntemplatesignatureEditObjectV3Response

Response for PUT /3/object/ezsigntemplatesignature/{pkiEzsigntemplatesignatureID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplatesignature_edit_object_v3_response import EzsigntemplatesignatureEditObjectV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignatureEditObjectV3Response from a JSON string
ezsigntemplatesignature_edit_object_v3_response_instance = EzsigntemplatesignatureEditObjectV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignatureEditObjectV3Response.to_json())

# convert the object into a dict
ezsigntemplatesignature_edit_object_v3_response_dict = ezsigntemplatesignature_edit_object_v3_response_instance.to_dict()
# create an instance of EzsigntemplatesignatureEditObjectV3Response from a dict
ezsigntemplatesignature_edit_object_v3_response_from_dict = EzsigntemplatesignatureEditObjectV3Response.from_dict(ezsigntemplatesignature_edit_object_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


