# EzsigntemplatedocumentGetEzsigntemplatedocumentpagesV1Response

Response for GET /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/getEzsigntemplatedocumentpages

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatedocumentGetEzsigntemplatedocumentpagesV1ResponseMPayload**](EzsigntemplatedocumentGetEzsigntemplatedocumentpagesV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1_response import EzsigntemplatedocumentGetEzsigntemplatedocumentpagesV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentGetEzsigntemplatedocumentpagesV1Response from a JSON string
ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1_response_instance = EzsigntemplatedocumentGetEzsigntemplatedocumentpagesV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentGetEzsigntemplatedocumentpagesV1Response.to_json())

# convert the object into a dict
ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1_response_dict = ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1_response_instance.to_dict()
# create an instance of EzsigntemplatedocumentGetEzsigntemplatedocumentpagesV1Response from a dict
ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1_response_from_dict = EzsigntemplatedocumentGetEzsigntemplatedocumentpagesV1Response.from_dict(ezsigntemplatedocument_get_ezsigntemplatedocumentpages_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


