# CustomEzmaxinvoicingEzsignfolderResponse

An EzmaxinvoicingEzsignfolder object containing information about the Ezmaxinvoicing for an Ezsignfolder

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | 
**fki_billingentityinternal_id** | **int** | The unique ID of the Billingentityinternal. | [optional] 
**s_ezsignfolder_description** | **str** | The description of the Ezsignfolder | 
**b_ezsigntsarequirement_billable** | **bool** | Whether the TSA requirement is billable or not | 
**b_ezsignfolder_mfaused** | **bool** | Whether the MFA was used or not for the Ezsignfolder | 
**b_ezsignfolder_paymentused** | **bool** | Whether there was a signature is of type payment | 
**b_ezsignfolder_allowed** | **bool** | Whether you have access to the Ezsignfolder or not | 

## Example

```python
from eZmaxApi.models.custom_ezmaxinvoicing_ezsignfolder_response import CustomEzmaxinvoicingEzsignfolderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzmaxinvoicingEzsignfolderResponse from a JSON string
custom_ezmaxinvoicing_ezsignfolder_response_instance = CustomEzmaxinvoicingEzsignfolderResponse.from_json(json)
# print the JSON string representation of the object
print(CustomEzmaxinvoicingEzsignfolderResponse.to_json())

# convert the object into a dict
custom_ezmaxinvoicing_ezsignfolder_response_dict = custom_ezmaxinvoicing_ezsignfolder_response_instance.to_dict()
# create an instance of CustomEzmaxinvoicingEzsignfolderResponse from a dict
custom_ezmaxinvoicing_ezsignfolder_response_from_dict = CustomEzmaxinvoicingEzsignfolderResponse.from_dict(custom_ezmaxinvoicing_ezsignfolder_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


