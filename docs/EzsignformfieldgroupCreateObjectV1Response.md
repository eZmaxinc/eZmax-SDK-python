# EzsignformfieldgroupCreateObjectV1Response

Response for POST /1/object/ezsignformfieldgroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignformfieldgroupCreateObjectV1ResponseMPayload**](EzsignformfieldgroupCreateObjectV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignformfieldgroup_create_object_v1_response import EzsignformfieldgroupCreateObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignformfieldgroupCreateObjectV1Response from a JSON string
ezsignformfieldgroup_create_object_v1_response_instance = EzsignformfieldgroupCreateObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignformfieldgroupCreateObjectV1Response.to_json())

# convert the object into a dict
ezsignformfieldgroup_create_object_v1_response_dict = ezsignformfieldgroup_create_object_v1_response_instance.to_dict()
# create an instance of EzsignformfieldgroupCreateObjectV1Response from a dict
ezsignformfieldgroup_create_object_v1_response_from_dict = EzsignformfieldgroupCreateObjectV1Response.from_dict(ezsignformfieldgroup_create_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


