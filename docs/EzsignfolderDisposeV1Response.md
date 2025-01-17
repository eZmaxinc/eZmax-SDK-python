# EzsignfolderDisposeV1Response

Response for POST /1/object/ezsignfolder/{pkiEzsignfolderID}/dispose

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfolder_dispose_v1_response import EzsignfolderDisposeV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderDisposeV1Response from a JSON string
ezsignfolder_dispose_v1_response_instance = EzsignfolderDisposeV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderDisposeV1Response.to_json())

# convert the object into a dict
ezsignfolder_dispose_v1_response_dict = ezsignfolder_dispose_v1_response_instance.to_dict()
# create an instance of EzsignfolderDisposeV1Response from a dict
ezsignfolder_dispose_v1_response_from_dict = EzsignfolderDisposeV1Response.from_dict(ezsignfolder_dispose_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


