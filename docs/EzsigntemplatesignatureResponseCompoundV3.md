# EzsigntemplatesignatureResponseCompoundV3

A Ezsigntemplatesignature Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**b_ezsigntemplatesignature_customdate** | **bool** | Whether the Ezsigntemplatesignature has a custom date format or not. (Only possible when eEzsigntemplatesignatureType is **Name** or **Handwritten**) | [optional] 
**a_obj_ezsigntemplatesignaturecustomdate** | [**List[EzsigntemplatesignaturecustomdateResponseCompoundV2]**](EzsigntemplatesignaturecustomdateResponseV2.md) | An array of custom date blocks that will be filled at the time of signature.  Can only be used if bEzsigntemplatesignatureCustomdate is true.  Use an empty array if you don&#39;t want to have a date at all. | [optional] 
**a_obj_ezsigntemplateelementdependency** | [**List[EzsigntemplateelementdependencyResponseCompound]**](EzsigntemplateelementdependencyResponse.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplatesignature_response_compound_v3 import EzsigntemplatesignatureResponseCompoundV3

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignatureResponseCompoundV3 from a JSON string
ezsigntemplatesignature_response_compound_v3_instance = EzsigntemplatesignatureResponseCompoundV3.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignatureResponseCompoundV3.to_json())

# convert the object into a dict
ezsigntemplatesignature_response_compound_v3_dict = ezsigntemplatesignature_response_compound_v3_instance.to_dict()
# create an instance of EzsigntemplatesignatureResponseCompoundV3 from a dict
ezsigntemplatesignature_response_compound_v3_from_dict = EzsigntemplatesignatureResponseCompoundV3.from_dict(ezsigntemplatesignature_response_compound_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


