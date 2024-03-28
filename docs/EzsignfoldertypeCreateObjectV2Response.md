# EzsignfoldertypeCreateObjectV2Response

Response for POST /2/object/ezsignfoldertype

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfoldertypeCreateObjectV2ResponseMPayload**](EzsignfoldertypeCreateObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfoldertype_create_object_v2_response import EzsignfoldertypeCreateObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldertypeCreateObjectV2Response from a JSON string
ezsignfoldertype_create_object_v2_response_instance = EzsignfoldertypeCreateObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldertypeCreateObjectV2Response.to_json())

# convert the object into a dict
ezsignfoldertype_create_object_v2_response_dict = ezsignfoldertype_create_object_v2_response_instance.to_dict()
# create an instance of EzsignfoldertypeCreateObjectV2Response from a dict
ezsignfoldertype_create_object_v2_response_form_dict = ezsignfoldertype_create_object_v2_response.from_dict(ezsignfoldertype_create_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


