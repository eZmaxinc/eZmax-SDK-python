# EzsigntemplatedocumentGetEzsigntemplatedocumentpagerecognitionsV1Response

Response for GET /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocument}/getEzsigntemplatedocumentpagerecognitions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatedocumentGetEzsigntemplatedocumentpagerecognitionsV1ResponseMPayload**](EzsigntemplatedocumentGetEzsigntemplatedocumentpagerecognitionsV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_get_ezsigntemplatedocumentpagerecognitions_v1_response import EzsigntemplatedocumentGetEzsigntemplatedocumentpagerecognitionsV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentGetEzsigntemplatedocumentpagerecognitionsV1Response from a JSON string
ezsigntemplatedocument_get_ezsigntemplatedocumentpagerecognitions_v1_response_instance = EzsigntemplatedocumentGetEzsigntemplatedocumentpagerecognitionsV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentGetEzsigntemplatedocumentpagerecognitionsV1Response.to_json())

# convert the object into a dict
ezsigntemplatedocument_get_ezsigntemplatedocumentpagerecognitions_v1_response_dict = ezsigntemplatedocument_get_ezsigntemplatedocumentpagerecognitions_v1_response_instance.to_dict()
# create an instance of EzsigntemplatedocumentGetEzsigntemplatedocumentpagerecognitionsV1Response from a dict
ezsigntemplatedocument_get_ezsigntemplatedocumentpagerecognitions_v1_response_from_dict = EzsigntemplatedocumentGetEzsigntemplatedocumentpagerecognitionsV1Response.from_dict(ezsigntemplatedocument_get_ezsigntemplatedocumentpagerecognitions_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


