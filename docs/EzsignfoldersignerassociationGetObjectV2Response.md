# EzsignfoldersignerassociationGetObjectV2Response

Response for GET /2/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociationID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfoldersignerassociationGetObjectV2ResponseMPayload**](EzsignfoldersignerassociationGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_get_object_v2_response import EzsignfoldersignerassociationGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationGetObjectV2Response from a JSON string
ezsignfoldersignerassociation_get_object_v2_response_instance = EzsignfoldersignerassociationGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print EzsignfoldersignerassociationGetObjectV2Response.to_json()

# convert the object into a dict
ezsignfoldersignerassociation_get_object_v2_response_dict = ezsignfoldersignerassociation_get_object_v2_response_instance.to_dict()
# create an instance of EzsignfoldersignerassociationGetObjectV2Response from a dict
ezsignfoldersignerassociation_get_object_v2_response_form_dict = ezsignfoldersignerassociation_get_object_v2_response.from_dict(ezsignfoldersignerassociation_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


