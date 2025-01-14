# EzsigntemplatedocumentEditEzsigntemplatedocumentpagerecognitionsV1Response

Response for PUT /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/editEzsigntemplatedocumentpagerecognitions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatedocumentEditEzsigntemplatedocumentpagerecognitionsV1ResponseMPayload**](EzsigntemplatedocumentEditEzsigntemplatedocumentpagerecognitionsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_edit_ezsigntemplatedocumentpagerecognitions_v1_response import EzsigntemplatedocumentEditEzsigntemplatedocumentpagerecognitionsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentEditEzsigntemplatedocumentpagerecognitionsV1Response from a JSON string
ezsigntemplatedocument_edit_ezsigntemplatedocumentpagerecognitions_v1_response_instance = EzsigntemplatedocumentEditEzsigntemplatedocumentpagerecognitionsV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentEditEzsigntemplatedocumentpagerecognitionsV1Response.to_json())

# convert the object into a dict
ezsigntemplatedocument_edit_ezsigntemplatedocumentpagerecognitions_v1_response_dict = ezsigntemplatedocument_edit_ezsigntemplatedocumentpagerecognitions_v1_response_instance.to_dict()
# create an instance of EzsigntemplatedocumentEditEzsigntemplatedocumentpagerecognitionsV1Response from a dict
ezsigntemplatedocument_edit_ezsigntemplatedocumentpagerecognitions_v1_response_from_dict = EzsigntemplatedocumentEditEzsigntemplatedocumentpagerecognitionsV1Response.from_dict(ezsigntemplatedocument_edit_ezsigntemplatedocumentpagerecognitions_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


