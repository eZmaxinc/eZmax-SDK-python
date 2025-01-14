# EzsignfoldersignerassociationCreateEmbeddedUrlV1Request

Request for POST /1/object/ezsignfoldersignerassociation/createEmbeddedUrl

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_return_url** | **str** | The return Url to redirect after the signing is completed  **Warning** Due to the potential for Ezsignsigners to cancel redirection, close their browser post-signing, or spoof the landing URL, it&#39;s advisable not to solely depend on the sReturnUrl for accurate status within your integration.  Once the Ezsignsigner finishes, they are directed back to your application. Your application can retain transaction state details by either storing data in a cookie or incorporating query parameters in the sReturnUrl. For example: https://www.example.com/sReturnUrl?sSessionID&#x3D;ABC123  The actual url that will be called will have an extra url parameter appended to give details about the process. The possible values are listed in the table below. For example: https://www.example.com/sReturnUrl?sSessionID&#x3D;ABC123&amp;eEzsignEvent&#x3D;CompletedEzsignfolder   |**Query parameters appended**| |---| |eEzsignEvent|   |**eEzsignEvent**|**Description**| |---|---| |SessionTimeout|The session timed out| |SessionLogout|The Ezsignsigner signed out| |DeclinedTermOfUse|The Ezsignsigner refused the terms| |DeclinedSign|The Ezsignsigner refused to sign| |Reassigned|The Ezsignsigner reassigned his signatures to someone else| |CompletedStep|The Ezsignsigner completed his step. There is other signatures to complete the Ezsigndocument| |CompletedEzsignfolder|The Ezsignfolder is completed. Everyone signed their signatures| | [optional] 
**s_iframedomain** | **str** | Domain protection for the iFrame | [optional] 
**b_is_iframe** | **bool** | Whether the url would be in an iFrame or not | [optional] 

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
ezsignfoldersignerassociation_create_embedded_url_v1_request_from_dict = EzsignfoldersignerassociationCreateEmbeddedUrlV1Request.from_dict(ezsignfoldersignerassociation_create_embedded_url_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


