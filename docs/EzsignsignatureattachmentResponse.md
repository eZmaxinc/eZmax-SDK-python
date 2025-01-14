# EzsignsignatureattachmentResponse

An Ezsignsignatureattachment Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignsignatureattachment_id** | **int** | The unique ID of the Ezsignsignatureattachment | 
**fki_ezsignsignature_id** | **int** | The unique ID of the Ezsignsignature | 
**bin_ezsignsignatureattachment_md5** | **str** | The md5 of the Ezsignsignatureattachment | 
**s_ezsignsignatureattachment_name** | **str** | The name of the Ezsignsignatureattachment | 
**s_download_url** | **str** | The Url to the requested document.  Url will expire after 3 hours. | 

## Example

```python
from eZmaxApi.models.ezsignsignatureattachment_response import EzsignsignatureattachmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureattachmentResponse from a JSON string
ezsignsignatureattachment_response_instance = EzsignsignatureattachmentResponse.from_json(json)
# print the JSON string representation of the object
print(EzsignsignatureattachmentResponse.to_json())

# convert the object into a dict
ezsignsignatureattachment_response_dict = ezsignsignatureattachment_response_instance.to_dict()
# create an instance of EzsignsignatureattachmentResponse from a dict
ezsignsignatureattachment_response_from_dict = EzsignsignatureattachmentResponse.from_dict(ezsignsignatureattachment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


