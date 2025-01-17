# EzsigndocumentGetEzsignsignaturesV1Response

Response for GET /1/object/ezsigndocument/{pkiEzsigndocument}/getEzsignsignatures

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsigndocumentGetEzsignsignaturesV1ResponseMPayload**](EzsigndocumentGetEzsignsignaturesV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_get_ezsignsignatures_v1_response import EzsigndocumentGetEzsignsignaturesV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentGetEzsignsignaturesV1Response from a JSON string
ezsigndocument_get_ezsignsignatures_v1_response_instance = EzsigndocumentGetEzsignsignaturesV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentGetEzsignsignaturesV1Response.to_json())

# convert the object into a dict
ezsigndocument_get_ezsignsignatures_v1_response_dict = ezsigndocument_get_ezsignsignatures_v1_response_instance.to_dict()
# create an instance of EzsigndocumentGetEzsignsignaturesV1Response from a dict
ezsigndocument_get_ezsignsignatures_v1_response_from_dict = EzsigndocumentGetEzsignsignaturesV1Response.from_dict(ezsigndocument_get_ezsignsignatures_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


