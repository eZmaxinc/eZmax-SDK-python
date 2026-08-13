# EzsigntemplatepackagemembershipResponseCompoundV3

A Ezsigntemplatepackagemembership Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatepackagemembership_id** | **int** | The unique ID of the Ezsigntemplatepackagemembership | 
**fki_ezsigntemplatepackage_id** | **int** | The unique ID of the Ezsigntemplatepackage | 
**fki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | 
**i_ezsigntemplatepackagemembership_order** | **int** | The order in which the Ezsigntemplate will be imported when using an Ezsigntemplatepackage. | 
**obj_ezsigntemplate** | [**EzsigntemplateResponseCompoundV4**](EzsigntemplateResponseCompoundV4.md) |  | 
**a_obj_ezsigntemplatepackagesignermembership** | [**List[EzsigntemplatepackagesignermembershipResponseCompound]**](EzsigntemplatepackagesignermembershipResponseCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagemembership_response_compound_v3 import EzsigntemplatepackagemembershipResponseCompoundV3

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagemembershipResponseCompoundV3 from a JSON string
ezsigntemplatepackagemembership_response_compound_v3_instance = EzsigntemplatepackagemembershipResponseCompoundV3.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagemembershipResponseCompoundV3.to_json())

# convert the object into a dict
ezsigntemplatepackagemembership_response_compound_v3_dict = ezsigntemplatepackagemembership_response_compound_v3_instance.to_dict()
# create an instance of EzsigntemplatepackagemembershipResponseCompoundV3 from a dict
ezsigntemplatepackagemembership_response_compound_v3_from_dict = EzsigntemplatepackagemembershipResponseCompoundV3.from_dict(ezsigntemplatepackagemembership_response_compound_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


