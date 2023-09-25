# EzsigntemplatedocumentResponseCompound

A Ezsigntemplatedocument Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatedocument_id** | **int** | The unique ID of the Ezsigntemplatedocument | 
**fki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | 
**s_ezsigntemplatedocument_name** | **str** | The name of the Ezsigntemplatedocument. | 
**i_ezsigntemplatedocument_pagetotal** | **int** | The number of pages in the Ezsigntemplatedocument. | 
**i_ezsigntemplatedocument_signaturetotal** | **int** | The number of total signatures in the Ezsigntemplate. | 
**b_ezsigntemplatedocument_hassignedsignatures** | **bool** | If the Ezsigntemplatedocument contains signed signatures (From internal or external sources) | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_response_compound import EzsigntemplatedocumentResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentResponseCompound from a JSON string
ezsigntemplatedocument_response_compound_instance = EzsigntemplatedocumentResponseCompound.from_json(json)
# print the JSON string representation of the object
print EzsigntemplatedocumentResponseCompound.to_json()

# convert the object into a dict
ezsigntemplatedocument_response_compound_dict = ezsigntemplatedocument_response_compound_instance.to_dict()
# create an instance of EzsigntemplatedocumentResponseCompound from a dict
ezsigntemplatedocument_response_compound_form_dict = ezsigntemplatedocument_response_compound.from_dict(ezsigntemplatedocument_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


