# EzsigndocumentEditEzsignannotationsV1Response

Response for PUT /1/object/ezsigndocument/{pkiEzsigndocumentID}/editEzsignannotations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigndocumentEditEzsignannotationsV1ResponseMPayload**](EzsigndocumentEditEzsignannotationsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_edit_ezsignannotations_v1_response import EzsigndocumentEditEzsignannotationsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentEditEzsignannotationsV1Response from a JSON string
ezsigndocument_edit_ezsignannotations_v1_response_instance = EzsigndocumentEditEzsignannotationsV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentEditEzsignannotationsV1Response.to_json())

# convert the object into a dict
ezsigndocument_edit_ezsignannotations_v1_response_dict = ezsigndocument_edit_ezsignannotations_v1_response_instance.to_dict()
# create an instance of EzsigndocumentEditEzsignannotationsV1Response from a dict
ezsigndocument_edit_ezsignannotations_v1_response_from_dict = EzsigndocumentEditEzsignannotationsV1Response.from_dict(ezsigndocument_edit_ezsignannotations_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


