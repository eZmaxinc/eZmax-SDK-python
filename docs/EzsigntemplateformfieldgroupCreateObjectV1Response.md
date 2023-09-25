# EzsigntemplateformfieldgroupCreateObjectV1Response

Response for POST /1/object/ezsigntemplateformfieldgroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplateformfieldgroupCreateObjectV1ResponseMPayload**](EzsigntemplateformfieldgroupCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplateformfieldgroup_create_object_v1_response import EzsigntemplateformfieldgroupCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateformfieldgroupCreateObjectV1Response from a JSON string
ezsigntemplateformfieldgroup_create_object_v1_response_instance = EzsigntemplateformfieldgroupCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print EzsigntemplateformfieldgroupCreateObjectV1Response.to_json()

# convert the object into a dict
ezsigntemplateformfieldgroup_create_object_v1_response_dict = ezsigntemplateformfieldgroup_create_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplateformfieldgroupCreateObjectV1Response from a dict
ezsigntemplateformfieldgroup_create_object_v1_response_form_dict = ezsigntemplateformfieldgroup_create_object_v1_response.from_dict(ezsigntemplateformfieldgroup_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


