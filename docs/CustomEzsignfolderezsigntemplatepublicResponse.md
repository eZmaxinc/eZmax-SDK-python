# CustomEzsignfolderezsigntemplatepublicResponse

An Ezsignfolder Object in the context of an Ezsigntemplatepublic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | 
**s_ezsignfolder_description** | **str** | The description of the Ezsignfolder | 
**e_ezsignfolder_step** | [**FieldEEzsignfolderStep**](FieldEEzsignfolderStep.md) |  | 
**i_ezsignfolder_signaturetotal** | **int** | The number of total signatures that were requested in the Ezsignfolder | 
**i_ezsignfolder_formfieldtotal** | **int** | The number of total form fields that were requested in the Ezsignfolder | 
**i_ezsignfolder_signaturesigned** | **int** | The number of signatures that were signed in the Ezsignfolder. | 
**a_obj_ezsignfolderezsigntemplatepublic_signer** | [**List[CustomEzsignfolderezsigntemplatepublicSignerResponse]**](CustomEzsignfolderezsigntemplatepublicSignerResponse.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.custom_ezsignfolderezsigntemplatepublic_response import CustomEzsignfolderezsigntemplatepublicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsignfolderezsigntemplatepublicResponse from a JSON string
custom_ezsignfolderezsigntemplatepublic_response_instance = CustomEzsignfolderezsigntemplatepublicResponse.from_json(json)
# print the JSON string representation of the object
print(CustomEzsignfolderezsigntemplatepublicResponse.to_json())

# convert the object into a dict
custom_ezsignfolderezsigntemplatepublic_response_dict = custom_ezsignfolderezsigntemplatepublic_response_instance.to_dict()
# create an instance of CustomEzsignfolderezsigntemplatepublicResponse from a dict
custom_ezsignfolderezsigntemplatepublic_response_from_dict = CustomEzsignfolderezsigntemplatepublicResponse.from_dict(custom_ezsignfolderezsigntemplatepublic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


