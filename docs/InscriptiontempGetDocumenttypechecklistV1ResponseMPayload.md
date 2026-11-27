# InscriptiontempGetDocumenttypechecklistV1ResponseMPayload

Response for GET /1/object/inscriptiontemp/{pkiInscriptiontempID}/getDocumenttypechecklist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_documenttypechecklist** | [**List[CustomDocumenttypechecklistResponse]**](CustomDocumenttypechecklistResponse.md) |  | 

## Example

```python
from eZmaxApi.models.inscriptiontemp_get_documenttypechecklist_v1_response_m_payload import InscriptiontempGetDocumenttypechecklistV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of InscriptiontempGetDocumenttypechecklistV1ResponseMPayload from a JSON string
inscriptiontemp_get_documenttypechecklist_v1_response_m_payload_instance = InscriptiontempGetDocumenttypechecklistV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print(InscriptiontempGetDocumenttypechecklistV1ResponseMPayload.to_json())

# convert the object into a dict
inscriptiontemp_get_documenttypechecklist_v1_response_m_payload_dict = inscriptiontemp_get_documenttypechecklist_v1_response_m_payload_instance.to_dict()
# create an instance of InscriptiontempGetDocumenttypechecklistV1ResponseMPayload from a dict
inscriptiontemp_get_documenttypechecklist_v1_response_m_payload_from_dict = InscriptiontempGetDocumenttypechecklistV1ResponseMPayload.from_dict(inscriptiontemp_get_documenttypechecklist_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


