# EzsigntemplateformfieldgroupEditObjectV1Response

Response for PUT /1/object/ezsigntemplateformfieldgroup/{pkiEzsigntemplateformfieldgroupID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplateformfieldgroup_edit_object_v1_response import EzsigntemplateformfieldgroupEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateformfieldgroupEditObjectV1Response from a JSON string
ezsigntemplateformfieldgroup_edit_object_v1_response_instance = EzsigntemplateformfieldgroupEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateformfieldgroupEditObjectV1Response.to_json())

# convert the object into a dict
ezsigntemplateformfieldgroup_edit_object_v1_response_dict = ezsigntemplateformfieldgroup_edit_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplateformfieldgroupEditObjectV1Response from a dict
ezsigntemplateformfieldgroup_edit_object_v1_response_from_dict = EzsigntemplateformfieldgroupEditObjectV1Response.from_dict(ezsigntemplateformfieldgroup_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


