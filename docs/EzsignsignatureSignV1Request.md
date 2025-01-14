# EzsignsignatureSignV1Request

Request for POST /1/object/ezsignsignature/{pkiEzsignsignatureID}/sign

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezsignsigningreason_id** | **int** | The unique ID of the Ezsignsigningreason | [optional] 
**fki_font_id** | **int** | The unique ID of the Font | [optional] 
**s_value** | **str** | The value required for the Ezsignsignature.  This can only be set if eEzsignsignatureType is **City**, **FieldText** or **FieldTextarea** | [optional] 
**e_attachments_confirmation_decision** | **str** | Whether the attachment are accepted or refused.  This can only be set if eEzsignsignatureType is **AttachmentsConfirmation** | [optional] 
**s_attachments_refusal_reason** | **str** | The reason of refused.  This can only be set if eEzsignsignatureType is **AttachmentsConfirmation** | [optional] 
**s_svg** | **str** | The SVG of the signature.  This can only be set if eEzsignsignatureType is **Signature**/**Initials** and **bIsAutomatic** is false | [optional] 
**a_obj_file** | [**List[CommonFile]**](CommonFile.md) |  | [optional] 
**b_is_automatic** | **bool** | Indicates if the Ezsignsignature was part of an automatic process or not.  This can only be true if eEzsignsignatureType is **Acknowledgement**, **City**, **Signature**, **Initials** or **Stamp**.  | 

## Example

```python
from eZmaxApi.models.ezsignsignature_sign_v1_request import EzsignsignatureSignV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureSignV1Request from a JSON string
ezsignsignature_sign_v1_request_instance = EzsignsignatureSignV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsignsignatureSignV1Request.to_json())

# convert the object into a dict
ezsignsignature_sign_v1_request_dict = ezsignsignature_sign_v1_request_instance.to_dict()
# create an instance of EzsignsignatureSignV1Request from a dict
ezsignsignature_sign_v1_request_from_dict = EzsignsignatureSignV1Request.from_dict(ezsignsignature_sign_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


