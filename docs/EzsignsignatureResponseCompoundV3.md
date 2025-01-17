# EzsignsignatureResponseCompoundV3

An Ezsignsignature Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**b_ezsignsignature_customdate** | **bool** | Whether the Ezsignsignature has a custom date format or not. (Only possible when eEzsignsignatureType is **Name** or **Handwritten**) | [optional] 
**a_obj_ezsignsignaturecustomdate** | [**List[EzsignsignaturecustomdateResponseCompoundV2]**](EzsignsignaturecustomdateResponseV2.md) | An array of custom date blocks that will be filled at the time of signature.  Can only be used if bEzsignsignatureCustomdate is true.  Use an empty array if you don&#39;t want to have a date at all. | [optional] 
**obj_creditcardtransaction** | [**CustomCreditcardtransactionResponse**](CustomCreditcardtransactionResponse.md) |  | [optional] 
**a_obj_ezsignelementdependency** | [**List[EzsignelementdependencyResponseCompound]**](EzsignelementdependencyResponse.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignsignature_response_compound_v3 import EzsignsignatureResponseCompoundV3

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureResponseCompoundV3 from a JSON string
ezsignsignature_response_compound_v3_instance = EzsignsignatureResponseCompoundV3.from_json(json)
# print the JSON string representation of the object
print(EzsignsignatureResponseCompoundV3.to_json())

# convert the object into a dict
ezsignsignature_response_compound_v3_dict = ezsignsignature_response_compound_v3_instance.to_dict()
# create an instance of EzsignsignatureResponseCompoundV3 from a dict
ezsignsignature_response_compound_v3_from_dict = EzsignsignatureResponseCompoundV3.from_dict(ezsignsignature_response_compound_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


