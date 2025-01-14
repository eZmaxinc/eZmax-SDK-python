# EzsigntemplateglobalResponse

A Ezsigntemplateglobal Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplateglobal_id** | **int** | The unique ID of the Ezsigntemplateglobal | 
**fki_ezsigntemplateglobaldocument_id** | **int** | The unique ID of the Ezsigntemplateglobaldocument | 
**fki_module_id** | **int** | The unique ID of the Module | 
**s_module_name_x** | **str** | The Name of the Module in the language of the requester | [optional] 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**s_language_name_x** | **str** | The Name of the Language in the language of the requester | 
**e_ezsigntemplateglobal_module** | [**FieldEEzsigntemplateglobalModule**](FieldEEzsigntemplateglobalModule.md) |  | 
**e_ezsigntemplateglobal_supplier** | [**FieldEEzsigntemplateglobalSupplier**](FieldEEzsigntemplateglobalSupplier.md) |  | 
**s_ezsigntemplateglobal_code** | **str** | The Code of the Ezsigntemplateglobal | 
**s_ezsigntemplateglobal_description** | **str** | The description of the Ezsigntemplate | 

## Example

```python
from eZmaxApi.models.ezsigntemplateglobal_response import EzsigntemplateglobalResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateglobalResponse from a JSON string
ezsigntemplateglobal_response_instance = EzsigntemplateglobalResponse.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateglobalResponse.to_json())

# convert the object into a dict
ezsigntemplateglobal_response_dict = ezsigntemplateglobal_response_instance.to_dict()
# create an instance of EzsigntemplateglobalResponse from a dict
ezsigntemplateglobal_response_from_dict = EzsigntemplateglobalResponse.from_dict(ezsigntemplateglobal_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


