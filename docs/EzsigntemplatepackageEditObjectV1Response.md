# EzsigntemplatepackageEditObjectV1Response

Response for PUT /1/object/ezsigntemplatepackage/{pkiEzsigntemplatepackageID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackage_edit_object_v1_response import EzsigntemplatepackageEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackageEditObjectV1Response from a JSON string
ezsigntemplatepackage_edit_object_v1_response_instance = EzsigntemplatepackageEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackageEditObjectV1Response.to_json())

# convert the object into a dict
ezsigntemplatepackage_edit_object_v1_response_dict = ezsigntemplatepackage_edit_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplatepackageEditObjectV1Response from a dict
ezsigntemplatepackage_edit_object_v1_response_from_dict = EzsigntemplatepackageEditObjectV1Response.from_dict(ezsigntemplatepackage_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


