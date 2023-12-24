# EzsigndocumentGetDownloadUrlV1ResponseMPayload

Payload for GET /1/object/ezsigndocument/{pkiEzsigndocument}/getDownloadUrl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_download_url** | **str** | The Url to the requested document.  Url will expire after 5 minutes. | 

## Example

```python
from eZmaxApi.models.ezsigndocument_get_download_url_v1_response_m_payload import EzsigndocumentGetDownloadUrlV1ResponseMPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentGetDownloadUrlV1ResponseMPayload from a JSON string
ezsigndocument_get_download_url_v1_response_m_payload_instance = EzsigndocumentGetDownloadUrlV1ResponseMPayload.from_json(json)
# print the JSON string representation of the object
print EzsigndocumentGetDownloadUrlV1ResponseMPayload.to_json()

# convert the object into a dict
ezsigndocument_get_download_url_v1_response_m_payload_dict = ezsigndocument_get_download_url_v1_response_m_payload_instance.to_dict()
# create an instance of EzsigndocumentGetDownloadUrlV1ResponseMPayload from a dict
ezsigndocument_get_download_url_v1_response_m_payload_form_dict = ezsigndocument_get_download_url_v1_response_m_payload.from_dict(ezsigndocument_get_download_url_v1_response_m_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


