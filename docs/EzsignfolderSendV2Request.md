# EzsignfolderSendV2Request

Request for POST /2/object/ezsignfolder/{pkiEzsignfolderID}/send

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**t_ezsignfolder_message** | **str** | A custom text message that will be added to the email sent. | 
**a_fki_ezsignfoldersignerassociation_id** | **List[int]** |  | 
**a_obj_ezsignfoldersignerassociationmessage** | [**List[CustomEzsignfoldersignerassociationmessageRequest]**](CustomEzsignfoldersignerassociationmessageRequest.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_send_v2_request import EzsignfolderSendV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderSendV2Request from a JSON string
ezsignfolder_send_v2_request_instance = EzsignfolderSendV2Request.from_json(json)
# print the JSON string representation of the object
print EzsignfolderSendV2Request.to_json()

# convert the object into a dict
ezsignfolder_send_v2_request_dict = ezsignfolder_send_v2_request_instance.to_dict()
# create an instance of EzsignfolderSendV2Request from a dict
ezsignfolder_send_v2_request_form_dict = ezsignfolder_send_v2_request.from_dict(ezsignfolder_send_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


