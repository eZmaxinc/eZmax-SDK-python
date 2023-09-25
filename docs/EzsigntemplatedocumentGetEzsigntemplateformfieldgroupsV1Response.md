# EzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1Response

Response for GET /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocument}/getEzsigntemplateformfieldgroups

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1ResponseMPayload**](EzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_get_ezsigntemplateformfieldgroups_v1_response import EzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1Response from a JSON string
ezsigntemplatedocument_get_ezsigntemplateformfieldgroups_v1_response_instance = EzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1Response.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1Response.to_json()

# convert the object into a dict
ezsigntemplatedocument_get_ezsigntemplateformfieldgroups_v1_response_dict = ezsigntemplatedocument_get_ezsigntemplateformfieldgroups_v1_response_instance.to_dict()
# create an instance of EzsigntemplatedocumentGetEzsigntemplateformfieldgroupsV1Response from a dict
ezsigntemplatedocument_get_ezsigntemplateformfieldgroups_v1_response_form_dict = ezsigntemplatedocument_get_ezsigntemplateformfieldgroups_v1_response.from_dict(ezsigntemplatedocument_get_ezsigntemplateformfieldgroups_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


