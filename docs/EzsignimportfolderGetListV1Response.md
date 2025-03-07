# EzsignimportfolderGetListV1Response

Response for GET /1/object/ezsignimportfolder/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsignimportfolderGetListV1ResponseMPayload**](EzsignimportfolderGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignimportfolder_get_list_v1_response import EzsignimportfolderGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignimportfolderGetListV1Response from a JSON string
ezsignimportfolder_get_list_v1_response_instance = EzsignimportfolderGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignimportfolderGetListV1Response.to_json())

# convert the object into a dict
ezsignimportfolder_get_list_v1_response_dict = ezsignimportfolder_get_list_v1_response_instance.to_dict()
# create an instance of EzsignimportfolderGetListV1Response from a dict
ezsignimportfolder_get_list_v1_response_from_dict = EzsignimportfolderGetListV1Response.from_dict(ezsignimportfolder_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


