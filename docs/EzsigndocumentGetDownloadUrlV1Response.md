# EzsigndocumentGetDownloadUrlV1Response

Response for GET /1/object/ezsigndocument/{pkiEzsigndocument}/getDownloadUrl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsigndocumentGetDownloadUrlV1ResponseMPayload**](EzsigndocumentGetDownloadUrlV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigndocument_get_download_url_v1_response import EzsigndocumentGetDownloadUrlV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentGetDownloadUrlV1Response from a JSON string
ezsigndocument_get_download_url_v1_response_instance = EzsigndocumentGetDownloadUrlV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentGetDownloadUrlV1Response.to_json())

# convert the object into a dict
ezsigndocument_get_download_url_v1_response_dict = ezsigndocument_get_download_url_v1_response_instance.to_dict()
# create an instance of EzsigndocumentGetDownloadUrlV1Response from a dict
ezsigndocument_get_download_url_v1_response_from_dict = EzsigndocumentGetDownloadUrlV1Response.from_dict(ezsigndocument_get_download_url_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


