# EzsignfolderSendV1Response

Response for GET /1/object/attachment/{pkiAttachmentID}/download

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfolder_send_v1_response import EzsignfolderSendV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderSendV1Response from a JSON string
ezsignfolder_send_v1_response_instance = EzsignfolderSendV1Response.from_json(json)
# print the JSON string representation of the object
print EzsignfolderSendV1Response.to_json()

# convert the object into a dict
ezsignfolder_send_v1_response_dict = ezsignfolder_send_v1_response_instance.to_dict()
# create an instance of EzsignfolderSendV1Response from a dict
ezsignfolder_send_v1_response_form_dict = ezsignfolder_send_v1_response.from_dict(ezsignfolder_send_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


