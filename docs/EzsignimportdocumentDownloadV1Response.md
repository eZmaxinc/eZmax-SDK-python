# EzsignimportdocumentDownloadV1Response

Response for GET /1/object/ezsignimportdocument/{pkiEzsignimportdocumentID}/download

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | **object** | Response for GET /1/object/ezsignimportdocument/{pkiEzsignimportdocumentID}/download | 

## Example

```python
from eZmaxApi.models.ezsignimportdocument_download_v1_response import EzsignimportdocumentDownloadV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignimportdocumentDownloadV1Response from a JSON string
ezsignimportdocument_download_v1_response_instance = EzsignimportdocumentDownloadV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignimportdocumentDownloadV1Response.to_json())

# convert the object into a dict
ezsignimportdocument_download_v1_response_dict = ezsignimportdocument_download_v1_response_instance.to_dict()
# create an instance of EzsignimportdocumentDownloadV1Response from a dict
ezsignimportdocument_download_v1_response_from_dict = EzsignimportdocumentDownloadV1Response.from_dict(ezsignimportdocument_download_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


