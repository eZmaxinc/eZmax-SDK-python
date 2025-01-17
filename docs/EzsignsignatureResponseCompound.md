# EzsignsignatureResponseCompound

An Ezsignsignature Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dt_ezsignsignature_date_in_folder_timezone** | **str** | The date the Ezsignsignature was signed in folder&#39;s timezone | [optional] 
**b_ezsignsignature_customdate** | **bool** | Whether the Ezsignsignature has a custom date format or not. (Only possible when eEzsignsignatureType is **Name** or **Handwritten**) | [optional] 
**a_obj_ezsignsignaturecustomdate** | [**List[EzsignsignaturecustomdateResponseCompound]**](EzsignsignaturecustomdateResponse.md) | An array of custom date blocks that will be filled at the time of signature.  Can only be used if bEzsignsignatureCustomdate is true.  Use an empty array if you don&#39;t want to have a date at all. | [optional] 
**obj_creditcardtransaction** | [**CustomCreditcardtransactionResponse**](CustomCreditcardtransactionResponse.md) |  | [optional] 
**a_obj_ezsignelementdependency** | [**List[EzsignelementdependencyResponseCompound]**](EzsignelementdependencyResponse.md) |  | [optional] 
**obj_timezone** | [**CustomTimezoneWithCodeResponse**](CustomTimezoneWithCodeResponse.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignsignature_response_compound import EzsignsignatureResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureResponseCompound from a JSON string
ezsignsignature_response_compound_instance = EzsignsignatureResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignsignatureResponseCompound.to_json())

# convert the object into a dict
ezsignsignature_response_compound_dict = ezsignsignature_response_compound_instance.to_dict()
# create an instance of EzsignsignatureResponseCompound from a dict
ezsignsignature_response_compound_from_dict = EzsignsignatureResponseCompound.from_dict(ezsignsignature_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


