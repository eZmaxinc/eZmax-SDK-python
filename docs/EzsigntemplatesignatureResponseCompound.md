# EzsigntemplatesignatureResponseCompound

A Ezsigntemplatesignature Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**b_ezsigntemplatesignature_customdate** | **bool** | Whether the Ezsigntemplatesignature has a custom date format or not. (Only possible when eEzsigntemplatesignatureType is **Name** or **Handwritten**) | [optional] 
**a_obj_ezsigntemplatesignaturecustomdate** | [**List[EzsigntemplatesignaturecustomdateResponseCompound]**](EzsigntemplatesignaturecustomdateResponse.md) | An array of custom date blocks that will be filled at the time of signature.  Can only be used if bEzsigntemplatesignatureCustomdate is true.  Use an empty array if you don&#39;t want to have a date at all. | [optional] 
**a_obj_ezsigntemplateelementdependency** | [**List[EzsigntemplateelementdependencyResponseCompound]**](EzsigntemplateelementdependencyResponse.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplatesignature_response_compound import EzsigntemplatesignatureResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignatureResponseCompound from a JSON string
ezsigntemplatesignature_response_compound_instance = EzsigntemplatesignatureResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignatureResponseCompound.to_json())

# convert the object into a dict
ezsigntemplatesignature_response_compound_dict = ezsigntemplatesignature_response_compound_instance.to_dict()
# create an instance of EzsigntemplatesignatureResponseCompound from a dict
ezsigntemplatesignature_response_compound_from_dict = EzsigntemplatesignatureResponseCompound.from_dict(ezsigntemplatesignature_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


