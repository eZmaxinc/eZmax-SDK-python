# TaxassignmentAutocompleteElementResponse

A Taxassignment AutocompleteElement Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_taxassignment_description_x** | **str** | The description of the Taxassignment  in the language of the requester | 
**pki_taxassignment_id** | **int** | The unique ID of the Taxassignment.  Valid values:  |Value|Description| |-|-| |1|No tax| |2|GST| |3|HST (ON)| |4|HST (NB)| |5|HST (NS)| |6|HST (NL)| |7|HST (PE)| |8|GST + QST (QC)| |9|GST + QST (QC) Non-Recoverable| |10|GST + PST (BC)| |11|GST + PST (SK)| |12|GST + RST (MB)| |13|GST + PST (BC) Non-Recoverable| |14|GST + PST (SK) Non-Recoverable| |15|GST + RST (MB) Non-Recoverable| | 
**b_taxassignment_isactive** | **bool** | Whether the Taxassignment is active or not | 

## Example

```python
from eZmaxApi.models.taxassignment_autocomplete_element_response import TaxassignmentAutocompleteElementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaxassignmentAutocompleteElementResponse from a JSON string
taxassignment_autocomplete_element_response_instance = TaxassignmentAutocompleteElementResponse.from_json(json)
# print the JSON string representation of the object
print TaxassignmentAutocompleteElementResponse.to_json()

# convert the object into a dict
taxassignment_autocomplete_element_response_dict = taxassignment_autocomplete_element_response_instance.to_dict()
# create an instance of TaxassignmentAutocompleteElementResponse from a dict
taxassignment_autocomplete_element_response_form_dict = taxassignment_autocomplete_element_response.from_dict(taxassignment_autocomplete_element_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


