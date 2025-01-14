# EzsignfolderSendV3Request

Request for POST /3/object/ezsignfolder/{pkiEzsignfolderID}/send

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**t_ezsignfolder_message** | **str** | A custom text message that will be added to the email sent. | [optional] 
**e_ezsignfolder_messageorder** | [**FieldEEzsignfolderMessageorder**](FieldEEzsignfolderMessageorder.md) |  | [optional] [default to FieldEEzsignfolderMessageorder.GLOBALFIRST]
**dt_ezsignfolder_delayedsenddate** | **str** | The date and time at which the Ezsignfolder will be sent in the future. | [optional] 
**a_fki_ezsignfoldersignerassociation_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.ezsignfolder_send_v3_request import EzsignfolderSendV3Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignfolderSendV3Request from a JSON string
ezsignfolder_send_v3_request_instance = EzsignfolderSendV3Request.from_json(json)
# print the JSON string representation of the object
print(EzsignfolderSendV3Request.to_json())

# convert the object into a dict
ezsignfolder_send_v3_request_dict = ezsignfolder_send_v3_request_instance.to_dict()
# create an instance of EzsignfolderSendV3Request from a dict
ezsignfolder_send_v3_request_from_dict = EzsignfolderSendV3Request.from_dict(ezsignfolder_send_v3_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


