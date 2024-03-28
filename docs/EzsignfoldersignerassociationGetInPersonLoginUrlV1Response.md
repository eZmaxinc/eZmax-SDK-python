# EzsignfoldersignerassociationGetInPersonLoginUrlV1Response

Response for GET /1/object/ezsignfoldersignerassociation/getInPersonLoginUrl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfoldersignerassociationGetInPersonLoginUrlV1ResponseMPayload**](EzsignfoldersignerassociationGetInPersonLoginUrlV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_get_in_person_login_url_v1_response import EzsignfoldersignerassociationGetInPersonLoginUrlV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationGetInPersonLoginUrlV1Response from a JSON string
ezsignfoldersignerassociation_get_in_person_login_url_v1_response_instance = EzsignfoldersignerassociationGetInPersonLoginUrlV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationGetInPersonLoginUrlV1Response.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_get_in_person_login_url_v1_response_dict = ezsignfoldersignerassociation_get_in_person_login_url_v1_response_instance.to_dict()
# create an instance of EzsignfoldersignerassociationGetInPersonLoginUrlV1Response from a dict
ezsignfoldersignerassociation_get_in_person_login_url_v1_response_form_dict = ezsignfoldersignerassociation_get_in_person_login_url_v1_response.from_dict(ezsignfoldersignerassociation_get_in_person_login_url_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


