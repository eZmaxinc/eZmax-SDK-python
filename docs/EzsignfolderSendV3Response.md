# EzsignfolderSendV3Response

Response for POST /3/object/ezsignfolder/{pkiEzsignfolderID}/send

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfolder_send_v3_response import EzsignfolderSendV3Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderSendV3Response from a JSON string
ezsignfolder_send_v3_response_instance = EzsignfolderSendV3Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderSendV3Response.to_json())

# convert the object into a dict
ezsignfolder_send_v3_response_dict = ezsignfolder_send_v3_response_instance.to_dict()
# create an instance of EzsignfolderSendV3Response from a dict
ezsignfolder_send_v3_response_from_dict = EzsignfolderSendV3Response.from_dict(ezsignfolder_send_v3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


