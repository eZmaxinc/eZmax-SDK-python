# EzsignfoldertypeGetObjectV2Response

Response for GET /2/object/ezsignfoldertype/{pkiEzsignfoldertypeID}

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfoldertypeGetObjectV2ResponseMPayload**](EzsignfoldertypeGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldertype_get_object_v2_response import EzsignfoldertypeGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldertypeGetObjectV2Response from a JSON string
ezsignfoldertype_get_object_v2_response_instance = EzsignfoldertypeGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print EzsignfoldertypeGetObjectV2Response.to_json()

# convert the object into a dict
ezsignfoldertype_get_object_v2_response_dict = ezsignfoldertype_get_object_v2_response_instance.to_dict()
# create an instance of EzsignfoldertypeGetObjectV2Response from a dict
ezsignfoldertype_get_object_v2_response_form_dict = ezsignfoldertype_get_object_v2_response.from_dict(ezsignfoldertype_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


