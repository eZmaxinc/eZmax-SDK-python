# EzsignfoldersignerassociationCreateEmbeddedUrlV1Request

Request for POST /1/object/ezsignfoldersignerassociation/createEmbeddedUrl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_return_url** | **str** | The return Url to redirect after the signing is completed | [optional] 
**s_iframedomain** | **str** | Domain protection for the iFrame | [optional] 
**b_isiframe** | **bool** | Whether the url would be in an iFrame or not | [optional] 

## Example

```python
from eZmaxApi.models.ezsignfoldersignerassociation_create_embedded_url_v1_request import EzsignfoldersignerassociationCreateEmbeddedUrlV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfoldersignerassociationCreateEmbeddedUrlV1Request from a JSON string
ezsignfoldersignerassociation_create_embedded_url_v1_request_instance = EzsignfoldersignerassociationCreateEmbeddedUrlV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsignfoldersignerassociationCreateEmbeddedUrlV1Request.to_json())

# convert the object into a dict
ezsignfoldersignerassociation_create_embedded_url_v1_request_dict = ezsignfoldersignerassociation_create_embedded_url_v1_request_instance.to_dict()
# create an instance of EzsignfoldersignerassociationCreateEmbeddedUrlV1Request from a dict
ezsignfoldersignerassociation_create_embedded_url_v1_request_form_dict = ezsignfoldersignerassociation_create_embedded_url_v1_request.from_dict(ezsignfoldersignerassociation_create_embedded_url_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


