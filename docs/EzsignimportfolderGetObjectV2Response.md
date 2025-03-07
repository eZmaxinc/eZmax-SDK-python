# EzsignimportfolderGetObjectV2Response

Response for GET /2/object/ezsignimportfolder/{pkiEzsignimportfolderID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignimportfolderGetObjectV2ResponseMPayload**](EzsignimportfolderGetObjectV2ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignimportfolder_get_object_v2_response import EzsignimportfolderGetObjectV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignimportfolderGetObjectV2Response from a JSON string
ezsignimportfolder_get_object_v2_response_instance = EzsignimportfolderGetObjectV2Response.from_json(json)
# print the JSON string representation of the object
print(EzsignimportfolderGetObjectV2Response.to_json())

# convert the object into a dict
ezsignimportfolder_get_object_v2_response_dict = ezsignimportfolder_get_object_v2_response_instance.to_dict()
# create an instance of EzsignimportfolderGetObjectV2Response from a dict
ezsignimportfolder_get_object_v2_response_from_dict = EzsignimportfolderGetObjectV2Response.from_dict(ezsignimportfolder_get_object_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


