# EzsigndocumentEditEzsignformfieldgroupsV2Response

Response for PUT /2/object/ezsigndocument/{pkiEzsigndocumentID}/editEzsignformfieldgroups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigndocumentEditEzsignformfieldgroupsV2ResponseMPayload**](EzsigndocumentEditEzsignformfieldgroupsV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_edit_ezsignformfieldgroups_v2_response import EzsigndocumentEditEzsignformfieldgroupsV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentEditEzsignformfieldgroupsV2Response from a JSON string
ezsigndocument_edit_ezsignformfieldgroups_v2_response_instance = EzsigndocumentEditEzsignformfieldgroupsV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentEditEzsignformfieldgroupsV2Response.to_json())

# convert the object into a dict
ezsigndocument_edit_ezsignformfieldgroups_v2_response_dict = ezsigndocument_edit_ezsignformfieldgroups_v2_response_instance.to_dict()
# create an instance of EzsigndocumentEditEzsignformfieldgroupsV2Response from a dict
ezsigndocument_edit_ezsignformfieldgroups_v2_response_from_dict = EzsigndocumentEditEzsignformfieldgroupsV2Response.from_dict(ezsigndocument_edit_ezsignformfieldgroups_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


