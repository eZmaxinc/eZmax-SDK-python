# EzsignfoldersignerassociationForceDisconnectV1Response

Response for POST /1/object/ezsignfoldersignerassociation/{pkiEzsignfoldersignerassociation}/forceDisconnect

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_force_disconnect_v1_response import EzsignfoldersignerassociationForceDisconnectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationForceDisconnectV1Response from a JSON string
ezsignfoldersignerassociation_force_disconnect_v1_response_instance = EzsignfoldersignerassociationForceDisconnectV1Response.from_json(json)
# print the JSON string representation of the object
print EzsignfoldersignerassociationForceDisconnectV1Response.to_json()

# convert the object into a dict
ezsignfoldersignerassociation_force_disconnect_v1_response_dict = ezsignfoldersignerassociation_force_disconnect_v1_response_instance.to_dict()
# create an instance of EzsignfoldersignerassociationForceDisconnectV1Response from a dict
ezsignfoldersignerassociation_force_disconnect_v1_response_form_dict = ezsignfoldersignerassociation_force_disconnect_v1_response.from_dict(ezsignfoldersignerassociation_force_disconnect_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


