# EzsigntemplateformfieldgroupGetObjectV2Response

Response for GET /2/object/ezsigntemplateformfieldgroup/{pkiEzsigntemplateformfieldgroupID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplateformfieldgroupGetObjectV2ResponseMPayload**](EzsigntemplateformfieldgroupGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplateformfieldgroup_get_object_v2_response import EzsigntemplateformfieldgroupGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateformfieldgroupGetObjectV2Response from a JSON string
ezsigntemplateformfieldgroup_get_object_v2_response_instance = EzsigntemplateformfieldgroupGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print EzsigntemplateformfieldgroupGetObjectV2Response.to_json()

# convert the object into a dict
ezsigntemplateformfieldgroup_get_object_v2_response_dict = ezsigntemplateformfieldgroup_get_object_v2_response_instance.to_dict()
# create an instance of EzsigntemplateformfieldgroupGetObjectV2Response from a dict
ezsigntemplateformfieldgroup_get_object_v2_response_form_dict = ezsigntemplateformfieldgroup_get_object_v2_response.from_dict(ezsigntemplateformfieldgroup_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


