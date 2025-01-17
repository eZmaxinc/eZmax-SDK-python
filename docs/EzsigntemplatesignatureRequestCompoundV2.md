# EzsigntemplatesignatureRequestCompoundV2

A Ezsigntemplatesignature Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**b_ezsigntemplatesignature_customdate** | **bool** | Whether the Ezsigntemplatesignature has a custom date format or not. (Only possible when eEzsigntemplatesignatureType is **Name** or **Handwritten**) | [optional] 
**a_obj_ezsigntemplatesignaturecustomdate** | [**List[EzsigntemplatesignaturecustomdateRequestCompoundV2]**](EzsigntemplatesignaturecustomdateRequestV2.md) | An array of custom date blocks that will be filled at the time of signature.  Can only be used if bEzsigntemplatesignatureCustomdate is true.  Use an empty array if you don&#39;t want to have a date at all. | [optional] 
**a_obj_ezsigntemplateelementdependency** | [**List[EzsigntemplateelementdependencyRequestCompound]**](EzsigntemplateelementdependencyRequest.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplatesignature_request_compound_v2 import EzsigntemplatesignatureRequestCompoundV2

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignatureRequestCompoundV2 from a JSON string
ezsigntemplatesignature_request_compound_v2_instance = EzsigntemplatesignatureRequestCompoundV2.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignatureRequestCompoundV2.to_json())

# convert the object into a dict
ezsigntemplatesignature_request_compound_v2_dict = ezsigntemplatesignature_request_compound_v2_instance.to_dict()
# create an instance of EzsigntemplatesignatureRequestCompoundV2 from a dict
ezsigntemplatesignature_request_compound_v2_from_dict = EzsigntemplatesignatureRequestCompoundV2.from_dict(ezsigntemplatesignature_request_compound_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


