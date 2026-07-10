# EzsignfolderGetEzsignfoldersignerassociationsV2Response

Response for GET /1/object/ezsignfolder/{pkiEzsignfolder}/getEzsignfoldersignerassociations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfolderGetEzsignfoldersignerassociationsV2ResponseMPayload**](EzsignfolderGetEzsignfoldersignerassociationsV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_get_ezsignfoldersignerassociations_v2_response import EzsignfolderGetEzsignfoldersignerassociationsV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderGetEzsignfoldersignerassociationsV2Response from a JSON string
ezsignfolder_get_ezsignfoldersignerassociations_v2_response_instance = EzsignfolderGetEzsignfoldersignerassociationsV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderGetEzsignfoldersignerassociationsV2Response.to_json())

# convert the object into a dict
ezsignfolder_get_ezsignfoldersignerassociations_v2_response_dict = ezsignfolder_get_ezsignfoldersignerassociations_v2_response_instance.to_dict()
# create an instance of EzsignfolderGetEzsignfoldersignerassociationsV2Response from a dict
ezsignfolder_get_ezsignfoldersignerassociations_v2_response_from_dict = EzsignfolderGetEzsignfoldersignerassociationsV2Response.from_dict(ezsignfolder_get_ezsignfoldersignerassociations_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


