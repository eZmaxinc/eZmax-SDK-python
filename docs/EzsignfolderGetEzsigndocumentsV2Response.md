# EzsignfolderGetEzsigndocumentsV2Response

Response for GET /2/object/ezsignfolder/{pkiEzsignfolder}/getEzsigndocuments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignfolderGetEzsigndocumentsV2ResponseMPayload**](EzsignfolderGetEzsigndocumentsV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_get_ezsigndocuments_v2_response import EzsignfolderGetEzsigndocumentsV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderGetEzsigndocumentsV2Response from a JSON string
ezsignfolder_get_ezsigndocuments_v2_response_instance = EzsignfolderGetEzsigndocumentsV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderGetEzsigndocumentsV2Response.to_json())

# convert the object into a dict
ezsignfolder_get_ezsigndocuments_v2_response_dict = ezsignfolder_get_ezsigndocuments_v2_response_instance.to_dict()
# create an instance of EzsignfolderGetEzsigndocumentsV2Response from a dict
ezsignfolder_get_ezsigndocuments_v2_response_from_dict = EzsignfolderGetEzsigndocumentsV2Response.from_dict(ezsignfolder_get_ezsigndocuments_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


