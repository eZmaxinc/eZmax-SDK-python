# CustomEzsignfoldertypeResponse

A Custom Ezsignfoldertype Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | 
**s_ezsignfoldertype_name_x** | **str** | The name of the Ezsignfoldertype in the language of the requester | [optional] 
**b_ezsignfoldertype_sendproofezsignsigner** | **bool** | Whether we send the proof in the email to Ezsignsigner | [optional] 
**b_ezsignfoldertype_includeproofsigner** | **bool** | THIS FIELD WILL BE DELETED. Whether we include the proof with the signed Ezsigndocument for Ezsignsigners | [optional] 
**b_ezsignfoldertype_includeproofuser** | **bool** | Whether we include the proof with the signed Ezsigndocument for users | [optional] 
**b_ezsignfoldertype_allowdownloadattachmentezsignsigner** | **bool** | Whether we allow the Ezsigndocument to be downloaded by an Ezsignsigner | [optional] 
**b_ezsignfoldertype_allowdownloadproofezsignsigner** | **bool** | Whether we allow the proof to be downloaded by an Ezsignsigner | [optional] 
**b_ezsignfoldertype_delegate** | **bool** | Wheter if delegation of signature is allowed to another user or not | [optional] 
**b_ezsignfoldertype_reassign** | **bool** | Wheter if Reassignment of signature is allowed to another signatory or not | [optional] 
**b_ezsignfoldertype_reassignezsignsigner** | **bool** | Wheter if Reassignment of signature is allowed by a signatory to another signatory or not | [optional] 
**b_ezsignfoldertype_reassignuser** | **bool** | Wheter if Reassignment of signature is allowed by a user to a signatory or another user or not | [optional] 

## Example

```python
from eZmaxApi.models.custom_ezsignfoldertype_response import CustomEzsignfoldertypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsignfoldertypeResponse from a JSON string
custom_ezsignfoldertype_response_instance = CustomEzsignfoldertypeResponse.from_json(json)
# print the JSON string representation of the object
print CustomEzsignfoldertypeResponse.to_json()

# convert the object into a dict
custom_ezsignfoldertype_response_dict = custom_ezsignfoldertype_response_instance.to_dict()
# create an instance of CustomEzsignfoldertypeResponse from a dict
custom_ezsignfoldertype_response_form_dict = custom_ezsignfoldertype_response.from_dict(custom_ezsignfoldertype_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


