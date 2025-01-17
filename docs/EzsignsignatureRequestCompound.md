# EzsignsignatureRequestCompound

An Ezsignsignature Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**b_ezsignsignature_customdate** | **bool** | Whether the Ezsignsignature has a custom date format or not. (Only possible when eEzsignsignatureType is **Name** or **Handwritten**) | [optional] 
**a_obj_ezsignsignaturecustomdate** | [**List[EzsignsignaturecustomdateRequestCompound]**](EzsignsignaturecustomdateRequest.md) | An array of custom date blocks that will be filled at the time of signature.  Can only be used if bEzsignsignatureCustomdate is true.  Use an empty array if you don&#39;t want to have a date at all. | [optional] 
**a_obj_ezsignelementdependency** | [**List[EzsignelementdependencyRequestCompound]**](EzsignelementdependencyRequest.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsignsignature_request_compound import EzsignsignatureRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignatureRequestCompound from a JSON string
ezsignsignature_request_compound_instance = EzsignsignatureRequestCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignsignatureRequestCompound.to_json())

# convert the object into a dict
ezsignsignature_request_compound_dict = ezsignsignature_request_compound_instance.to_dict()
# create an instance of EzsignsignatureRequestCompound from a dict
ezsignsignature_request_compound_from_dict = EzsignsignatureRequestCompound.from_dict(ezsignsignature_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


